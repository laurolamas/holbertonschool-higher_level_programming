/**
 * Write a JavaScript script that updates the text of the header element to New Header!!!
 *  when the user clicks on the element with id update_header
 */

const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

updateHeader.onclick = () => {
  header.innerHTML = 'New Header!!!';
};
