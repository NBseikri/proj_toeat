"use strict";

// Add a Restaurant Div
$(document).ready(function(){$("#track").hide();});

function toggleTrackingNote() {$("#track").toggle();
    if ($("#yes").attr("disabled") === 'disabled') {
        $("#yes").attr("disabled", false);
    }
    else {
        $("#yes").attr("disabled", true);
   }
}

$("#no").on('click', toggleTrackingNote);

$(document).ready(function(){$("#review").hide();});

function toggleReview() {$("#review").toggle();
    if ($("#no").attr("disabled") === 'disabled') {
        $("#no").attr("disabled", false);
    }
    else {
        $("#no").attr("disabled", true);
   }
}

$("#yes").on('click', toggleReview);

var input = document.getElementById('searchTextField');

var defaultBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(85, -180), 
    new google.maps.LatLng(-85, 180));

var options = {bounds: defaultBounds, types: ['establishment']};

var autocomplete = new google.maps.places.Autocomplete(input, options);
    autocomplete.addListener('place_changed', getDetails);

function getDetails() {var place = autocomplete.getPlace();}

$(document).ready(function(){$("#tracking_form").hide();});

function toggleDiv() {$("#tracking_form").toggle();}

$("#add_rest_header").on('click', toggleDiv);

// Restaurant List Div
$(document).ready(function(){$("#rest_list").hide();});

function toggleRestDiv() {$("#rest_list").toggle();}

$("#list_header").on('click', toggleRestDiv);

// Filter and Sort Divs
function showOrg(result) {
    var data = result.data;
    $("#original_rest").empty();
    for (var i in data) {
        var photo = data[i]['photo'];
        var newPhotoHTML = ("<div class='rest_photo'><img src='" + photo + "'width='100' height='100'></a></div>");

        var id = data[i]['tracking_id'];
        var rest_name = data[i]['rest_name'];
        var newLink = ("<a href=/tracking/" + id + ">" + rest_name + "</a>");


        var visited = data[i]['visited'];
        var newVisit = ("<p>" + visited +"</p>");

        var city = data[i]['city'];
        var newCity = ("<p>" + city +"</p>");

        $("#original_rest").append(newPhotoHTML, newLink, newCity, newVisit);

    }
}

function orgRequest(evt) {
    evt.preventDefault();
    var formInputs = {
        "filter" : $("#filter_select").val(),
    };
    $.get("/filter_rest", formInputs, showOrg);
}

$("#filter_form").on("submit", orgRequest);


function sortRequest(evt){
    evt.preventDefault();
    var sortInputs = {
        "sort" : $("#sort_select").val(),
    };
    $.get("/sort_rest", sortInputs, showOrg);
}

$("#sort_form").on("submit", sortRequest);

// Friends Div
$(document).ready(function(){$("#friend_info").hide();});

function toggleFriendDiv() {$("#friend_info").toggle();}

$("#friend_header").on('click', toggleFriendDiv);