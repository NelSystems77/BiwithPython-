"""
Dashboard de BI interactivo para TiendaPy, construido con Streamlit.

Uso:
    streamlit run app/dashboard.py

Este dashboard es el resultado final del curso "BI con Python: Zero to Hero".
Integra todo lo aprendido: carga y limpieza de datos (pandas), calculo de
KPIs, y visualizacion interactiva (plotly), todo dentro de una interfaz web
filtrable.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="TiendaPy - Dashboard de Ventas",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])
    df["segmento_cliente"] = df["segmento_cliente"].fillna("Desconocido")
    df = df.drop_duplicates()
    df["margen_pct"] = df["utilidad"] / df["ingreso"]
    df["anio"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    df["dia_semana"] = df["fecha"].dt.day_name()
    return df


df = cargar_datos()

st.sidebar.title("🔎 Filtros")

rango_fechas = st.sidebar.date_input(
    "Rango de fechas",
    value=(df["fecha"].min().date(), df["fecha"].max().date()),
    min_value=df["fecha"].min().date(),
    max_value=df["fecha"].max().date(),
)

regiones = st.sidebar.multiselect(
    "Region", options=sorted(df["region"].unique()), default=sorted(df["region"].unique())
)
categorias = st.sidebar.multiselect(
    "Categoria", options=sorted(df["categoria"].unique()), default=sorted(df["categoria"].unique())
)
segmentos = st.sidebar.multiselect(
    "Segmento de cliente",
    options=sorted(df["segmento_cliente"].unique()),
    default=sorted(df["segmento_cliente"].unique()),
)

if len(rango_fechas) == 2:
    fecha_inicio, fecha_fin = rango_fechas
else:
    fecha_inicio, fecha_fin = df["fecha"].min().date(), df["fecha"].max().date()

filtro = (
    (df["fecha"].dt.date >= fecha_inicio)
    & (df["fecha"].dt.date <= fecha_fin)
    & (df["region"].isin(regiones))
    & (df["categoria"].isin(categorias))
    & (df["segmento_cliente"].isin(segmentos))
)
df_filtrado = df[filtro]

st.title("📊 TiendaPy - Dashboard de Ventas")
st.caption("Proyecto capstone del curso BI con Python: Zero to Hero")

if df_filtrado.empty:
    st.warning("No hay datos para los filtros seleccionados. Ajusta los filtros en la barra lateral.")
    st.stop()

# --- KPIs ---
ingreso_total = df_filtrado["ingreso"].sum()
utilidad_total = df_filtrado["utilidad"].sum()
margen_promedio = utilidad_total / ingreso_total if ingreso_total else 0
ticket_promedio = df_filtrado["ingreso"].mean()
num_ventas = len(df_filtrado)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Ingreso total", f"${ingreso_total:,.0f}")
col2.metric("Utilidad total", f"${utilidad_total:,.0f}")
col3.metric("Margen promedio", f"{margen_promedio:.1%}")
col4.metric("Ticket promedio", f"${ticket_promedio:,.0f}")
col5.metric("N° de ventas", f"{num_ventas:,}")

st.divider()

# --- Tendencia mensual ---
st.subheader("Tendencia de ingresos y utilidad")
tendencia = df_filtrado.groupby("mes", as_index=False)[["ingreso", "utilidad"]].sum()
fig_tendencia = px.line(
    tendencia, x="mes", y=["ingreso", "utilidad"], markers=True,
    labels={"mes": "Mes", "value": "Monto ($)", "variable": "Metrica"},
)
fig_tendencia.update_layout(xaxis_tickangle=-90, legend_title_text="")
st.plotly_chart(fig_tendencia, use_container_width=True)

col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("Top 10 productos por ingreso")
    top_productos = (
        df_filtrado.groupby("producto", as_index=False)["ingreso"]
        .sum()
        .sort_values("ingreso", ascending=False)
        .head(10)
    )
    fig_productos = px.bar(
        top_productos, x="ingreso", y="producto", orientation="h",
        color="ingreso", color_continuous_scale="Blues",
        labels={"ingreso": "Ingreso ($)", "producto": ""},
    )
    fig_productos.update_layout(yaxis={"categoryorder": "total ascending"}, coloraxis_showscale=False)
    st.plotly_chart(fig_productos, use_container_width=True)

with col_der:
    st.subheader("Participacion por categoria")
    participacion = df_filtrado.groupby("categoria", as_index=False)["ingreso"].sum()
    fig_categoria = px.pie(
        participacion, values="ingreso", names="categoria", hole=0.4,
    )
    st.plotly_chart(fig_categoria, use_container_width=True)

st.subheader("Ingreso por region y categoria")
tabla_calor = df_filtrado.pivot_table(values="ingreso", index="categoria", columns="region", aggfunc="sum", fill_value=0)
fig_heatmap = px.imshow(
    tabla_calor, text_auto=",.0f", color_continuous_scale="YlGnBu",
    labels={"color": "Ingreso ($)"},
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.subheader("Ranking de vendedores")
ranking_vendedores = (
    df_filtrado.groupby("vendedor")
    .agg(ingreso_total=("ingreso", "sum"), utilidad_total=("utilidad", "sum"), num_ventas=("id_venta", "count"))
    .sort_values("ingreso_total", ascending=False)
    .reset_index()
)
st.dataframe(
    ranking_vendedores.style.format({"ingreso_total": "${:,.0f}", "utilidad_total": "${:,.0f}"}),
    use_container_width=True,
    hide_index=True,
)

with st.expander("Ver datos filtrados (tabla completa)"):
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)
