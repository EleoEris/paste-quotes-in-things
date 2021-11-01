# paste-quotes-in-things
You can use this program to paste things in your multiplayer videogames with chat.
## REQUIREMENTS:
- Python 3.7 or higher
- keyboard (python -m pip install keyboard)
- python file with quotes in an array (might change it later)

## OPTIONS:
- paste_func  - function that takes a quote and does stuff with it, it will be run in determined time intervals.
- quote_delay - delay between pasted quotes
- delta       - it will add a random integer (between delta and -delta) to quote_delay for videogames that might ban timed messages
- startup     - how much time passes before the first quote is pasted

## QUOTES DICTIONARY:
It has to be a python array with quotes. You might create an iterable with quotes, as long as it has __len__ and a __getitem__ that returns a string.
