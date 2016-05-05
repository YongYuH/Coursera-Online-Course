// put your javascript code here
$(document).ready(function(){
  var nav_source = $("#nav-template").html();
  var nav_template = Handlebars.compile(nav_source);
  var html = nav_template(animals_data);
  $("#nav").html(html); 

  var default_source = $("#default-template").html();
  var default_template = Handlebars.compile(default_source);
  var html =default_template(animals_data);
  $('#animals').html(html);

  var animals_source = $("#animals-template").html();
  var animals_template = Handlebars.compile(animals_source);
  // var html =animals_template(animals_data);
  // $('#animals').html(html);

  $("li.animal_btn").click(function(){
    var category_index = this.id.split("-")[0];
    var animals_index = this.id.split("-")[1];
    var specific_category = animals_data.category[category_index];
    var specific_content = specific_category.animals[animals_index];
    var html = animals_template(specific_category);
    $('#animals').html(html);
  });
});


