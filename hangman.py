import random
class Hangman:

    def __init__(self, arvamused):
        self.proovid = 5
        self.sõna = random.choice(sõnad)
        self.arvamused = str(arvamused)

    def calc(self):   
        while self.proovid > 0:
            pettumus = 0
            arvamus = str(input("Sisestage enda arvates õige täht.\n:"))
            for täht in self.sõna:
                if täht in self.arvamused:
                    print(täht, end=""),
                else:
                    print("_", end=""),
                    pettumus += 1 
            if pettumus == 0:
                print("\nTeie võit!")
                break
            
            self.arvamused += arvamus
            if arvamus not in self.sõna:
                self.proovid -= 1
                print("Vale vastus! Proovi uuesti.")
                print(f"Teil on jäänud {self.proovid} korda!")
                if self.proovid == 0:
                    print("Teie kaotasite.")

sõnad = ["Linux", "Windows", "MacOS"]