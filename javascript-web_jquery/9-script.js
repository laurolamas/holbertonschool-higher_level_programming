#!/usr/bin/node

$(document).ready(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});
