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
        self.root.title('Szkoła')
        self.root.geometry("250x55")
        self.check = tki.Button(self.root, text="Znajdź ucznia", command=self.czytajdane)
        self.check.grid(row=0, column=1)
        self.insert = tki.Button(self.root, text="Wprowadź dane", command=self.insert)
        self.insert.grid(row=0, column=0)
        #self.lub = tki.Label(text="lub")
        #self.lub.grid(row=0, column=1)
        self.kasuj = tki.Button(self.root, text="Kasuj ucznia", command=self.kasowanie)
        self.kasuj.grid(row=1, column=0)
        self.wszyscy = tki.Button(text="Pokaż wszystkich", command=tabele.all)
        self.wszyscy.grid(row=1, column=1)

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



            else:
                continue


            if s==0:
                messagebox.showwarning("Uwaga", "Nie ma takiego ucznia")

        #self.find.destroy()



    #kasowanie ucznia
    def kasowanie(self):
        self.kas = tki.Tk()
        self.kas.title('Kasuj ucznia')
        self.kas.geometry("275x111")
        self.nid = tki.Label(self.kas, text="ID:")
        self.nid.grid(row=0, column=0)
        self.nid1 = tki.Entry(self.kas, width=5)
        self.nid1.grid(row=0, column=1)
        self.kaso = tki.Button(self.kas, text="Usuń", command=self.usun)
        self.kaso.grid(row=4, column=0)
        self.ok = tki.Button(self.kas, text="Pokaż", command=self.poka)
        self.ok.grid(row=4, column=1)
        self.nim = tki.Label(self.kas, text="Imię:").grid(row=1, column=0)
        self.nnaz = tki.Label(self.kas, text="Nazwisko:").grid(row=2, column=0)
        self.nkl = tki.Label(self.kas, text="Klasa:").grid(row=3, column=0)

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

    def poka(self):

        """Funkcja pobiera i wyświetla dane z bazy."""
        cur.execute(
            """
            SELECT uczniowie.ID,imie,nazwisko,nazwa,profil  FROM uczniowie,klasa WHERE uczniowie.klasa=klasa.ID
            """)
        uczniowie = cur.fetchall()
        for uczen in uczniowie:

            if uczen['ID'] == int(self.nid1.get()):
                print(uczen)
                self.niml = tki.Label(self.kas, text="Imię:").grid(row=1, column=0)
                self.nnazl = tki.Label(self.kas, text="Nazwisko:").grid(row=2, column=0)
                self.nkll = tki.Label(self.kas, text="Klasa:").grid(row=3, column=0)


                self.kiuczen = tki.Label(self.kas, text=uczen['imie'])
                self.kiuczen.grid(row=1, column=1)
                self.knuczen = tki.Label(self.kas, text=uczen['nazwisko'])
                self.knuczen.grid(row=2, column=1)
                self.kkuczen = tki.Label(self.kas, text=uczen['nazwa'])
                self.kkuczen.grid(row=3, column=1)
                print(uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])

            else:
                continue

class tabele(object):

#pokazywanie wszystkich rekordów tabelarycznie

    def all():
        tabela = tki.Tk()
        tabela.title('Uczniowie')
        tabela.geometry("240x300")
        frame = tki.Frame(tabela)
        frame.pack()
        frame1 = tki.Frame(tabela)
        frame1.pack()
        frame2 = tki.Frame(tabela, width=40, height=20)
        frame2.pack(fill='both')
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame3 = tki.Frame(tabela)
        frame3.pack()
        #Kasowanie ucznia z sql i z listy
        def kasowanie():

            new=mylist.get(tki.ANCHOR)
            tuple(new)
            print(new[0])
            sql = "DELETE FROM uczniowie  WHERE uczniowie.ID = %s "
            adr = new[0]
            cur.execute(sql, adr)
            con.commit()
            mylist.delete(tki.ANCHOR)
        def szukanie():

            mylist.delete(0, tki.END)
            cur.execute(
            """
            SELECT uczniowie.ID,imie,nazwisko,nazwa,profil  FROM uczniowie,klasa WHERE uczniowie.klasa=klasa.ID
            """)
            uczniowie = cur.fetchall()

            for uczen in uczniowie:
                if uczen['nazwisko'] == str(nazwisko.get()) and uczen['imie'] == str(imie.get()):
                    mylist.insert(tki.END, (uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']))
                elif uczen['nazwisko'] == str(nazwisko.get()) and len(imie.get()) == 0:
                    mylist.insert(tki.END, (uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']))
                elif len(nazwisko.get()) == 0 and uczen['imie'] == str(imie.get()):
                    mylist.insert(tki.END, (uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']))
                elif len(nazwisko.get()) == 0 and len(imie.get()) == 0:
                    mylist.insert(tki.END, (uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']))
        def mody():
            zmiany = tki.Tk()
            zmiany.title('Modyfikuj dane')
            zmiany.geometry("260x90")
            new = tuple(mylist.get(tki.ANCHOR))
            fimie = tki.Entry(zmiany, width=10)
            fimie.insert(tki.END, new[1])
            fimie.grid(row=0, column=2)
            fnazwisko = tki.Entry(zmiany, width=10)
            fnazwisko.insert(tki.END, new[2])
            fnazwisko.grid(row=1, column=2)
            fklasa = tki.Entry(zmiany, width=10)
            fklasa.insert(tki.END, new[3])
            nowy = (fimie.get(), fnazwisko.get(), new[0])
            cur.execute("UPDATE uczniowie SET imie=%s, nazwisko=%s  WHERE ID=%s", nowy)
            fklasa.grid(row=2, column=2)
            tki.Label(zmiany, text="Imię:").grid(row=0, column=0)
            tki.Label(zmiany, text="Nazwisko:").grid(row=1, column=0)
            tki.Label(zmiany, text="Klasa:").grid(row=2, column=0)
            tki.Button(zmiany, width=10, text="Zmień", command=lambda: print(nowy) ).grid(row=2, column=3, sticky="nsew", pady=2)
            con.commit
            def popraw():
                con.commit

                print("done")
        def pusto():
            mylist.delete(0, tki.END)

        kasuj = tki.Button(frame3, text="Kasuj ucznia", command=kasowanie)
        kasuj.grid(row=1, column=0)
        szukaj = tki.Button(frame3, text="Szukaj ucznia", command=szukanie)
        szukaj.grid(row=1, column=1)
        mod = tki.Button(frame3, text="Popraw dane", command=mody)
        mod.grid(row=2, column=1)
        empty = tki.Button(frame3, text="Wyczysć liste", command=pusto)
        empty.grid(row=2, column=0)
        imie = tki.Entry(frame, width=10)
        imie.insert(tki.END, "Adam")
        imie.grid(row=0, column=0)
        nazwisko = tki.Entry(frame, width=10)
        #nazwisko.insert(tki.END, "Kowal")
        nazwisko.grid(row=0, column=1)
        tki.Label(frame1, text="ID  Imię Nazwisko Klasa             ").grid(row=1, column=0, sticky="E")
        tki.Label(frame1, text="Imię:").grid(row=1, column=1)
        #tki.Label(frame1, text="Nazwisko:").grid(row=1, column=2)
        #tki.Label(frame1, text="Klasa:").grid(row=1, column=3)
        #Funkcja pobiera i wyświetla dane z bazy
        """Funkcja pobiera i wyświetla dane z bazy."""
        cur.execute(
            """
            SELECT uczniowie.ID,imie,nazwisko,nazwa,profil  FROM uczniowie,klasa WHERE uczniowie.klasa=klasa.ID
            """)
        uczniowie = cur.fetchall()
        i = 0
        mylist = tki.Listbox(frame2, width=5, selectmode=tki.EXTENDED)
        mylist.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        #new = tuple(mylist.get(tki.ANCHOR))
        scrollb = tki.Scrollbar(frame2, command=mylist.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        mylist['yscrollcommand'] = scrollb.set
        for uczen in uczniowie:
            mylist.insert(tki.END, (uczen['ID'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']))
            #test =tuple(uczen['ID'], uczen['imie'],uczen['nazwisko'], uczen['nazwa'])
            #tki.Label(frame, text=uczen['ID']).grid(row=2 + i, column=0)
            #tki.Label(frame, text=uczen['imie']).grid(row=2 + i, column=1)
            #tki.Label(frame, text=uczen['nazwisko']).grid(row=2 + i, column=2)
            #tki.Label(frame, text=uczen['nazwa']).grid(row=2 + i, column=3)
            #print(test)
            i = i + 1

app = apka()
app.root.mainloop()
