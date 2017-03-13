import tkinter
from tkinter import *
import math, pyperclip, transpositionDecrypt, detectEnglish,cryptomath, sys


SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXTZ"
class Project_GUI(Frame):

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # Title label
        self.instruction = Label(self, text = "Encrypt/Decrypt", font=("arial",17,"bold"))
        self.instruction.grid(row = 1, column = 0, columnspan = 3, padx = 5, sticky = W)

        #type label
        self.type = Label(self, text = "Choose Type")
        self.type.grid(row = 2, column = 0, columnspan = 2, padx = 5, sticky = W)

        #type option
        self.var1 = IntVar()

        self.type = Radiobutton(self, text = "Caesar_Encrypt", pady = 5, variable = self.var1, value=0, command = self.caesar)
        self.type.grid(row = 3, column = 0, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Caesar_Decrypt", pady = 5, variable = self.var1, value=1, command = self.caesar)
        self.type.grid(row = 3, column = 1, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Transposition_Encrypt", pady = 5, variable = self.var1, value=2, command = self.Transposition_Encrypt)
        self.type.grid(row = 3, column = 2, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Transposition_Decrypt", pady = 5, variable = self.var1, value=3, command = self.Transposition_Decrypt)
        self.type.grid(row = 3, column = 3, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Affine_Encrypt", pady = 5, variable = self.var1, value=4, command = self.Affine_Encrypt)
        self.type.grid(row = 3, column = 4, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Affine_Decrypt", pady = 5, variable = self.var1, value=5, command = self.Affine_Decrypt)
        self.type.grid(row = 3, column = 5, columnspan = 1, padx = 5, sticky = W)

        self.type = Radiobutton(self, text = "Substitution_Encrypt", pady=5, variable = self.var1, value=6, command=self.Substitution_Encrypt)
        self.type.grid(row=4, column=0, columnspan=1, padx=5, sticky=W)

        self.type = Radiobutton(self, text = "Substitution_Decrypt", pady=5, variable = self.var1, value=7, command=self.Substitution_Decrypt)
        self.type.grid(row=4, column=1, columnspan=1, padx=5, sticky=W)

        self.type = Radiobutton(self, text = "Vigenere_Encrypt", pady=5, variable = self.var1, value=8, command=self.Vigenere_Encrypt)
        self.type.grid(row=4, column=2, columnspan=1, padx=5, sticky=W)

        self.type = Radiobutton(self, text = "Vigenere_Decrypt", pady=5, variable = self.var1, value=9, command=self.Vigenere_Decrypt)
        self.type.grid(row=4, column=3, columnspan=1, padx=5, sticky=W)

        self.type = Radiobutton(self, text = "RSA_Encrypt", pady=5, variable = self.var1, value=10, command=self.RSA_Encrypt)
        self.type.grid(row=4, column=4, columnspan=1, padx=5, sticky=W)

        self.type = Radiobutton(self, text = "RSA_Decrypt", pady=5, variable = self.var1, value=11, command=self.RSA_Decrypt)
        self.type.grid(row=4, column=5, columnspan=1, padx=5, sticky=W)



        # # Mode label
        # self.mode = Label(self, text = "Choose caesar mode")
        # self.mode.grid(row = 2, column = 6, columnspan = 2, padx = 5, sticky = W)
        #
        # # Mode options
        # self.var2 = IntVar()
        #
        # self.mode = Radiobutton(self, text="Encrypt", pady = 5, variable=self.var2, value=6, command = self.caesar)
        # self.mode.grid(row = 3, column = 6, columnspan = 1, padx = 5, sticky = E)
        #
        # self.mode = Radiobutton(self, text="Decrypt", pady = 5, variable=self.var2, value=7, command = self.caesar)
        # self.mode.grid(row = 3, column = 7, columnspan = 1, padx = 5, sticky = E)

        # Message label
        self.instruction = Label(self, text = "Enter message: ")
        self.instruction.grid(row = 6, column = 0, columnspan = 100, padx = 5, sticky = W)

        # Message entry
        self.message= Entry(self)
        self.message.grid(row = 7, column = 0, padx = 5, sticky = W)

        # Key label
        self.instruction = Label(self, text = "Enter key")
        self.instruction.grid(row = 8, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Key entry
        self.key= Entry(self)
        self.key.grid(row = 9, column = 0, padx = 5, sticky = W)

        # Submit
        self.submit_button = Button(self, text = "Submit", command = self.caesar)
        self.submit_button.grid(row = 10, column = 0, padx = 5, sticky = W)

        # Result label
        self.instruction = Label(self, text = "Result", font=("arial",14,"bold"))
        self.instruction.grid(row = 11, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Result
        self.result = Text(self, width = 80, height = 10, wrap = WORD)
        self.result.grid(row = 12, column = 0, columnspan = 3, padx = 5, sticky = W)

    def caesar(self):
        m = self.message.get()
        k = int(self.key.get())
        ciphertext = ''

        if self.var1.get()==0:
            k
        if self.var1.get()== 1:
            k = -k

        for symbol in m:
            if symbol.isalpha():
                num = ord(symbol) + k

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26

                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                ciphertext  += chr(num)
            else:
                ciphertext += symbol

        self.result.delete(0.0, END)
        self.result.insert(0.0, ciphertext)

        return ciphertext

    def Transposition_Encrypt(self):
        m = self.message.get()
        k = int(self.key.get())

        if self.var1.get() == 2:
            ciphertext = [''] * k

            for col in range(k):
                pointer = col
                while pointer < len(m):
                    ciphertext[col] += m[pointer]
                    pointer += k

        self.result.delete(0.0, END)
        self.result.insert(0.0, ciphertext)

        return ''.join(ciphertext)

    def Transposition_Decrypt(self):
        m = self.message.get()
        k = int(self.key.get())

        if self.var1.get()==3:
                numOfColumns = math.ceil(len(m) / k)
                numOfRows = k
                numOfShadedBoxes = (numOfColumns * numOfRows) - len(m)

                plaintext = [''] * numOfColumns

                col = 0
                row = 0

                for symbol in m:
                    plaintext[col] += symbol
                    col += 1

                    if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                        col = 0
                        row += 1

        self.result.delete(0.0, END)
        self.result.insert(0.0, plaintext)

        return ''.join(plaintext)

    # def Transposition_Hack(self):
    #     m = self.message.get()
    #
    #     if (self.var1.get())==4:
    #             for key in range(1, len(m)):
    #                 decryptedText = transpositionDecrypt.decryptMessage(key, m)
    #
    #                 if detectEnglish.isEnglish(decryptedText):
    #                     decryptedText[:100]
    #
    #     self.result.delete(0.0, END)
    #     self.result.insert(0.0, decryptedText)
    #
    #     return None

    # def getKeyParts(key):
    #     keyA = key // len(SYMBOLS) #몫
    #     keyB = key % len(SYMBOLS) #나머지
    #     return (keyA, keyB)

    def Affine_Encrypt(self):
        m = self.message.get()
        k = self.message.get()

        if self.var1.get() == 4:
            keyA = k // len(SYMBOLS) #몫
            keyB = k % len(SYMBOLS) #나머지

            ciphertext = ''
            for symbol in m:
                if symbol in SYMBOLS:
                    # encrypt this symbol
                    symIndex = SYMBOLS.find(symbol)
                    ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
                    # Keypoint
                else:
                    ciphertext += symbol # just append this symbol unencrypted
        self.result.delete(0.0, END)
        self.result.insert(0.0, ciphertext)

        return ciphertext


    def Affine_Decrypt(self):
        m = self.message.get()
        k = self.message.get()
        if self.var1.get() == 5:
            keyA = k // len(SYMBOLS) #몫
            keyB = k % len(SYMBOLS) #나머지

        plaintext = ''
        modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

        for symbol in m:
            if symbol in SYMBOLS:
                # decrypt this symbol
                symIndex = SYMBOLS.find(symbol)
                plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
            else:
                plaintext += symbol # just append this symbol undecrypted

        self.result.delete(0.0, END)
        self.result.insert(0.0, plaintext)

        return plaintext

   def Substitution_Encrypt(self):
        m = self.message.get()
        k = self.message.get()
        if self.var1.get() == 6:
            charsA = LETTERS
            charsB = k

            translated = ''
            for symbol in m:
                if symbol.upper() in charsA:
                    # encrypt/decrypt the symbol
                    symIndex = charsA.find(symbol.upper())
                    if symbol.isupper():
                        translated += charsB[symIndex].upper()
                    else:
                        translated += charsB[symIndex].lower()
                else:
                    # symbol is not in LETTERS, just add it
                    translated += symbol

        return translated

   def Substitution_Decrypt(self):
        m = self.message.get()
        k = self.message.get()
        if self.var1.get() == 7:
            charsA = k
            charsB = LETTERS


            translated = ''
            for symbol in m:
                if symbol.upper() in charsA:
                    # encrypt/decrypt the symbol
                    symIndex = charsA.find(symbol.upper())
                    if symbol.isupper():
                        translated += charsB[symIndex].upper()
                    else:
                        translated += charsB[symIndex].lower()
                else:
                    # symbol is not in LETTERS, just add it
                    translated += symbol

        return translated


    def Vigenere_Encrypt(self):
        m = self.message.get()
        k = self.message.get()
        if self.var1.get() == 8:
             translated = []

        keyIndex = 0
        k = k.upper()

        for symbol in m: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                num += LETTERS.find(k[keyIndex]) # add if encrypting
            num %= len(LETTERS) # handle the potential wrap-around
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(k):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

        return ''.join(translated)

    def Vigenere_Decrypt(self):
        m = self.message.get()
        k = self.message.get()
        if self.var1.get() == 9:
             translated = []

        keyIndex = 0
        k = k.upper()

        for symbol in m: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                num -= LETTERS.find(k[keyIndex]) # add if encrypting
            num %= len(LETTERS) # handle the potential wrap-around
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(k):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

        return ''.join(translated)



root = Tk()
root.title("Project_GUI")
root.geometry("1400x500")
view = Project_GUI(root)
root.mainloop()
