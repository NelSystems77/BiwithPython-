# BI con Python: Zero to Hero 📊

Un curso practico, en espanol, para aprender **Business Intelligence (BI) y
Analisis de Datos con Python**, desde cero hasta construir tu propio
dashboard interactivo.

Aprenderas trabajando siempre sobre un caso de negocio real: **TiendaPy**,
una cadena retail ficticia, usando un dataset de ventas simulado.

## ¿Que vas a construir?

Al terminar el curso vas a tener:

- Una serie de notebooks con analisis de datos completo (carga, limpieza, EDA).
- Un conjunto de visualizaciones profesionales de las ventas de TiendaPy.
- Un **dashboard interactivo** construido con Streamlit ([`app/dashboard.py`](app/dashboard.py)).
- Tu propio proyecto final de BI, aplicando todo lo aprendido a un dataset propio.

## Estructura del repositorio

```
BiwithPython-/
├── data/                    # Datos del curso (se generan con scripts/generate_data.py)
├── notebooks/                # Los 8 modulos del curso, en orden
│   ├── 00_configuracion_entorno.ipynb
│   ├── 01_fundamentos_python.ipynb
│   ├── 02_pandas_basico.ipynb
│   ├── 03_limpieza_datos.ipynb
│   ├── 04_analisis_exploratorio.ipynb
│   ├── 05_visualizacion.ipynb
│   ├── 06_dashboard_streamlit.ipynb
│   └── 07_proyecto_final.ipynb
├── app/
│   ├── dashboard.py          # Dashboard final del curso (Streamlit)
│   └── ejemplo_minimo.py     # Ejemplo minimo usado en el modulo 6
├── solutions/                 # Soluciones de referencia para los retos de cada modulo
├── scripts/
│   └── generate_data.py       # Genera el dataset sintetico data/ventas.csv
├── requirements.txt
└── README.md
```

## Ruta del curso (Zero to Hero)

| # | Modulo | Que aprenderas |
|---|---|---|
| 0 | Configuracion del entorno | Instalar dependencias, entender el caso de negocio |
| 1 | Fundamentos de Python para BI | Variables, listas, diccionarios, condicionales, bucles, funciones |
| 2 | Pandas: cargar y explorar datos | `read_csv`, seleccion, filtrado, ordenamiento |
| 3 | Limpieza y transformacion de datos | Nulos, duplicados, tipos, feature engineering |
| 4 | Analisis exploratorio (EDA) y KPIs | `groupby`, `pivot_table`, indicadores de negocio |
| 5 | Visualizacion de datos | matplotlib, seaborn, plotly |
| 6 | Dashboards interactivos con Streamlit | Widgets, layout, cache, el dashboard final |
| 7 | Proyecto final | Tu propio analisis de BI de punta a punta |

Cada notebook combina teoria aplicada a negocio, codigo ejecutable y
**retos (🧠)** para practicar. Las soluciones de referencia estan en
`solutions/`.

## Como empezar

1. Clona el repositorio y entra a la carpeta del proyecto.

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Genera el dataset de practica:

   ```bash
   python scripts/generate_data.py
   ```

4. Abre Jupyter y sigue los notebooks en orden, desde `00` hasta `07`:

   ```bash
   jupyter notebook notebooks/
   ```

5. Cuando llegues al modulo 6, ejecuta el dashboard final (desde la raiz del
   proyecto, para que encuentre `data/ventas.csv`):

   ```bash
   streamlit run app/dashboard.py
   ```

   Se abrira en tu navegador en `http://localhost:8501`.

## El dataset: TiendaPy

`data/ventas.csv` contiene ventas simuladas (2023-2025) con estas columnas:

| Columna | Descripcion |
|---|---|
| `id_venta` | Identificador unico de la venta |
| `fecha` | Fecha de la venta |
| `region` | Norte, Sur, Centro, Este u Oeste |
| `categoria` | Electronica, Hogar, Ropa, Deportes u Oficina |
| `producto` | Nombre del producto vendido |
| `vendedor` | Nombre del vendedor |
| `segmento_cliente` | Individual, Pyme o Corporativo (con algunos nulos, a proposito) |
| `unidades` | Unidades vendidas |
| `precio_unitario` | Precio unitario del producto |
| `descuento_pct` | Descuento aplicado |
| `ingreso` | Ingreso neto de la venta |
| `costo` | Costo de la venta |
| `utilidad` | Utilidad de la venta (`ingreso - costo`) |

El dataset incluye a proposito valores nulos y filas duplicadas, para que el
Modulo 3 (limpieza de datos) tenga sentido practico.

## Requisitos

- Python 3.9 o superior.
- Conocimientos previos: ninguno. El curso parte desde cero en Python.

## Licencia

Material educativo de libre uso para fines de aprendizaje.
