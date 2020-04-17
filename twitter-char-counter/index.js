const maxLength = 280;

var el;
var checked = false;

el = document.getElementById('tweet');
el.addEventListener('keyup', countCharacters, false);

function countCharacters(e) {
  var textEntered, countRemaining, counter;
  textEntered = document.getElementById('tweet').value;
  counter = (maxLength - (textEntered.length));
  checkChar(counter);
  countRemaining = document.getElementById('charactersRemaining');
  countRemaining.textContent = counter;
}

function checkChar(number){
  if(number < 0 && checked === false){
    document.getElementById('tweet').className += 'grey';
    document.getElementById('charactersRemaining').className += 'red';
    checked = true;
  }
  else if(number >= 0){
    checked = false;
    document.getElementById('tweet').className = '';
    document.getElementById('charactersRemaining').className = '';
  }
};
