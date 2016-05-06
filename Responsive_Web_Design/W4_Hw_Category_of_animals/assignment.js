$(document).ready(function(){
  // use handlebar.js to render nav-template to navbar
  var nav_source = $("#nav-template").html();
  var nav_template = Handlebars.compile(nav_source);
  var html = nav_template(animals_data);
  $("#nav").html(html); 

  // use handlebar.js to render default-template to whole page
  var default_source = $("#default-template").html();
  var default_template = Handlebars.compile(default_source);
  var html =default_template(animals_data);
  $('#category').html(html);

  // use handlebar.js template to render specific javascript object to whole page when clicking buttons in the navbar
  $("li.animal_btn").click(function(){
    // load the necessary data when click the button in the navbar
    var category_source = $("#category-template").html();
    var category_template = Handlebars.compile(category_source);

    var animals_source = $("#animals-template").html();
    var animals_template = Handlebars.compile(animals_source);

    var category_index = this.id.split("-")[0];
    var animals_index = this.id.split("-")[1];
    var specific_category = animals_data.category[category_index];
    var specific_content = animals_data.category[category_index].animals[animals_index];

    // use handlebar.js to render category-template to category div
    var category_html = category_template(specific_category);
    $('#category').html(category_html);
    // use handlebar.js to render animals-template to animals div
    var animals_html = animals_template(specific_content);
    $('#animals').html(animals_html);
  });

  // use handlebar.js to render show-all-template to category div
  $("a.show_all").click(function(){
    var show_all_source = $("#show-all-template").html();
    var show_all_template = Handlebars.compile(show_all_source);
    var all_data_html = show_all_template(animals_data);
    $('#category').html(all_data_html);
    $('#animals').empty();
  });
});


