"""Soluciones de referencia para los retos del Modulo 2 - Pandas basico."""

import pandas as pd

df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])

# 1. Total de filas y columnas
print("Filas:", df.shape[0], "- Columnas:", df.shape[1])

# 2. Ventas del vendedor "Ana Torres"
ventas_ana = df[df["vendedor"] == "Ana Torres"]
print("Ventas de Ana Torres:", len(ventas_ana))

# 3. Las 5 ventas con menor ingreso (mayor a 0)
menores_ingresos = df[df["ingreso"] > 0].sort_values("ingreso").head(5)
print(menores_ingresos[["fecha", "producto", "ingreso"]])

# 4. Ventas de Deportes en la region Sur con mas de 3 unidades
filtro = (df["categoria"] == "Deportes") & (df["region"] == "Sur") & (df["unidades"] > 3)
print("Ventas que cumplen el filtro:", filtro.sum())
