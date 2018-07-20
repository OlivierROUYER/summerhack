$(document).ready(function() {

setInterval(function () {
	var settings = {
	    "async": true,
	    "crossDomain": true,
	    "url": "http://172.16.15.7:8000/tree/",
	    "method": "GET",
	    "headers": {
		"Authorization": "Basic cm9vdDpyb290",
		"Cache-Control": "no-cache",
		"Postman-Token": "ca0e836a-4d6e-479e-bf1d-a50b2a5c8e3a"
	    }
	};
  $("tr[id*='Destroyit']").each(function (i, el) {
      el.remove();
  });
  $.ajax(settings).done(function getResult(response) {
	   var data = response.tree_list;
     data.forEach(function (element, index) {
       var node = document.createElement("TR");
       node.setAttribute("id", "Destroyit");
       var mess = "test";
       var content = document.createTextNode(mess);
       node.appendChild(content);

       node.innerHTML = "<td>" + element.folder_path + "</td>" +
       "<td>" + element.key + "</td>" +
       "<td>" + element.created_at + "</td>" +
       "<td>" + element.updated_at + "</td>";
       $(".key-file").append(node);
     });
  })}, 5000);

setInterval(function () {
  	var settings = {
  	    "async": true,
  	    "crossDomain": true,
  	    "url": "http://172.16.15.7:8000/buffer/",
  	    "method": "GET",
  	    "headers": {
  		  "Authorization": "Basic cm9vdDpyb290",
  		  "Cache-Control": "no-cache",
  		  "Postman-Token": "ca0e836a-4d6e-479e-bf1d-a50b2a5c8e3a"
  	   }
  	};

    $.ajax(settings).done(function getResult(response) {
  	   var data = response.buffer2;
       if (data.length != 0) {

       } else {
         var node = document.createElement("DIV");
         var mess = "test";
        }
       console.log(data);
    })}, 5000);
});
