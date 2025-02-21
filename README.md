Steganography Message Encryption and Decryption:-

==>> This project demonstrates how to hide a secret message inside an image using the concept of steganography, with an added layer of security using password-based encryption. The program allows users to encrypt and decrypt messages using images and a passcode, making the process of message hiding both simple and secure.

 Features:- 
 
1. Message Encryption: A secret message is embedded in the least significant bits of an image file, making the changes visually imperceptible.

2. Password Protection: Users provide a passcode to encrypt and decrypt the message, ensuring that only authorized users can access the hidden information.

3. Message Decryption: The embedded message can be retrieved and decrypted by inputting the correct passcode.
   
4. Automatic File Handling: Encrypted images are automatically saved and decrypted messages are stored in a text file.



Requirements:- 
1. Python 3.x

2. OpenCV (cv2 library) for image processing

3. NumPy for array manipulation

4. Operating system: Compatible with Windows (due to file opening via os.system())

 Install the libraries:-
 
 	pip install opencv-python numpy


How to use Step by Step details:- 

   Steps:
 
Encrypting a Message:----

1. When you run the script, it will ask if you want to encrypt or decrypt.

2. Choose encryption (E), then provide the image, secret message, and passcode.

3. The encrypted image will be saved with a custom filename indicating message length and passcode length.

 
Decrypting a Message:----

1. Choose decryption (D) and provide the passcode used during encryption.

2. If the passcode is correct, the hidden message will be displayed and saved in a decrypted_message.txt file.

