#!/usr/bin/node

const header = $('header');
$('#update_header').on('click', event => {
  header.text('New Header!!!');
});
