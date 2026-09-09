// Service worker del sitio "BI con Python: Zero to Hero".
// Cachea el "app shell" (landing page, dashboard, notebooks estaticos y
// assets) para que el sitio se pueda instalar y abrir sin conexion tras la
// primera visita. No toca docs/lite/ (JupyterLite trae su propio service
// worker, con su propio alcance) ni las librerias que se cargan desde CDN
// (esas siempre necesitan internet, igual que cualquier app que corre
// Python en el navegador).

const CACHE_VERSION = "v1";
const CACHE_NAME = "bi-python-zth-" + CACHE_VERSION;

const PRECACHE_URLS = [
  "./",
  "./index.html",
  "./dashboard.html",
  "./manifest.json",
  "./assets/style.css",
  "./assets/pwa.js",
  "./assets/progress.js",
  "./data/ventas.csv",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon-192-maskable.png",
  "./icons/icon-512-maskable.png",
  "./icons/apple-touch-icon.png",
  "./notebooks/00_configuracion_entorno.html",
  "./notebooks/01_fundamentos_python.html",
  "./notebooks/02_pandas_basico.html",
  "./notebooks/03_limpieza_datos.html",
  "./notebooks/04_analisis_exploratorio.html",
  "./notebooks/05_visualizacion.html",
  "./notebooks/06_dashboard_streamlit.html",
  "./notebooks/07_proyecto_final.html",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

function isOwnScope(url) {
  return url.origin === self.location.origin && !url.pathname.includes("/lite/");
}

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (!isOwnScope(url)) return; // deja pasar CDNs y todo lo que sirve docs/lite/

  event.respondWith(
    caches.match(request).then((cached) => {
      const network = fetch(request)
        .then((response) => {
          if (response && response.ok) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
          }
          return response;
        })
        .catch(() => cached);
      // Stale-while-revalidate: sirve cache al instante si existe,
      // y actualiza en segundo plano cuando hay red.
      return cached || network;
    })
  );
});
