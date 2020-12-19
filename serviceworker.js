const cacheName = 'djangopwa-v1';
const cacheAssets = [
  './',
  // './account/templates/account/account.html',
  // './account/templates/account/register.html',
  // './account/templates/account/login.html',
  // './account/templates/account/must_authenticate.html',
  './static/js/script.js',
  './static/css/style.css',
  './static/img/favico.png',
  './static/img/fondo.jpeg',
  './static/img/ofertas/oferta1.jpeg',
  './static/img/ofertas/oferta2.jpeg',
  './static/img/ofertas/oferta3.jpeg',
  './static/img/ofertas/oferta4.jpeg',
  './static/img/carrusel/banner1.jpeg',
  './static/img/carrusel/banner2.jpeg',
  './static/img/carrusel/banner3.jpeg'
  ];


// Call Install Event
self.addEventListener('install', e => {
  console.log('Service Worker: Installed');

  e.waitUntil(
    caches
      .open(cacheName)
      .then(cache => {
        console.log('Service Worker: Caching Files');
        cache.addAll(cacheAssets);
      })
      .then(() => self.skipWaiting())
  );
});

// Call Activate Event
self.addEventListener('activate', e => {
  console.log('Service Worker: Activated');
  // Remove unwanted caches
  e.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== cacheName) {
            console.log('Service Worker: Clearing Old Cache');
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

// Call Fetch Event
self.addEventListener('fetch', e => {
  console.log('Service Worker: Fetching');
  e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
});