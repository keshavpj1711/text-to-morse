# Str of Morse Code

## Dots and Dashes 

- **a dot(.)** represents a short signal
- **a dash(-)** represent a long signal

## Info about Timing

- The duration of a dot is the basic unit of time.
- A dash is three times the duration of a dot.
- The space between symbols (dots and dashes) of the same letter is equal to the duration of one dot.
- The space between letters is equal to the duration of three dots.
- The space between words is equal to the duration of seven dots.

## Dictionary of morse code used

```python
morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.', 
  'D': '-..',    'E': '.',      'F': '..-.',
  'G': '--.',    'H': '....',   'I': '..',
  'J': '.---',   'K': '-.-',    'L': '.-..',
  'M': '--',     'N': '-.',     'O': '---',
  'P': '.--.',   'Q': '--.-',   'R': '.-.',
  'S': '...',    'T': '-',      'U': '..-',
  'V': '...-',   'W': '.--',    'X': '-..-',
  'Y': '-.--',   'Z': '--..',
  '0': '-----',  '1': '.----',  '2': '..---',
  '3': '...--',  '4': '....-',  '5': '.....',
  '6': '-....',  '7': '--...',  '8': '---..',
  '9': '----.' 
  }
```

## Just a simple project

How i approached it was pretty simple and the dictionary present explains everything on it's own.