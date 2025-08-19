#create morse code dictionary
morse_code = {}
morse_code["A"] = ".-"
morse_code["B"] = "-..."
morse_code["C"] = "-.-."
morse_code["D"] = "-.."
morse_code["E"] = "."
morse_code["F"] = "..-."
morse_code["G"] = "--."
morse_code["H"] = "...."
morse_code["I"] = ".."
morse_code["J"] = ".---"
morse_code["K"] = "-.-"
morse_code["L"] = ".-.."
morse_code["M"] = "--"
morse_code["N"] = "-."
morse_code["O"] = "---"
morse_code["P"] = ".--."
morse_code["Q"] = "--.-"
morse_code["R"] = ".-."
morse_code["S"] = "..."
morse_code["T"] = "-"
morse_code["U"] = "..-"
morse_code["V"] = "...-"
morse_code["W"] = ".--"
morse_code["X"] = "-..-"
morse_code["Y"] = "-.--"
morse_code["Z"] = "--.."
morse_code["0"] = "-----"
morse_code["1"] = ".----"
morse_code["2"] = "..---"
morse_code["3"] = "...--"
morse_code["4"] = "....-"
morse_code["5"] = "....."
morse_code["6"] = "-...."
morse_code["7"] = "--..."
morse_code["8"] = "---.."
morse_code["9"] = "----."

#convert string to uppercase
user_input = str(input("Enter a string: ")).upper()
#create empty string to store converted output
converted_string = ""
#user_input split into each word, separated by space, store in a list
list_of_words = user_input.split()

#iterate through each word
for word in list_of_words:
    #is the word a morse value (i.e. dots and dashes)?
    if word in morse_code.values():
        #find the corresponding alphabet/digit
        for key, value in morse_code.items():
            if value == word:
                #add the alphabet/digit to the output string, plus a space between words
                converted_string += key
                converted_string += " "
    #the word is not a morse value
    else:
        #analyse by character
        for char in word:
            ##is the character an alphabet/digit?
            if char in morse_code:
                #add the corresponding morse value to the output, plus a space
                converted_string += morse_code.get(char)
                converted_string += " "
            #character is a special symbol, keep it as is
            else:
                converted_string += char
                converted_string += " "
print(converted_string)