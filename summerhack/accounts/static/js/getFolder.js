$(document).ready(function() {

  var settings = {
   "async": true,
   "crossDomain": true,
   "url": "http://127.0.0.1:8000/tree/",
   "method": "GET",
   "headers": {
     "Authorization": "Basic cm9vdDpyb290",
     "Cache-Control": "no-cache",
     "Postman-Token": "ca0e836a-4d6e-479e-bf1d-a50b2a5c8e3a"
   }
  }

  $.ajax(settings).done(function (response) {
     var data = response.tree_list;
     data.forEach(function (element, index) {
       var node = document.createElement("TR");
       var mess = "test";
       var content = document.createTextNode(mess);
       node.appendChild(content);

       node.innerHTML = "<td>" + element.folder_path + "</td>" +
       "<td>" + element.key + "</td>" +
       "<td>" + element.created_at + "</td>" +
       "<td>" + element.updated_at + "</td>";
       $(".key-file").append(node);
       console.log(element);
       console.log(index);
     });
    // console.log(data)
  });
});