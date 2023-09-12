/**
 * Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:
The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list
 */

const list = document.querySelector('.my_list');
const button = document.getElementById('add_item');
button.onclick = () => {
  const listItem = document.createElement('li');
  listItem.innerHTML = 'Item';
  list.appendChild(listItem);
};
