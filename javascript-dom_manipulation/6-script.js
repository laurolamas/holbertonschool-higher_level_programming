/**
 * Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
    The name must be displayed in the HTML tag with id character.
    You must use the Fetch API.
    You probably should read something about usign Promises later.
 */

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the response body as JSON
  })
  .then((data) => {
    const character = document.getElementById('character');
    character.innerHTML = data.name;
  });
