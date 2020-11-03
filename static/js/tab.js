$(document).ready(function(){
    $(".theme-btn").on("click", function() {
var primaryColor = $(this).css("--primary-color");
var secondaryColor = $(this).css("--secondary-color");
var tertiaryColor = $(this).css("--tertiary-color");
var hamburgerColor = $(this).css("--hamburger-color");
var primaryforeColor = $(this).css("--primary-forecolor");
var secondaryforeColor = $(this).css("--secondary-forecolor");
var sidebarColor = $(this).css("--sidebar-forecolor");

$(document.body).css("--primary-color", primaryColor);
$(document.body).css("--secondary-color", secondaryColor);
$(document.body).css("--tertiary-color", tertiaryColor);
$(document.body).css("--hamburger-color", hamburgerColor);
$(document.body).css("--primary-forecolor", primaryforeColor);
$(document.body).css("--secondary-forecolor", secondaryforeColor);
$(document.body).css("--sidebar-forecolor", sidebarColor);
});
}); 