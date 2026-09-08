"""
Genera el dataset sintetico de ventas usado en todo el curso "BI con Python: Zero to Hero".

Uso:
    python scripts/generate_data.py

Crea data/ventas.csv con ventas simuladas de una cadena retail ficticia
(TiendaPy) durante 3 anos, con estacionalidad, regiones, categorias de
producto y vendedores.
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(seed=42)

REGIONES = ["Norte", "Sur", "Centro", "Este", "Oeste"]

CATEGORIAS_PRODUCTOS = {
    "Electronica": ["Audifonos", "Cargador", "Mouse", "Teclado", "Parlante Bluetooth"],
    "Hogar": ["Lampara LED", "Set de Ollas", "Aspiradora", "Cafetera", "Ventilador"],
    "Ropa": ["Camiseta", "Pantalon", "Chaqueta", "Zapatillas", "Gorra"],
    "Deportes": ["Balon Futbol", "Mancuernas", "Bicicleta", "Colchoneta Yoga", "Bototas Trekking"],
    "Oficina": ["Cuaderno", "Silla Ergonomica", "Escritorio", "Impresora", "Resma de Papel"],
}

SEGMENTOS_CLIENTE = ["Individual", "Pyme", "Corporativo"]

VENDEDORES = [
    "Ana Torres", "Bruno Silva", "Carla Diaz", "Diego Rojas", "Elena Vidal",
    "Felipe Soto", "Gabriela Nunez", "Hugo Reyes", "Isidora Munoz", "Javier Castro",
]

PRECIOS_BASE = {
    "Audifonos": 15990, "Cargador": 8990, "Mouse": 6990, "Teclado": 12990, "Parlante Bluetooth": 24990,
    "Lampara LED": 9990, "Set de Ollas": 39990, "Aspiradora": 79990, "Cafetera": 29990, "Ventilador": 19990,
    "Camiseta": 7990, "Pantalon": 15990, "Chaqueta": 34990, "Zapatillas": 44990, "Gorra": 5990,
    "Balon Futbol": 12990, "Mancuernas": 17990, "Bicicleta": 149990, "Colchoneta Yoga": 9990, "Bototas Trekking": 54990,
    "Cuaderno": 1990, "Silla Ergonomica": 89990, "Escritorio": 99990, "Impresora": 69990, "Resma de Papel": 3990,
}

COSTO_RATIO = 0.6  # el costo es ~60% del precio de venta


def _producto_a_categoria():
    mapping = {}
    for categoria, productos in CATEGORIAS_PRODUCTOS.items():
        for p in productos:
            mapping[p] = categoria
    return mapping


def generar_ventas(n_filas: int = 12000) -> pd.DataFrame:
    productos = list(PRECIOS_BASE.keys())
    producto_a_categoria = _producto_a_categoria()

    fechas = pd.date_range("2023-01-01", "2025-12-31", freq="D")
    dia_del_anio = np.array(fechas.dayofyear, dtype=float)
    pesos_estacionales = 1 + 0.5 * np.sin(2 * np.pi * (dia_del_anio / 365) + 1.2)
    pesos_estacionales = pesos_estacionales / pesos_estacionales.sum()
    fechas_elegidas = RNG.choice(fechas, size=n_filas, p=pesos_estacionales)

    productos_elegidos = RNG.choice(productos, size=n_filas)
    unidades = RNG.integers(1, 8, size=n_filas)

    precios_base = np.array([PRECIOS_BASE[p] for p in productos_elegidos])
    ruido_precio = RNG.normal(1.0, 0.05, size=n_filas)
    precio_unitario = np.round(precios_base * ruido_precio, -1)

    descuento_pct = RNG.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2], size=n_filas)

    df = pd.DataFrame({
        "fecha": fechas_elegidas,
        "region": RNG.choice(REGIONES, size=n_filas),
        "categoria": [producto_a_categoria[p] for p in productos_elegidos],
        "producto": productos_elegidos,
        "vendedor": RNG.choice(VENDEDORES, size=n_filas),
        "segmento_cliente": RNG.choice(SEGMENTOS_CLIENTE, size=n_filas, p=[0.55, 0.3, 0.15]),
        "unidades": unidades,
        "precio_unitario": precio_unitario,
        "descuento_pct": descuento_pct,
    })

    df["ingreso"] = np.round(df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"]), 0)
    df["costo"] = np.round(df["unidades"] * df["precio_unitario"] * COSTO_RATIO, 0)
    df["utilidad"] = df["ingreso"] - df["costo"]

    # Introducimos algunos problemas de calidad de datos a proposito,
    # para que el modulo de limpieza tenga sentido.
    idx_nulos = RNG.choice(df.index, size=int(n_filas * 0.02), replace=False)
    df.loc[idx_nulos, "segmento_cliente"] = np.nan

    idx_duplicados = RNG.choice(df.index, size=30, replace=False)
    df = pd.concat([df, df.loc[idx_duplicados]], ignore_index=True)

    df = df.sort_values("fecha").reset_index(drop=True)
    df["id_venta"] = range(1, len(df) + 1)

    columnas = [
        "id_venta", "fecha", "region", "categoria", "producto", "vendedor",
        "segmento_cliente", "unidades", "precio_unitario", "descuento_pct",
        "ingreso", "costo", "utilidad",
    ]
    return df[columnas]


if __name__ == "__main__":
    df = generar_ventas()
    df.to_csv("data/ventas.csv", index=False)
    print(f"Dataset generado: data/ventas.csv ({len(df)} filas, {df.shape[1]} columnas)")
