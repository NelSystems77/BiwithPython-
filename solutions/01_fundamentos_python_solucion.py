"""Soluciones de referencia para los retos del Modulo 1 - Fundamentos de Python."""

ventas = [
    {"producto": "Mouse", "region": "Norte", "unidades": 5, "precio_unitario": 6990},
    {"producto": "Teclado", "region": "Sur", "unidades": 2, "precio_unitario": 12990},
    {"producto": "Monitor", "region": "Centro", "unidades": 1, "precio_unitario": 129990},
]


# 1. Ingreso promedio por venta
def ingreso_promedio(ventas):
    ingresos = [v["unidades"] * v["precio_unitario"] for v in ventas]
    return sum(ingresos) / len(ingresos)


# 2. Venta con mayor ingreso
def mejor_venta(ventas):
    return max(ventas, key=lambda v: v["unidades"] * v["precio_unitario"])


# 3. Productos con ingreso mayor a 50.000
def productos_ingreso_alto(ventas, umbral=50000):
    return [v["producto"] for v in ventas if v["unidades"] * v["precio_unitario"] > umbral]


# 4. Ingreso total por region
def resumen_por_region(ventas):
    resumen = {}
    for v in ventas:
        ingreso = v["unidades"] * v["precio_unitario"]
        resumen[v["region"]] = resumen.get(v["region"], 0) + ingreso
    return resumen


if __name__ == "__main__":
    print("Ingreso promedio:", ingreso_promedio(ventas))
    print("Mejor venta:", mejor_venta(ventas))
    print("Productos con ingreso > 50.000:", productos_ingreso_alto(ventas))
    print("Resumen por region:", resumen_por_region(ventas))
