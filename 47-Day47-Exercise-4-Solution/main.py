# Import random to generate random characters
import random
# Import string to get letters and number easily
import string

#--------------------------------------------------
# RANDOM CHARACTERS
#--------------------------------------------------
def generate_random_chars():
    # Crerate a collection containing letters and numbers
    characters = string.ascii_letters + string.digits
    
    # Randomly select 3 characters and join them into a string
    return ''.join(random.choices(characters, k=3))

#--------------------------------------------------
# ENCRYPT ONE WORD
#--------------------------------------------------
def encrypt_word(word):
    # if the word has 3 or more characters
    if len(word) >= 3:
        
        # Remove the first character and put in at the end
        new_word = word[1:] + word[0]
        
        # Generate 3 random characters for the beginning
        random_start = generate_random_chars()
        
        # Generate 3 random characters for the end
        random_end = generate_random_chars()
        
        # Add random characters to both sides
        return random_start + new_word + random_end
    
    # If the word has less than 3 characters,
    # Simply reverse the word
    else:
        return word[::-1]
    
#--------------------------------------------------
# DECRYPT ONE WORD
#--------------------------------------------------
def decrypt_word(word):
    # If the word has less than 3 characters,
    # Simply reverse the word
    if len(word) < 3:
        return word[::-1]
    
    # Remove the first 3 random characters
    # and the last 3 random characters
    new_word = word[3:-3]
    
    # Move the last character to the beginning
    new_word = new_word[-1] + new_word[:-1]
    
    # Return the original word
    return new_word

#--------------------------------------------------
# ENCRYPT COMPLETE MESSSAGE
#--------------------------------------------------
def encrypt_message(message):
    # SPlit the message into individual words
    words = message.split()
    
    # Store encrypted words here
    encrypted_words = []
    
    # Encrypt each word separately
    for word in words:
        encrypted_words.append(encrypt_word(word))
    
    # Join all encrypted words back into a sentence
    return " ".join(encrypted_words)

#--------------------------------------------------
# DECRYPT COMPLETE MESSSAGE
#--------------------------------------------------
def decrypt_message(message):
    # SPlit the message into individual words
    words = message.split()
    
    # Store encrypted words here
    decrypted_words = []
    
    # Encrypt each word separately
    for word in words:
        decrypted_words.append(decrypt_word(word))
    
    # Join all encrypted words back into a sentence
    return " ".join(decrypted_words)

#--------------------------------------------------
# MAIN PROGRAM
#--------------------------------------------------
def main():
    
    # Keep showing the menu until the user chooses 0
    while True:
        print("\n==============================")
        print("       SECRET CODE")
        print("==============================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Quit")
        print("==============================")
        
        # Ask the user what they want to do
        choice = input("Enter your choice: ")
        
        # Encrypt
        if choice == "1":
            # Get the noermal message
            message = input("Enter message: ")
            
            # Encrypt and display the message
            encrypted = encrypt_message(message)
            print("Encrypted: ", encrypted)
        
        # Decrypt
        elif choice == "2":
            # Get the encrypted message
            message = input("Enter encrypted message: ")
            
            # Decrypt and display the message
            decrypted = decrypt_message(message)
            print("Decrypted: ",decrypted)
        
        # Quit
        elif choice == "0":
            print("Goodbye!")
            break
        
        # Handle Invalid Choices
        else:
            print("Invalid Choice! Plear Enter 0,1 or 2")
        
# Start the Program
main()