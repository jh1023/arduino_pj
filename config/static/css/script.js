var map;

function initMap() {
  var seoul = { lat: 36.35871237152672 ,lng: 127.3842626232509 };
  map = new google.maps.Map( document.getElementById('map'), {
      zoom: 12,
      center: seoul
    });

  new google.maps.Marker({
    position: seoul,
    map: map,
    label: "대전 서구청"
  });
}