#!/usr/bin/node

const element = $('header');
$('#red_header').on('click', event => {
  element.css('color', 'red');
});
