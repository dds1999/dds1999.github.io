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

/*function addComment(){
  var text = $("#commentBox").val();
  if (numComment > 0) {
    $("#previousComments").prepend("<hr>");
  }
  $("#previousComments").prepend("<p>"+text+"</p>");
  numComment = numComment + 1;
}
")*/

function addComment(text){
  $("#previousComments").prepend("<hr><p>"+text+"</p>");
  numComment = numComment + 1;
}

function addCommentSection(list) {
  alert("The comment was submitted")
  console.log("Working until here?")
  for (var i = 0; i < list.length; i++) {
    addComment(list[i]);
    console.log("broken?")
  }
}

function setup() {
  /*$("#commentInput").onsubmit();*/
  $("#maintitle").hide(0).fadeIn(7000)
}

function fadeTitle() {
  $("#maintitle").fadeTo(3000, .3);
}
$(document).ready(setup);
