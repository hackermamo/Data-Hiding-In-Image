import cv2
import os
import numpy as np

def encrypt_message(img_path):
    
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    # Combine password and message for authentication
    full_msg = password + '|' + msg + '|END'  # Delimiter '|END' marks message end
    binary_msg = ''.join(format(ord(i), '08b') for i in full_msg)
    
    data_index = 0
    total_bits = len(binary_msg)
    
    for row in img:
        for pixel in row:
            for channel in range(3):
                if data_index < total_bits:
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_msg[data_index])
                    data_index += 1
                else:
                    break

    # Generate a custom filename based on the message length & passcode
    encrypted_filename = f"encrypted_{len(msg)}_{len(password)}.png"
    
    cv2.imwrite(encrypted_filename, img)
    print(f"Message encrypted successfully! Saved as {encrypted_filename}")
    os.system(f"start {encrypted_filename}")  # Automatically open the image
    
    # Save the file name for automatic decryption
    with open("last_encrypted.txt", "w") as f:
        f.write(encrypted_filename)

def decrypt_message():
    
    try:
        with open("last_encrypted.txt", "r") as f:
            encrypted_img = f.read().strip()
    except FileNotFoundError:
        print("No encrypted file found! Please encrypt a message first.")
        return
    
    img = cv2.imread(encrypted_img)
    if img is None:
        print(f"Error: Image not found at {encrypted_img}")
        return
    
    binary_msg = ""
    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_msg += str(pixel[channel] & 1)

    binary_chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''.join(chr(int(char, 2)) for char in binary_chars if int(char, 2)) 

    if '|END' in message:
        message = message.split('|END')[0]
    
    if '|' in message:
        password, secret_msg = message.split('|', 1)
    else:
        print("Error: No valid message found!")
        return

    entered_pass = input("Enter passcode for Decryption: ")

    if password.strip()[:len(entered_pass)] != entered_pass.strip():
        print("YOU ARE NOT AUTHORIZED")
        return

    print("Decryption message:", secret_msg)
    with open("decrypted_message.txt", "w", encoding="utf-8") as file:
        file.write(secret_msg)
    print("Decrypted message saved in 'decrypted_message.txt'")

def main():
    
    img_path = r"C:\\Desktop\\New folder\\DAA practical\\Stenography-main\\mypic.jpg"  # Input image
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    
    if choice == 'e':
        encrypt_message(img_path)
    elif choice == 'd':
        decrypt_message()
    else:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
