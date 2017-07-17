/*function addComment() {
  var text = $('#commentBox').val();
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
*/

function addComment(){
  var text = $("commentBox").val();
  $("commentSection").append(text);
}
function setup() {
  $("#ok_button").click(addListItem);

}

$(document).ready(setup);
addComment("from JS file");

function addListItem(text){
  list = document.$('#previousComments ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
