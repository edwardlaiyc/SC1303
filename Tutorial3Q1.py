def encrypter(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr((ord('z') - ord(char)+ ord('a')))
    return encrypted_text