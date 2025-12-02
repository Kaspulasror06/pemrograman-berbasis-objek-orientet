import tkinter as tk

def klik(tombol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + tombol)

def hitung():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)


def key_event(event):
    char = event.char

    if char in "0123456789+-*/.":
        klik(char)

    if event.keysym == "Return":
        hitung()

    if event.keysym == "BackSpace":
        hapus_satu()

    if event.keysym == "Escape":
        clear()

root = tk.Tk()
root.title("Kalkulator By Kaspul")
root.bind("<Key>", key_event)

entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 18),
    borderwidth=5,
    relief="ridge",
    justify="right"
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tombol_list = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (teks, baris, kolom) in tombol_list:
    if teks == "=":
        tombol = tk.Button(
            root,
            text=teks,
            width=5,
            height=2,
            font=("Arial", 14),
            command=hitung,
            bg="#03B3FF",
            fg="#000000"
        )
    else:
        tombol = tk.Button(
            root,
            text=teks,
            width=5,
            height=2,
            font=("Arial", 14),
            command=lambda t=teks: klik(t)
        )

    tombol.grid(row=baris, column=kolom, padx=5, pady=5)

tombol_clear = tk.Button(
    root,
    text="Clear",
    width=22,
    height=2,
    font=("Arial", 14),
    command=clear,
    bg="#FD0303",
    fg="#000000"
)

tombol_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()