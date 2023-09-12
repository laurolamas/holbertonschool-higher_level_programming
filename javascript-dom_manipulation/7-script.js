/**
Write a JavaScript script that fetches and lists the title for all movies by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json

    All movie titles must be list in the HTML ul element with id list_movies
    You must use the Fetch API.
*/

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the response body as JSON
  })
  .then((data) => {
    // Work with the JSON data
    const resultsArray = data.results;
    const titles = resultsArray.map((movie) => movie.title);
    const list = document.getElementById('list_movies');
    for (const title of titles) {
      const listItem = document.createElement('li');
      listItem.innerHTML = title;
      list.appendChild(listItem);
    }
  })
  .catch((error) => {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
