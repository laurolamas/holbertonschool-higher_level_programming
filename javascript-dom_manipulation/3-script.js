const header = document.querySelector('header');
const button = document.getElementById('toggle_header');
button.onclick = () => {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
};
