import sys

#dictionary of the international morse codes
codes={'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '1': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
def decode(msg):

    '''decode the message'''
#create an empty list to store the decoded message
    decoded_message = []
    inv_dict= {v: k for k,v in codes.items()} #invert the dictionary

    for letter, code in inv_dict.items():

        for block in msg: #for block of codes in the message
            letter=inv_dict[block]
            decoded_message.append(letter)
        break    

    return decoded_message #returns decoded message in a list

def encode(msg):
    """to encode the message to morse code

    :msg: the message from input
    :returns: encoded list

    """
    encoded_message = []
    for letter, code in codes.items():
        for element in msg:
            if element == " ":
                blank=" "
                encoded_message.append(blank)
            else:
                letter = codes[element]
            encoded_message.append(letter)
        break
    return encoded_message


if __name__ == '__main__':
    # get the file from agruments
    coded_file = open(sys.argv[1],'r').read().strip()
    if coded_file.startswith('.') or coded_file.startswith('-'):
        decoded = decode(coded_file.split())
        print(''.join(decoded))
    else:
        encoded = encode(list(coded_file))
        print(" ".join(encoded))


