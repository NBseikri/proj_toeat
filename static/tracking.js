"use strict";

// Toggle for Manage Entry Form

$(document).ready(function(){$("#update_form").hide();});

function toggleForm() {$("#update_form").toggle();}

$("#manage_entry").on('click', toggleForm);

// Toggle for Update Review when 'Mark as Visited' is selected

$(document).ready(function(){$("#update_review").hide();});

function toggleUpdate() {$("#update_review").toggle();}

$("#update_visited").on('click', toggleUpdate);

// Google Map with Marker

var lat = $('#latlng').attr('data-lat');
var lng = $('#latlng').attr('data-lng');
 
function initMap() {var restLocation = {lat: +lat, lng: +lng};
    var map = new google.maps.Map(document.getElementById('map'), {zoom: 15, center: restLocation});
    var marker = new google.maps.Marker({position: restLocation, map: map});
}

initMap();