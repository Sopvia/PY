import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import random
import string
import secrets
import re

root = Tk()
root.title('Passwort Generator')
root.geometry("600x600+700+200")

img = PhotoImage(file='icon.png')
root.wm_iconphoto(False, img)

master = tkinter.Frame(root)
master.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

results = tkinter.Frame(root)
results.grid(row=9, column=0, sticky="nsew", padx=85, pady=20)


def toggle(name):
    if name == 'uppercase':
        if uppercaseVar.get():
            uppercase_entry.grid(row=2, column=2, sticky="ew")
            checked_buttons.append('uppercase')
        else:
            uppercase_entry.grid_forget()
            checked_buttons.remove('uppercase')
    elif name == 'lowercase':
        if lowercaseVar.get():
            lowercase_entry.grid(row=3, column=2, sticky="ew")
            checked_buttons.append('lowercase')
        else:
            lowercase_entry.grid_forget()
            checked_buttons.remove('lowercase')
    elif name == 'digits':
        if digitsVar.get():
            digits_entry.grid(row=4, column=2, sticky="ew")
            checked_buttons.append('digits')
        else:
            digits_entry.grid_forget()
            checked_buttons.remove('digits')
    elif name == 'symbols':
        if symbolsVar.get():
            symbols_entry.grid(row=5, column=2, sticky="ew")
            checked_buttons.append('symbols')
        else:
            symbols_entry.grid_forget()
            checked_buttons.remove('symbols')


def check():
    length = scale.get()

    if checked_buttons.count("uppercase") == 1 and len(uppercase_entry.get()) >= 1:
        upper = int(uppercase_entry.get())
    else:
        upper = 0

    if checked_buttons.count("lowercase") == 1 and len(lowercase_entry.get()) >= 1:
        lower = int(lowercase_entry.get())
    else:
        lower = 0

    if checked_buttons.count("digits") == 1 and len(digits_entry.get()) >= 1:
        digit = int(digits_entry.get())
    else:
        digit = 0

    if checked_buttons.count("symbols") == 1 and len(symbols_entry.get()) >= 1:
        symbol = int(symbols_entry.get())
    else:
        symbol = 0

    entries = [upper, lower, digit, symbol]
    sum_entries = sum(entries)

    search_upper = re.search("[a-zA-Z]", uppercase_entry.get())
    search_lower = re.search("[a-zA-Z]", lowercase_entry.get())
    search_digits = re.search("[a-zA-Z]", uppercase_entry.get())
    search_symbols = re.search("[a-zA-Z]", uppercase_entry.get())

    if ((uppercaseVar.get() == 1 and len(uppercase_entry.get()) == 0)
            or (lowercaseVar.get() == 1 and len(lowercase_entry.get()) == 0)
            or (digitsVar.get() == 1 and len(digits_entry.get()) == 0)
            or (symbolsVar.get() == 1 and len(symbols_entry.get()) == 0)
            or len(amountPasswords.get()) == 0):
        messagebox.showerror('Error', 'Bitte alle Felder ausfüllen/Invalider Input!')
    elif len(checked_buttons) == 0:
        messagebox.showerror('Error', 'Es muss mindestens 1 Kästchen gesetzt sein!')
    elif search_upper is not None or search_lower is not None or search_digits is not None or search_symbols is not None:
        messagebox.showerror('Error', 'Invalider Input!')
    elif sum_entries > length:
        messagebox.showerror('Error', 'Länge passt nicht mit den angegebenen Mindestanzahlen überein! ')
    else:
        generate()


def copy(text):
    master.clipboard_clear()
    master.clipboard_append(text)


def generate():
    for widgets in results.winfo_children():
        widgets.destroy()

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    characters = ''
    if uppercaseVar.get():
        characters += uppercase
    if lowercaseVar.get():
        characters += lowercase
    if digitsVar.get():
        characters += digits
    if symbolsVar.get():
        characters += symbols

    length = int(scale.get())
    amount = int(amountPasswords.get())

    idx = 1
    r = 0
    for x in range(amount):
        chars = []
        if uppercaseVar.get() and len(uppercase_entry.get()) >= 1:
            for y in range(int(uppercase_entry.get())):
                uppercase_result = ''.join(random.choice(uppercase))
                chars.append(uppercase_result)
        if lowercaseVar.get() and len(lowercase_entry.get()) >= 1:
            for y in range(int(lowercase_entry.get())):
                lowercase_result = ''.join(random.choice(lowercase))
                chars.append(lowercase_result)
        if digitsVar.get() and len(digits_entry.get()) >= 1:
            for y in range(int(digits_entry.get())):
                digits_result = ''.join(random.choice(digits))
                chars.append(digits_result)
        if symbolsVar.get() and len(symbols_entry.get()) >= 1:
            for y in range(int(symbols_entry.get())):
                symbols_result = ''.join(random.choice(symbols))
                chars.append(symbols_result)

        if len(chars) == length:
            random.shuffle(chars)
            result = ''.join(chars)
        else:
            missing_chars = length - len(chars)
            for y in range(missing_chars):
                fill = ''.join(random.choice(characters))
                chars.append(fill)
            random.shuffle(chars)
            result = ''.join(chars)

        output = Button(results, text=result, font="Georgia",
            command=lambda button_text=result: copy(button_text), activebackground="lightpink",
            cursor="heart", height=1, width=22, padx=2, pady=2)
        output.grid(row=9 + r, column=idx)

        idx = idx + 1
        if idx % 2:
            r = r + 1
            idx = 1
   

Label(master, text="Länge des Passwortes:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=1, column=1)
Label(master, text="Mindestanzahl Großbuchstaben:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=4)
Label(master, text="Mindestanzahl Kleinbuchstaben:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=4)
Label(master, text="Mindestanzahl Zahlen:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=4, column=1, padx=4)
Label(master, text="Mindestanzahl Sonderzeichen:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=5,
                                                                                                               column=1,
                                                                                                               padx=4)
Label(master, text="Anzahl der Passwörter:", font="Georgia", relief=RIDGE, width=40, borderwidth=2).grid(row=6,
                                                                                                         column=1,
                                                                                                         padx=4)

scale = Scale(master, from_=0, to=20, font="Georgia", orient=HORIZONTAL, activebackground="lightpink", cursor="heart")

checked_buttons = []

uppercaseVar = BooleanVar()
checkUppercase = Checkbutton(master, variable=uppercaseVar, command=lambda: toggle("uppercase"), name="uppercase",
                             activebackground="lightpink", fg="lightpink", cursor="heart")
uppercase_entry = Entry(master)

lowercaseVar = BooleanVar()
checkLowercase = Checkbutton(master, variable=lowercaseVar, command=lambda: toggle("lowercase"), name="lowercase",
                             activebackground="lightpink", fg="lightpink", cursor="heart")
lowercase_entry = Entry(master)

digitsVar = BooleanVar()
checkDigits = Checkbutton(master, variable=digitsVar, command=lambda: toggle("digits"), name="digits",
                          activebackground="lightpink", fg="lightpink", cursor="heart")
digits_entry = Entry(master)

symbolsVar = BooleanVar()
checkSymbols = Checkbutton(master, variable=symbolsVar, command=lambda: toggle("symbols"), name="symbols",
                           activebackground="lightpink", fg="lightpink", cursor="heart")
symbols_entry = Entry(master)

amountPasswords = ttk.Combobox(master)
amountPasswords['values'] = ('1',
                             '2',
                             '3',
                             '4',
                             '5',
                             '6',
                             '7',
                             '8',
                             '9',
                             '10',
                             '11',
                             '12',
                             '13',
                             '14',
                             '15',
                             '16',
                             '17',
                             '18',
                             '19',
                             '20')
amountPasswords.current(0)

scale.grid(row=1, column=2, sticky="ew")

checkUppercase.grid(row=2, column=0)
checkLowercase.grid(row=3, column=0)
checkDigits.grid(row=4, column=0)
checkSymbols.grid(row=5, column=0)

amountPasswords.grid(row=6, column=2, sticky="ew")

button = Button(master, text="Generieren", font="Georgia", command=check, relief=RAISED, activebackground="lightpink",
                cursor="heart")
button.grid(row=8, column=2, pady=10)

master.mainloop()