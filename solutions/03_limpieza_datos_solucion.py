"""Soluciones de referencia para los retos del Modulo 3 - Limpieza de datos."""

import pandas as pd

df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])
df["segmento_cliente"] = df["segmento_cliente"].fillna("Desconocido")
df = df.drop_duplicates()
df["margen_pct"] = df["utilidad"] / df["ingreso"]

# 1. Rango de fechas
print("Fecha minima:", df["fecha"].min())
print("Fecha maxima:", df["fecha"].max())

# 2. Columna es_fin_de_semana
df["es_fin_de_semana"] = df["fecha"].dt.day_name().isin(["Saturday", "Sunday"])
print(df["es_fin_de_semana"].value_counts())

# 3. Ventas con margen_pct <= 0
ventas_sin_margen = df[df["margen_pct"] <= 0]
print("Ventas con margen <= 0:", len(ventas_sin_margen))
print(ventas_sin_margen["descuento_pct"].describe())
# El costo se fija como 60% del precio de lista, pero el ingreso se calcula
# aplicando el descuento_pct. Con descuentos altos (0.15-0.2) el ingreso
# puede acercarse mucho al costo, dejando el margen muy bajo o negativo.

# 4. Columna rango_ingreso
df["rango_ingreso"] = pd.cut(
    df["ingreso"],
    bins=[-float("inf"), 30000, 100000, float("inf")],
    labels=["Bajo", "Medio", "Alto"],
)
print(df["rango_ingreso"].value_counts())
