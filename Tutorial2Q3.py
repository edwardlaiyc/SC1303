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

user_input = str(input("Enter a string: ")).upper()
converted_string = ""
list_of_words = user_input.split()

for word in list_of_words:
    if word in morse_code.values():
        for key, value in morse_code.items():
            if value == word:
                converted_string += key
                converted_string += " "
    else:
        for char in word:
            converted_string += morse_code.get(char, char)
            converted_string += " "
print(converted_string)