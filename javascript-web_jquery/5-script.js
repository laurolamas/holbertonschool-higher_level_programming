#!/usr/bin/node

const list = $('.my_list');
$('#add_item').on('click', event => {
  list.append('<li>Item</li>');
});
