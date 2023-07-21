from random import sample;

def keysgenerator(keysize):

    words = 'abcdefghijklmnopqrstuvwxyz'

    wordsUpper = words.upper()

    numeros = "0123456789"

    simbolos = "[]()*;/,_-"

    steps = words + numeros + wordsUpper + simbolos

    generator = sample(steps,keysize)

    result = "".join(generator)

    return result

# Range = number of times to generated keys

for x in range(5):
    key = keysgenerator(15)
    print("Your password generated is: ", key)