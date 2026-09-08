"""Soluciones de referencia para los retos del Modulo 4 - EDA y KPIs."""

import pandas as pd

df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])
df["segmento_cliente"] = df["segmento_cliente"].fillna("Desconocido")
df = df.drop_duplicates()
df["margen_pct"] = df["utilidad"] / df["ingreso"]
df["periodo"] = df["fecha"].dt.to_period("M")

# 1. Ingreso, utilidad y margen promedio por categoria
resumen_categoria = df.groupby("categoria").agg(
    ingreso_total=("ingreso", "sum"),
    utilidad_total=("utilidad", "sum"),
    margen_promedio=("margen_pct", "mean"),
)
print(resumen_categoria)

# 2. Segmento de cliente que genera mas utilidad
segmento_top = df.groupby("segmento_cliente")["utilidad"].sum().idxmax()
print("Segmento con mas utilidad:", segmento_top)

# 3. Ticket promedio por producto y segmento_cliente
tabla_ticket = pd.pivot_table(
    df, values="ingreso", index="producto", columns="segmento_cliente", aggfunc="mean"
)
print(tabla_ticket.round(0))

# 4. Mes con mayor y menor ingreso
ingreso_mensual = df.groupby("periodo")["ingreso"].sum()
print("Mes con mayor ingreso:", ingreso_mensual.idxmax(), ingreso_mensual.max())
print("Mes con menor ingreso:", ingreso_mensual.idxmin(), ingreso_mensual.min())

# 5. Numero de ventas y margen promedio por vendedor
resumen_vendedor = (
    df.groupby("vendedor")
    .agg(num_ventas=("id_venta", "count"), margen_promedio=("margen_pct", "mean"))
    .sort_values("margen_promedio", ascending=False)
)
print(resumen_vendedor)
