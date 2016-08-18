/**
 * Created by raquel on 21/07/16.
 */

var global;
var mapglobal;
var entra = false;


function initialize1(id_pac){

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: -2.161639, lng: -79.924639}
    });

    global = id_pac;
    mapglobal = map;

    localizacionPaciente();
    setInterval(localizacionPaciente, 4000);

}

function localizacionPaciente() {

    $.post( "/mapa/lngPac/"+global+"/",{ },
              function( data ) {

                    var posicion = data.length;
                    var posFinal = posicion-1;
                    var dispo = data[posFinal];


                  // console.log("yoooo", data[i].lat, data[i].lng);

                  if(entra){
                      marker.setMap(null);
                  }

                  marker = new google.maps.Marker({
                      position: new google.maps.LatLng(parseFloat(dispo.lat), parseFloat(dispo.lng)),
                      map: mapglobal,
                      animation: google.maps.Animation.BOUNCE,
                      icon:src="/static/img/corazon_peq.png",
                  });

                  entra = true;
                  

                  //$( ".result" ).html( data );
                  console.log(data);
              }
        );
}