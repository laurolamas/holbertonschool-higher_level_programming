const header = document.querySelector('header');
const button = document.getElementById('red_header');
button.onclick = () => {
  header.classList.add('red');
};
