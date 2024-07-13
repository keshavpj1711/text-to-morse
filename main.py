# Morse dict 
morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '/',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }


def to_morse(text):
  morse_code = ""
  for letter in text:
    morse_code += f"{morse_dict[letter.upper()]} "

  return morse_code


if __name__ == "__main__":
  user_input = input("Enter to convert: \n")
  morse_output = to_morse(user_input)
  print(f"Output Morse Code: \n{morse_output}")