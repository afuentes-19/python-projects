def caesar(direction, text, shift):
    finalString = ""
    if direction == "encode":
        for letter in text:
            if letter not in alphabet:
                finalString += " "
                continue 
            elif alphabet.index(letter) + shift > 25:
                newIndex = (alphabet.index(letter) + shift) % 26
            else:
                newIndex = alphabet.index(letter) + shift
            finalString += alphabet[newIndex]
    elif direction == "decode":
        for letter in text: 
            if letter not in alphabet: 
                finalString += " "
                continue 
            elif alphabet.index(letter) - shift < 0:
                newIndex = (len(alphabet) + alphabet.index(letter)) - shift 
            else: 
                newIndex = alphabet.index(letter) - shift
            finalString += alphabet[newIndex]
    print(f"The {direction}d text is {finalString}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

toContinue = True 

while toContinue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message: \n").lower()
    shift = int(input("Type your shift number:\n"))
    caesar(direction, text, shift)
    # if direction == "encode": 
    #     encrypt(text,shift)
    # elif direction == "decode": 
    #     decrypt(text,shift) 

    answer = input("Would you like to encode or decode or another string? Enter 'yes' or 'no'\n")
    answer = answer.lower()
    if answer == 'yes':
        toContinue = True
    else: 
        toContinue = False

