$(document).ready(function(){
  // display tertiary nav on hover, not click
  var hoverTime = 350; // ms
  var hoverInterval;
  
  $('.dropdown .dropdown .dropdown-toggle').hover(function(){
    clearInterval(hoverInterval);
    $('.dropdown .dropdown .dropdown-menu').hide();
    $(this).next(".dropdown-menu").show();
  });
  
  $('.dropdown .dropdown .dropdown-menu').hover(function(){
    clearInterval(hoverInterval);
  });
  
  $('.dropdown .dropdown a.dropdown-toggle').mouseleave(function(){
    var $element = $(this).next(".dropdown-menu");
    hoverInterval = setTimeout(hideElement,hoverTime,$element);
  });
  
  $('.dropdown .dropdown .dropdown-menu').mouseleave(function(){
    var $element = $(this);
    hoverInterval = setTimeout(hideElement,hoverTime,$element);
  });
  
  function hideElement($element){
    if($(window).width() > 767){
      $element.hide();
    }
  }
});
