// a helper function that instantiates a template and displays the results in the content div
function showTemplate(template, dest_id, data){
  var html = template(data);
  $(dest_id).html(html);
}

$(document).ready(function(){
  // use handlebar.js to render nav-template to id="nav"
  var nav_source = $("#nav-template").html();
  var nav_template = Handlebars.compile(nav_source);
  showTemplate(nav_template, "#nav", animals_data);

  // use handlebar.js to render default-template to id="content"
  var default_source = $("#default-template").html();
  var default_template = Handlebars.compile(default_source);
  showTemplate(default_template, "#content", animals_data);

  // use handlebar.js template to render category-template to id="content" when clicking crop-img of category
  $(".category-thumbnail").click(function(){
    // compile category-template
    var category_source = $("#category-template").html();
    var category_template = Handlebars.compile(category_source);

    var category_index = $(this).data("id");
    var specific_category = animals_data.category[category_index];

    // use handlebar.js to render category-template to id="content"
    showTemplate(category_template, "#content", specific_category);

    $(".animals-thumbnail").click(function(){
      // compile category-title-template
      var category_title_source = $("#category-title-template").html();
      var category_title_template = Handlebars.compile(category_title_source);

      // compile animals-template
      var animals_source = $("#animals-template").html();
      var animals_template = Handlebars.compile(animals_source);

      var animals_index = $(this).data("id");
      var specific_content = animals_data.category[category_index].animals[animals_index];

      // use handlebar.js to render category-template to category div
      showTemplate(category_title_template, "#category-title", specific_category);

      // use handlebar.js to render animals-template to animals div
      showTemplate(animals_template, "#content", specific_content);
    });

  });

  // use handlebar.js template to render category-title-template and animals-template
  // to id="content" when clicking buttons in the navbar
  $("li.nav_animal_btn").click(function(){
    // compile category-title-template
    var category_title_source = $("#category-title-template").html();
    var category_title_template = Handlebars.compile(category_title_source);

    // compile animals-template
    var animals_source = $("#animals-template").html();
    var animals_template = Handlebars.compile(animals_source);

    var category_index = this.id.split("-")[0];
    var animals_index = this.id.split("-")[1];
    var specific_category = animals_data.category[category_index];
    var specific_content = animals_data.category[category_index].animals[animals_index];

    // use handlebar.js to render category-title-template to id="category-title"
    showTemplate(category_title_template, "#category-title", specific_category);

    // use handlebar.js to render animals-template to id="content"
    showTemplate(animals_template, "#content", specific_content);
  });

  // use handlebar.js to render show-all-template to id="content"
  $("a.show_all").click(function(){
    var show_all_source = $("#show-all-template").html();
    var show_all_template = Handlebars.compile(show_all_source);
    var all_data_html = show_all_template(animals_data);
    showTemplate(show_all_template, "#content", animals_data);
    $("#category-title").empty();
  });

});


