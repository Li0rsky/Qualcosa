class Persona: 
    __cognome = ""
    __nome = ""
    __indirizzo = ""
    __residenza = ""


    def __init__(self, c, n, i, r):
        self.__cognome = c
        self.__nome = n
        self.__indirizzo = i
        self.__residenza = r

    def visualizza(self):
        print(f"Cognome: {self.__cognome}")
        print(f"Nome: {self.__nome}")
        print(f"Indirizzo: {self.__indirizzo}")
        print(f"Residenza: {self.__residenza}")

class Dipendente(Persona):
    __qualifica = ""
    __stipendio = 0.0
    
    def __init__(self, c, n, i, r, q, s):
        super().__init__(c, n, i, r)
        self.__qualifica = q
        self.__stipendio = s

    def reddito(self):
        return self.__stipendio * 13

    def get_qualifica(self):
        return self.__qualifica

def main():
    dipendente = None
    while True:
        print("Menu:")
        print("1. Inserimento dati")
        print("2. Visualizzazione dati Persona")
        print("3. Calcolo reddito")
        print("4. Output qualifica")
        print("5. Esci")
        scelta = input("Scegli un'opzione (1-5): ")
        if scelta == "1":
            c = input("Inserisci cognome: ")
            n = input("Inserisci nome: ")
            i = input("Inserisci indirizzo: ")
            r = input("Inserisci residenza: ")
            q = input("Inserisci qualifica: ")
            s = float(input("Inserisci stipendio: "))
            dipendente = Dipendente(c, n, i, r, q, s)
        elif scelta == "2":
            if dipendente is not None:
                dipendente.visualizza()
            else:
                print("Devi prima inserire i dati del dipendente.")
        elif scelta == "3":
            if dipendente is not None:
                print(f"Reddito annuale: {dipendente.reddito()} euro.")
            else:
                print("Devi prima inserire i dati del dipendente.")
        elif scelta == "4":
            if dipendente is not None:
                print(f"Qualifica: {dipendente.get_qualifica()}")
            else:
                print("Devi prima inserire i dati del dipendente.")
        elif scelta == "5":
            break
        else:
            print("Scelta non valida. Scegli un'opzione tra 1 e 5.")
main()