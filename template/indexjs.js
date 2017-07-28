/*
function addComment() {
  var text = $('#commentBox').val();
  list = document.querySelector('#previousComments');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
*/
var numComment = 0;

function addComment(){
  var text = $("#commentBox").val();
  if (numComment > 0) {
    $("#previousComments").prepend("<hr>");
  }
  $("#previousComments").prepend("<p>"+text+"</p>");
  numComment = numComment + 1;
}
function setup() {
  $("#ok_button").click(addComment);
  $("#maintitle").hide(0).fadeIn(7000)
}

function fadeTitle() {
  $("#maintitle").fadeTo(3000, .3);
}
$(document).ready(setup);
addComment("from JS file");
