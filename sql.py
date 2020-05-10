import pymysql as mysql  # ładowanie biblioteki
import tkinter as tki
from tkinter import messagebox

con = mysql.Connect(host='127.0.0.1', unix_socket='', user='root', passwd='', db='szkola')  # łączenie się z bazą danych

cur = con.cursor(
    mysql.cursors.DictCursor)  # tworzy obiekt, dzięki któremu będzie można wysyłać zapytania do bazy danych
cur.execute("USE szkola")  # wybranie istniejącej bazy danych
cur.execute("SHOW TABLES")  # zapytanie o tabele zawarte w wybranej wcześniej bazie danych




class apka():
    def __init__(self):
        self.root = tki.Tk()
        self.root.title('Który to uczeń')
        self.root.geometry("250x50")
        self.check = tki.Button(self.root, text="znajdź ucznia", command=self.czytajdane)
        self.check.grid(row=0, column=2)
        self.insert = tki.Button(self.root, text="wprowadź dane", command=self.insert)
        self.insert.grid(row=0, column=0)
        self.lub = tki.Label(text="lub")
        self.lub.grid(row=0, column=1)
        #self.kasuj = tki.Button(self.root, text="Kasuj ucznia", command=self.insert)
        #self.kasuj.grid(row=1, column=0)

    def insert(self):
        self.ins = tki.Tk()
        self.ins.title('Wprowadź dane')
        self.ins.geometry("275x90")
        self.nimie = tki.Entry(self.ins, width=10)
        self.nimie.insert(tki.END, "Adam")
        self.nimie.grid(row=0, column=2)
        self.nnazwisko = tki.Entry(self.ins, width=10)
        self.nnazwisko.insert(tki.END, "Rudy")
        self.nnazwisko.grid(row=1, column=2)
        self.nklasa = tki.Entry(self.ins, width=10)
        self.nklasa.insert(tki.END, int("1"))
        self.nklasa.grid(row=2, column=2)
        self.ok = tki.Button(self.ins, text="Dodaj", command=self.new_uczen)
        self.ok.grid(row=3, column=0)
        self.nim = tki.Label(self.ins, text="Imię:")
        self.nim.grid(row=0, column=0)
        self.nnaz = tki.Label(self.ins, text="Nazwisko:").grid(row=1, column=0)
        self.nkl = tki.Label(self.ins, text="Klasa:").grid(row=2, column=0)

    def new_uczen(self):
        print("nowy ciul")
        nowy = (None, self.nimie.get(), self.nnazwisko.get(), self.nklasa.get())
        cur.execute('INSERT INTO uczniowie VALUES(%s, %s, %s, %s)', nowy)
        con.commit()

        uczniowie = cur.fetchall()

        for uczen in uczniowie:
            print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
        self.ins.destroy()

    def czytajdane(self):

        self.find = tki.Tk()
        self.e = tki.Entry(self.find, width=10)
        self.e.grid(row=0, column=0)
        self.e.insert(tki.END, "3")
        self.szukaj = tki.Button(self.find, width=10, text="szukaj", command=self.pokaz).grid(row=1, column=0, sticky="nsew", pady=2)

    def pokaz(self):

        """Funkcja pobiera i wyświetla dane z bazy."""
        cur.execute(
            """
            SELECT uczniowie.ID,imie,nazwisko,nazwa,profil  FROM uczniowie,klasa WHERE uczniowie.klasa=klasa.ID
            """)
        uczniowie = cur.fetchall()
        for uczen in uczniowie:
            if uczen['ID'] == int(self.e.get()):
                messagebox.showinfo("uczeń", uczen['imie'])
                print(uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
            else:
                continue
        self.find.destroy()


# def kasuj_ucznia:


app = apka()

app.root.mainloop()
