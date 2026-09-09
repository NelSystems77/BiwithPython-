# BI con Python: Zero to Hero 📊

Un curso practico, en espanol, para aprender **Business Intelligence (BI) y
Analisis de Datos con Python**, desde cero hasta construir tu propio
dashboard interactivo.

Aprenderas trabajando siempre sobre un caso de negocio real: **TiendaPy**,
una cadena retail ficticia, usando un dataset de ventas simulado.

## 🌐 Ver el curso online

Todo el curso esta publicado como sitio estatico en GitHub Pages, sin
necesidad de instalar nada:

**👉 [Abrir el curso](https://nelsystems77.github.io/BiwithPython-/)**

Ahi encontraras los 8 notebooks corriendo **Python de verdad en tu
navegador** (edita y ejecuta cada celda, gracias a
[JupyterLite](https://jupyterlite.readthedocs.io/) + Pyodide/WebAssembly),
y un **dashboard interactivo real** que tambien corre 100% del lado del
cliente usando [stlite](https://github.com/whitphx/stlite) — Streamlit
compilado a WebAssembly. Ninguno de los dos necesita servidor.

> Si el link de arriba no carga, es porque GitHub Pages todavia no esta
> habilitado para este repositorio. Ve a **Settings → Pages** y configura
> **Source: Deploy from a branch**, eligiendo la rama correspondiente y la
> carpeta **`/docs`**. Ver la seccion [Publicar en GitHub Pages](#-publicar-en-github-pages) mas abajo.

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
├── docs/                       # Sitio estatico publicado en GitHub Pages
│   ├── index.html              # Landing page del curso
│   ├── dashboard.html          # Dashboard interactivo (stlite / WebAssembly)
│   ├── lite/                   # Notebooks ejecutables (JupyterLite / Pyodide)
│   ├── notebooks/*.html        # Notebooks exportados a HTML (respaldo, solo lectura)
│   ├── app/streamlit_app.py    # Copia de app/dashboard.py para stlite
│   └── data/ventas.csv         # Copia del dataset, servida al dashboard web
├── requirements.txt
├── requirements-dev.txt        # Solo para regenerar docs/lite/ (ver mas abajo)
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

## 🚀 Publicar en GitHub Pages

Este repositorio ya trae listo todo lo necesario para publicarse como sitio
estatico en la carpeta [`docs/`](docs/). Para activarlo:

1. En GitHub, ve a **Settings → Pages** del repositorio.
2. En **Source**, elige **Deploy from a branch**.
3. En **Branch**, selecciona la rama que quieras publicar (por ejemplo `main`
   despues de mergear este trabajo) y la carpeta **`/docs`**.
4. Guarda. GitHub publicara el sitio en unos minutos en
   `https://<tu-usuario>.github.io/<tu-repo>/`.

### Que incluye el sitio publicado

- **`docs/index.html`**: landing page con el roadmap del curso.
- **`docs/lite/`**: los 8 notebooks corriendo **de verdad** en el navegador
  vía [JupyterLite](https://jupyterlite.readthedocs.io/) + el kernel de
  Pyodide — puedes editar y ejecutar cada celda, sin backend. Cada tarjeta
  de modulo en la landing page enlaza directo a
  `lite/notebooks/index.html?path=notebooks/<archivo>.ipynb`.
- **`docs/notebooks/*.html`**: los mismos 8 notebooks exportados con
  `nbconvert` como respaldo de solo lectura (por si JupyterLite tarda en
  cargar o el navegador no soporta WebAssembly).
- **`docs/dashboard.html`**: el dashboard de Streamlit corriendo **100% en
  el navegador**, sin backend, gracias a
  [stlite](https://github.com/whitphx/stlite) (Streamlit + Pyodide/WebAssembly).
  Usa el mismo codigo que `app/dashboard.py`, copiado en
  `docs/app/streamlit_app.py` junto con una copia del dataset en
  `docs/data/ventas.csv`.

### Regenerar el sitio despues de cambiar el curso

Si modificas los notebooks, el dataset o el dashboard, regenera el sitio
estatico:

```bash
# 1. Volver a exportar los notebooks a HTML (respaldo de solo lectura)
jupyter nbconvert --to html --output-dir docs/notebooks notebooks/*.ipynb

# 2. Reconstruir la version ejecutable con JupyterLite
pip install -r requirements-dev.txt
./scripts/build_jupyterlite.sh

# 3. Sincronizar los datos y el codigo del dashboard con la version web
cp data/ventas.csv docs/data/ventas.csv
cp app/dashboard.py docs/app/streamlit_app.py
```

> Nota: `docs/app/streamlit_app.py` es una copia adaptada de
> `app/dashboard.py` porque stlite necesita que el archivo viva dentro de
> `docs/` para poder servirlo como parte del sitio estatico.

### Limitaciones de las versiones web

- La primera carga tarda 20-40 segundos tanto en el dashboard como en cada
  notebook: el navegador descarga un interprete de Python (Pyodide) y las
  librerias necesarias (`pandas`, `plotly`, `jinja2`, etc.).
- Corren completamente en el dispositivo del usuario, asi que en equipos muy
  limitados pueden sentirse mas lentas que trabajar localmente.
- En los notebooks de JupyterLite, los cambios **no se guardan** al cerrar
  la pestaña (viven en memoria del navegador). Para un entorno persistente,
  clona el repo y usa `jupyter notebook notebooks/` normalmente.
- Para desarrollar y depurar el dashboard, sigue usando
  `streamlit run app/dashboard.py` localmente; es mas rapido para iterar.

## Licencia

Material educativo de libre uso para fines de aprendizaje.
