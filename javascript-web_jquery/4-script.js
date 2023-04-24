#!/usr/bin/node

const element = $('header');
$('#toggle_header').on('click', event => {
  element.toggleClass('green red');
});
