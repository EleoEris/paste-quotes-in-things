# paste-quotes-in-things
You can use this program to paste things in your multiplayer videogames with chat.
## REQUIREMENTS:
- Python 3.7 or higher
- keyboard (python -m pip install keyboard)
- python file with quotes in an array

## OPTIONS:
<dl>
  <dt>paste_func</dt>
  <dd>function that takes a quote and does stuff with it, it will be run in determined time intervals.</dd>

  <dt>quote_delay</dt>
  <dd>delay between pasted quotes</dd>
  
  <dt>delta</dt>
  <dd>it will add a random integer (between delta and -delta) to quote_delay for videogames that might ban timed messages</dd>
  
  <dt>startup</dt>
  <dd>how much time passes before the first quote is pasted</dd>
  
  <dt>ineterrupt_key</dt>
  <dd>key that is pressed to quit the program</dd>
</dl>

## QUOTES ARRAY:
It has to be an iterable quotes in a file named _quotes.py_. You might create an iterable with quotes, as long as it has __\_\_len\_\___ and a __\_\_getitem\_\___ that returns a string.
