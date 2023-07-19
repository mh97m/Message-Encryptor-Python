import random
import string
import time
import argparse

nato_alphabet = {'a': '@@@@@##@#@', 'b': '@@@#@###@#', 'c': '#@@@@#@@##', 'd': '###@@@@#@@', 'e': '@#@@#@#@@@', 'f': '@@@@#@@@##', 'g': '@#@#@#@###', 'h': '####@##@#@', 'i': '######@@@@', 'j': '#@###@@@#@', 'k': '#@@###@@#@', 'l': '####@#####', 'm': '#@#####@#@', 'n': '#@@#@####@', 'o': '@##@###@@#', 'p': '##@#@####@', 'q': '@@####@@@@', 'r': '@@@@@@@@@#', 's': '##@#@@##@@', 't': '##@##@#@@@', 'u': '@#@@@#@@@@', 'v': '#@#@#@@###', 'w': '@####@@@@@', 'x': '@#@###@##@', 'y': '##@####@#@', 'z': '#@####@@##', 'A': '@###@##@#@', 'B': '#@##@@#@@#', 'C': '@##@@#@###', 'D': '##@#@#@##@', 'E': '@@@##@###@', 'F': '#@####@@@@', 'G': '#@##@#@#@#', 'H': '@@@@@###@@', 'I': '@##@@#####', 'J': '#######@#@', 'K': '@#@#@@@#@@', 'L': '@##@@##@@@', 'M': '@@@#@@@###', 'N': '##@#@@@#@#', 'O': '##@@@#@@##', 'P': '@@@#####@@', 'Q': '@#@@@#@#@@', 'R': '@@##@@@@#@', 'S': '@#@#@#@###', 'T': '#@@#@@@@#@', 'U': '@##@@@@##@', 'V': '@@@###@@@@', 'W': '@@@#@#@@#@', 'X': '@@@@###@##', 'Y': '@@#@#@@@@#', 'Z': '#@#@@@#@#@', '0': '@#@@#@@#@#', '1': '####@@#@@@', '2': '##@@@@#@#@', '3': '@@@#####@@', '4': '@##@##@#@#', '5': '###@#####@', '6': '#@@####@#@', '7': '#@#####@#@', '8': '###@##@#@@', '9': '@#@##@#@@#', '!': '@@@@@##@@@', '"': '#@#####@@#', '#': '@@@####@##', '$': '##@@@#####', '%': '@@##@##@@@', '&': '###@@@#@@@', "'": '###@#@@@##', '(': '@###@#@@#@', ')': '@#@@###@#@', '*': '@#####@@@@', '+': '@@#@@#####', ',': '@@###@@#@#', '-': '@@@@@@#@@@', '.': '@#@#@###@#', '/': '@####@@@@@', ':': '#@@@@###@@', ';': '##@######@', '<': '#@#####@@#', '=': '#@#@#@@###', '>': '####@#@###', '?': '#@########', '@': '@##@@#@@##', '[': '@##@@####@', '\\': '#@#@#@###@', ']': '@@@@@#@###', '^': '@@####@@#@', '_': '@@#####@#@', '`': '##@#@#####', '{': '##@###@@@@', '|': '@####@#@@@', '}': '@##@#@@@#@', '~': '@@@@@#@@#@', ' ': '@##@###@@@', '\t': '@@#@##@@##', '\n': '##@#@###@#', '\r': '@@@##@@#@#', '\x0b': '@#@@@@##@@', '\x0c': '@@@#@@@@@@'}

def encrypt_message(message, nato_alphabet=nato_alphabet):

   encrypted_message = ""

   # Iterate through each letter in the message
   for letter in message:

      # If the letter is in the dictionary, add the corresponding codeword to the encrypted message
      if letter in nato_alphabet:
         encrypted_message += nato_alphabet[letter]

      # If the letter is not in the dictionary, add the original letter to the encrypted message
      else:
         raise Exception("Letter not in dictionary")

   return encrypted_message

def decrypt_message(message, nato_alphabet=nato_alphabet):

   reversed_nato_alphabet = {value: key for key, value in nato_alphabet.items()}

   decrypt_message = ""

   if len(message)%10 != 0:
      raise Exception("Invalid message")

   for i in range(0, len(message), 10):

      character = message[i:i + 10]

      # If the letter is in the dictionary, add the corresponding codeword to the decrypt message
      if character in reversed_nato_alphabet:
         decrypt_message += reversed_nato_alphabet[character]

      # If the letter is not in the dictionary, add the original letter to the decrypt message
      else:
         raise Exception("Letter not in dictionary")

   return decrypt_message

if __name__ == '__main__':
   start = time.monotonic()
   parser = argparse.ArgumentParser(
            description='Encrypt or decrypt all files in a directory')
   parser.add_argument('--mode', choices=[
                        'encrypt', 'decrypt'], help='Mode to run the program in (encrypt or decrypt)')
   args = parser.parse_args()
   mode = args.mode
   message = input("Please enter message: ")
   if mode == 'encrypt':
      message = encrypt_message(message)
   elif mode == 'decrypt':
      message = decrypt_message(message)
   else:
         raise Exception('Invalid mode')
   end = time.monotonic()
   print(f"Operation completed in: {end-start} seconds \n #################### \n #################### \n #################### \n \n {message}")

quit()

############################################################
############### GENERATE NEW ALPHABET KEYS #################
############################################################
nato_alphabet={}
def generate_new_nato_alphabet(length=10, nato_alphabet=nato_alphabet):
   characters = "@#"  # Only "@" and "#"
   unique_string = ''.join(random.choice(characters) for _ in range(length))
   while unique_string in nato_alphabet.values():  # Check for uniqueness
      unique_string = ''.join(random.choice(characters) for _ in range(length))
   return unique_string

nato_alphabet = {letter: generate_new_nato_alphabet() for letter in string.ascii_letters + string.digits + string.punctuation + string.whitespace}
print(nato_alphabet)
