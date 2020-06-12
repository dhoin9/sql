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
        self.root.geometry("250x55")
        self.check = tki.Button(self.root, text="znajdź ucznia", command=self.czytajdane)
        self.check.grid(row=0, column=2)
        self.insert = tki.Button(self.root, text="wprowadź dane", command=self.insert)
        self.insert.grid(row=0, column=0)
        self.lub = tki.Label(text="lub")
        self.lub.grid(row=0, column=1)
        self.kasuj = tki.Button(self.root, text="Kasuj ucznia", command=self.kasowanie)
        self.kasuj.grid(row=1, column=0)

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
        self.ins.destroy()

    def czytajdane(self):

        self.find = tki.Tk()
        self.find.title('Szukaj ucznia')
        self.find.geometry("275x150")

        self.fimie = tki.Entry(self.find, width=10)
        self.fimie.insert(tki.END, "Adam")
        self.fimie.grid(row=0, column=2)
        self.fnazwisko = tki.Entry(self.find, width=10)
        self.fnazwisko.insert(tki.END, "Rudy")
        self.fnazwisko.grid(row=1, column=2)
        #self.fklasa = tki.Entry(self.find, width=10)
        #self.fklasa.insert(tki.END, int("1"))
        #self.fklasa.grid(row=2, column=2)
        self.nim = tki.Label(self.find, text="Imię:")
        self.nim.grid(row=0, column=0)
        self.nnaz = tki.Label(self.find, text="Nazwisko:").grid(row=1, column=0)
        self.nkl = tki.Label(self.find, text="Klasa:").grid(row=2, column=0)
        self.szukaj = tki.Button(self.find, width=10, text="szukaj", command=self.pokaz).grid(row=3, column=0, sticky="nsew", pady=2)


    def pokaz(self):

        """Funkcja pobiera i wyświetla dane z bazy."""
        cur.execute(
            """
            SELECT uczniowie.ID,imie,nazwisko,nazwa,profil  FROM uczniowie,klasa WHERE uczniowie.klasa=klasa.ID
            """)
        uczniowie = cur.fetchall()
        for uczen in uczniowie:
         while len(uczen) == 0:
            if uczen['nazwisko'] == str(self.fnazwisko.get()) and uczen['imie'] == str(self.fimie.get()):
                print(uczen)
                self.wuczen = tki.Tk()
                self.wuczen.geometry("200x120")
                self.iduczen = tki.Label(self.wuczen, text=('Uczeń ID: %s'%uczen['ID']))
                self.iduczen.grid(row=1, column=0)
                self.iuczen = tki.Label(self.wuczen, text=('Nazwisko: %s'%uczen['imie']))
                self.iuczen.grid(row=2, column=0)
                self.nuczen = tki.Label(self.wuczen, text=uczen['nazwisko'])
                self.nuczen.grid(row=3, column=0)
                self.kuczen = tki.Label(self.wuczen, text=uczen['nazwa'])
                self.kuczen.grid(row=4, column=0)
                print(uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
                uczenid = uczen['ID']

                              #kasowanie ucznia
                self.kasuj=tki.Button(self.wuczen, text='Kasuj', command=self.kasowanie)
                self.kasuj.grid(row=5, column=0)

                s= s+1
                print(s)
            else:
                print(s)


            if s==0:
                messagebox.showwarning("Uwaga", "Nie ma takiego ucznia")

        #self.find.destroy()


# def kasuj_ucznia:
#kasowanie ucznia
    def kasowanie(self):
        self.kas = tki.Tk()
        self.kas.title('Kasuj ucznia')
        self.kas.geometry("275x90")
        self.nid = tki.Label(self.kas, text="ID:")
        self.nid.grid(row=0, column=0)
        self.nid1 = tki.Entry(self.kas, width=5)
        self.nid1.grid(row=0, column=2)
        self.ok = tki.Button(self.kas, text="usuń", command=self.usun)
        self.ok.grid(row=3, column=0)
        self.nim = tki.Label(self.kas, text="Imię:")
        self.nim.grid(row=4, column=0)
        self.nnaz = tki.Label(self.kas, text="Nazwisko:").grid(row=1, column=0)
        self.nkl = tki.Label(self.kas, text="Klasa:").grid(row=2, column=0)

    def usun(self):
        sql = "DELETE FROM uczniowie  WHERE uczniowie.ID = %s "
        adr = int(self.nid1.get())
        cur.execute("SELECT uczniowie.ID,imie,nazwisko FROM uczniowie  WHERE uczniowie.ID =%s ", adr)
        es = cur.fetchall()
        #con.commit()
        print(len(es))
        if len(es) > 0:
            for es in es:
                print(es['ID'])
                print("adr: %s"%adr)
                cur.execute(sql, adr)
                con.commit()
        else:
            print("dupa2")



app = apka()

app.root.mainloop()
