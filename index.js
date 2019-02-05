$(document).ready(function() {
    var map = L.map('mapid', {
        center: [40.110130, -88.234201],
        zoom: 20
    });
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoic21pZ2h0eWNyZWVwIiwiYSI6ImNqcnM0ZmpyZDA3dDYzeWtjZm12emk4YzMifQ.9by-yOi2EOyroTdyc4cmpw'
}).addTo(map);
});