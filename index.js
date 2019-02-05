$(document).ready(function() {
    var map = L.map('map', {
        center: [40.110130, -88.234201],
        zoom: 20
    });
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
   attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
});