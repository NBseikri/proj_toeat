    "use strict";
    $(document).ready(function(){
            $("#update_form").hide();
        });

    function toggleForm() {
       $("#update_form").toggle();
    }

    $("#manage_entry").on('click', toggleForm);

// Google Map with Marker
// function initMap() {
//       var restLocation = {
//         lat: {{ tracking.restaurant.lat }}, 
//         lng: {{ tracking.restaurant.lng }} 
//     };

//       var map = new google.maps.Map(document.getElementById('map'), {
//         zoom: 13,
//         center: restLocation
//       });

//       var marker = new google.maps.Marker({
//         position: restLocation,
//         map: map
//       });
//     }