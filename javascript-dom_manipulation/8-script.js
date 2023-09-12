/**
 * Write a JavaScript script that fetches from
 * https://hellosalut.stefanbohacek.dev/?lang=fr
 *  and displays the value of hello from that fetch in the HTML element with id hello.

    The translation of “hello” must be displayed in the HTML element with id hello
    Your script must work when it is imported from the <head> tag

 */

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the response body as JSON
  })
  .then((data) => {
    // Work with the JSON data
    const hello = document.getElementById('hello');
    hello.innerHTML = data.hello;
  })
  .catch((error) => {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
