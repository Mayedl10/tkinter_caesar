import string
import os
import random
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Encryption")
root.resizable(False,False)


alist = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
def caesar(text, shift, alphabets):
    

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


def encrypt_current():
    string = str(input_str.get())
    try:
        key = int(input_key.get())
    except:
        output_out.delete(0,8192)
        output_out.insert(0,"Key must be a number")
    out = caesar(string,key,alist)
    output_out.delete(0,8192)
    output_out.insert(0,out)

def randkey():
    key = int(random.randint(1,26))
    input_key.delete(0,8192)
    input_key.insert(0,key)


def decrypt_current():
    string = str(input_str.get())
    try:
        key = int(input_key.get())
    except:
        output_out.delete(0,8192)
        output_out.insert(0,"Key must be a number")
    key = key*-1
    out = caesar(string,key,alist)
    output_out.delete(0,8192)
    output_out.insert(0,out)





str_label = Label(text="Input")
key_label = Label(text="Key")
out_label = Label(text="Output")

input_str = Entry(root, width = 62, bg="lightgray")
input_str.place(x=10, y=30)
input_str.focus()

str_label.place(x=10,y=7)

input_key = Entry(root,width=62,bg="lightgray")
input_key.place(x=10,y=70)

key_label.place(x=10,y=50)

output_out = Entry(root,width=62,bg="lightgray")
output_out.place(x=10,y=170)

out_label.place(x=10,y=150)

encrypt_b = Button(text="Encrypt with current key",bg="lightgray",command=encrypt_current)
encrypt_b.place(x=9,y=100)

decrypt_b = Button(text="Decrypt with current key",bg="lightgray",command=decrypt_current)
decrypt_b.place(x=149,y=100)

randkey_b = Button(text="Get random key",bg="lightgray",command=randkey)
randkey_b.place(x=290,y=100)


input_str.delete(0,8192)
input_key.delete(0,8192)
output_out.delete(0,8192)



root.mainloop()
