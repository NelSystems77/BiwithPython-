"""Soluciones de referencia para los retos del Modulo 5 - Visualizacion de datos."""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])
df["segmento_cliente"] = df["segmento_cliente"].fillna("Desconocido")
df = df.drop_duplicates()
df["margen_pct"] = df["utilidad"] / df["ingreso"]
df["periodo"] = df["fecha"].dt.to_period("M").astype(str)
df["dia_semana"] = df["fecha"].dt.day_name()

# 1. Ingreso total por region (barras)
ingreso_region = df.groupby("region")["ingreso"].sum().sort_values(ascending=False)
fig, ax = plt.subplots()
sns.barplot(x=ingreso_region.index, y=ingreso_region.values, hue=ingreso_region.index, legend=False, ax=ax)
ax.set_title("Ingreso total por region")
fig.savefig("solutions/reto5_1_ingreso_region.png", bbox_inches="tight")
plt.close(fig)

# 2. Margen promedio mensual (lineas)
margen_mensual = df.groupby("periodo")["margen_pct"].mean()
fig, ax = plt.subplots()
ax.plot(margen_mensual.index, margen_mensual.values, marker="o")
ax.set_title("Margen promedio mensual")
ax.tick_params(axis="x", rotation=90)
fig.savefig("solutions/reto5_2_margen_mensual.png", bbox_inches="tight")
plt.close(fig)

# 3. Scatter unidades vs ingreso coloreado por categoria (Plotly)
fig_scatter = px.scatter(df, x="unidades", y="ingreso", color="categoria", opacity=0.5)
fig_scatter.write_html("solutions/reto5_3_scatter.html")

# 4. Heatmap ingreso por dia de la semana y categoria
tabla = df.pivot_table(values="ingreso", index="dia_semana", columns="categoria", aggfunc="sum")
orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tabla = tabla.reindex(orden_dias)
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(tabla, annot=True, fmt=",.0f", cmap="YlOrRd", ax=ax)
ax.set_title("Ingreso por dia de la semana y categoria")
fig.savefig("solutions/reto5_4_heatmap_dia_categoria.png", bbox_inches="tight")
plt.close(fig)

print("Graficos guardados en la carpeta solutions/")
