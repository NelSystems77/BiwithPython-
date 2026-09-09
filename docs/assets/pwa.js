if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("sw.js").catch(() => {
      // Sin service worker el sitio sigue funcionando normal, solo sin cache offline.
    });
  });
}
