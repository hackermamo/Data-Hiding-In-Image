Steganography Message Encryption and Decryption:-

This project demonstrates how to hide a secret message inside an image using the concept of steganography, with an added layer of security using password-based encryption. The program allows users to encrypt and decrypt messages using images and a passcode, making the process of message hiding both simple and secure.

 Features:- 
 	Message Encryption: A secret message is embedded in the least significant bits of an image file, making the changes visually imperceptible.
	Password Protection: Users provide a passcode to encrypt and decrypt the message, ensuring that only authorized users can access the hidden information.
	Message Decryption: The embedded message can be retrieved and decrypted by inputting the correct passcode.
	Automatic File Handling: Encrypted images are automatically saved and decrypted messages are stored in a text file.


Requirements:- 
	Python 3.x
	OpenCV (cv2 library) for image processing
	NumPy for array manipulation
	Operating system: Compatible with Windows (due to file opening via os.system())

 Install the libraries:-
 
 	pip install opencv-python numpy


How to use Step by Step details:- 

   Steps:
 
Encrypting a Message:----

When you run the script, it will ask if you want to encrypt or decrypt.

Choose encryption (E), then provide the image, secret message, and passcode.

The encrypted image will be saved with a custom filename indicating message length and passcode length.

 
Decrypting a Message:----

Choose decryption (D) and provide the passcode used during encryption.

If the passcode is correct, the hidden message will be displayed and saved in a decrypted_message.txt file.

