$(document).ready(function() {

var resultscan;
var AllFile;

setInterval(function () {
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
	};
  $.ajax(settings).done(function getResult(response) {
      var data = response.tree_list;
      if (data != AllFile) {
      	AllFile = data;
	$("tr[id*='Destroyit']").each(function (i, el) {
	    el.remove();
	});
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
      }
  })}, 5000);

setInterval(function () {
  	var settings = {
  	    "async": true,
  	    "crossDomain": true,
  	    "url": "http://127.0.0.1:8000/buffer/",
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
         var node = document.createElement("DIV");
         node.setAttribute('class', 'message alert alert-danger');
         var mess = " ";
         var content = document.createTextNode(mess);
         var datatmp = JSON.stringify(data);
         datatmp = datatmp.replace(/["[\]]/gm, "");
      	 datatmp = datatmp.replace(/\\n/gm, "<br>");
      	 datatmp = datatmp.replace(/,/gm, "");
      	 if (resultscan != datatmp) {
      	     $("div[class*='message']").each(function (i, el) {
            		el.remove();
      	     });
             node.innerHTML = datatmp;
             node.appendChild(content);
             $(".resultScan").append(node);
      	     resultscan = datatmp;
	        }
       } else {
         if (resultscan != data) {
             $("div[class*='message']").each(function (i, el) {
                el.remove();
             });
             var node = document.createElement("DIV");
             node.setAttribute('class', 'message alert alert-success');
             var mess = "EVERYTHING IS OK ! :)";
             var content = document.createTextNode(mess);
             node.appendChild(content);
             $(".resultScan").append(node);
           }
        }
       console.log(data);
    })}, 5000);
});
