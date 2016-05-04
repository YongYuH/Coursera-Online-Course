// put your javascript code here
$(document).ready(function(){
  var nav_source = $("#nav-template").html();
  var nav_template = Handlebars.compile(nav_source);
  var html = nav_template(animals_data);
  $("#nav").html(html); 

  var animals_source = $("#animals-template").html();
  var animals_template = Handlebars.compile(animals_source);
  var html =animals_template(animals_data);
  $('#animals').html(html);

  // $("li.animal_btn").click(function(){
  //   var html =animals_template(animals_data);
  //   $('#animals').html(html);
  // });
});


