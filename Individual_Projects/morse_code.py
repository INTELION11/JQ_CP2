# JQ 2nd Morse code    
  
# make a list of the letters and numbers    
letters = (    
    'a','b','c','d','e','f','g','h','i','j','k','l','m',    
    'n','o','p','q','r','s','t','u','v','w','x','y','z',    
    '0','1','2','3','4','5','6','7','8','9'    
)    
# make a list of the morse code that matches with the letters    
morse = (    
    '.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-',    
    '.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-',    
    '.--','-..-','-.--','--..',    
    '-----','.----','..---','...--','....-','.....','-....','--...','---..','----.'    
)    
    
# make a dictionary to turn a letter into morse code    
eng_to_morse = {letters[i]: morse[i] for i in range(len(letters))}    
# make a dictionary to turn morse code into a letter    
morse_to_eng = {morse[i]: letters[i] for i in range(len(morse))}    
    
# turn english into morse code    
def english_to_morse(text):    
    result = []    
    for char in text:    
        # if there is a space, use /  
        if char == ' ':    
            result.append('/')  # Use / for word space    
        # if the letter is in the dictionary, use the morse code    
        elif char in eng_to_morse:    
            result.append(eng_to_morse[char])    
        # if the letter is not in the dictionary, use a ?    
        else:    
            result.append('?')  # For unknown characters    
    # join everything together with spaces between codes    
    return ' '.join(result)    
    
# turn morse code into english    
def morse_to_english(message):    
    # split up the words by looking for /  
    words = message.strip().split(' / ')    
    result = []    
    for word in words:    
        # split up letters in each word  
        letters = word.split()    
        out = ''    
        for l in letters:    
            # if the code matches, use the letter    
            if l in morse_to_eng:    
                out += morse_to_eng[l]    
            # if not, use a ?    
            else:    
                out += '?'    
        result.append(out)    
    # join all the words together with spaces  
    return ' '.join(result)    
    
# keep asking the user what they want to do    
while True:    
    choice = input("1. Morse to English \n2. English to Morse \n3. Exit").strip()    
    if choice == "1":    
        # ask for morse code and turn it into english    
        message = input("what do you want to translate\n").strip()     
        print(f"{morse_to_english(message.lower())}")    
    elif choice == "2":    
        # ask for english and turn it into morse code    
        text = input("What is the message you need translated:\n").strip().lower()    
        print(f"{english_to_morse(text)}")    
    elif choice == "3":    
        # end the program    
        break    
    else:    
        # wrong input, try again    
        print("try again")    
