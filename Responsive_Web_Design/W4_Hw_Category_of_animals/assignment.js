// put your javascript code here
$(document).ready(function(){
  var nav_source = $("#nav-template").html();
  var nav_template = Handlebars.compile(nav_source);
  var html = nav_template(animals_data);
  $("#nav").html(html); 

  var default_source = $("#default-template").html();
  var default_template = Handlebars.compile(default_source);
  var html =default_template(animals_data);
  $('#category').html(html);

  var category_source = $("#category-template").html();
  var category_template = Handlebars.compile(category_source);

  var animals_source = $("#animals-template").html();
  var animals_template = Handlebars.compile(animals_source);

  $("a.dropdown-toggle").click(function(){
    var category_index = this.id;
    var specific_category = animals_data.category[category_index];
    var html = category_template(specific_category);
    $('#category').html(html);
    $('#animals').empty();
  });

  $("li.animal_btn").click(function(){
    var category_index = this.id.split("-")[0];
    var animals_index = this.id.split("-")[1];
    var specific_content = animals_data.category[category_index].animals[animals_index];
    var html = animals_template(specific_content);
    $('#animals').html(html);
  });

  $("a.show_all").click(function(){
    var show_all_source = $("#show-all-template").html();
    var show_all_template = Handlebars.compile(show_all_source);
    var html = show_all_template(animals_data);
    $('#category').html(html);
    $('#animals').empty();
  });
});


