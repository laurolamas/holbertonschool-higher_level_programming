#!/usr/bin/node

const list = $('#list_movies');

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach((movie) => {
    list.append(`<li>${movie.title}</li>`);
  });
});
