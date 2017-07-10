/**
 * Created by entick on 07.07.2017.
 */
$(document).ready(function() {
  $('li.active').removeClass('active');
  loc = location.pathname;
  $('a[href="' + loc.substr(0,loc.substr(1).indexOf('/')+2) + '"]').closest('li').addClass('active');
});