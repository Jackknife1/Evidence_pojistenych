from uzivatel import Uzivatel


#Třída pojišťovna s funkcemi pro správu a vyhledávání uživatelů v seznamu pojisteni_uzivatele
class Pojistovna:

    #Konstruktor se seznamem
    def __init__(self):
        self.pojisteni_uzivatele = []

    #Funkce vypis_menu spustí hlavní nabídku pro navigaci uživatele v aplikaci
    def vypis_menu(self):

    #While cyklus pro neustálý běh programu 
        while True:
            print(
"""
------------------
Evidence pojištění
------------------

Vyberte z možností:
1 - Přidat nového pojištěného uživatele
2 - Vypsat všechny pojištěné uživatele
3 - Vyhledat pojištěného uživatele
4 - Ukončit
"""
)

            #Kontroluje vstup uživatele a předchází chybám s datovými typy
            volba_menu = None
            while volba_menu not in (1, 2, 3, 4):

                volba_menu = input("\nVyberte možnost: ")

                if not volba_menu.isdigit():
                    print("Zadejte číslo (1-4) ")
                    continue

                volba_menu = int(volba_menu)

                if volba_menu > 4 or volba_menu < 1:
                    print("Zadejte číslo (1-4) ")

            #Podmínka pro spustění určité funkce na základě uživatelského vstupu
            if volba_menu == 1:
                    self.vytvor_uzivatele()
            elif volba_menu == 2:
                    self.vypis_vsechny_uzivatele()
            elif volba_menu == 3:
                    self.vyhledej_uzivatele()
            elif volba_menu == 4:
                    print("\nUkončení aplikace\n")
                    break
            
            #Podmínky pro kontrolu uživatelského vstupu pro návrat do hlavního menu nebo ukončení aplikace
            if True:
                konec_volba = input(

            #Menu s možnostmi ukončení programu nebo návratem do hlavního menu
"""
Libovolná klávesa - návrat do hlavního menu
Q - ukončení
"""
            )
                
            if konec_volba.lower() == "q":
                print("\nUkončení aplikace\n")
                break


    #Tato funkce vytvoří nového uživatele a uloží ho do seznamu pojisteni_uzivatele
    def vytvor_uzivatele(self):

        #Cyklus s podmínkou kontrolující, jestli je jméno textový řetězec
        while True:
            jmeno = input("\nZadejte své křestní jméno: ")

            if not jmeno.isalpha():
                print("Zadejte jméno v textovém formátu")
                continue
            else:
                jmeno = jmeno.capitalize()

                #Cyklus s podmínkou kotrolující, jestli je příjmení textový řetězec
                while True:
                    prijmeni = input("\nZadejte své příjmení: ")

                    if not prijmeni.isalpha():
                        print("Zadejte příjmení v textovém formátu")
                        continue
                    else:
                        prijmeni = prijmeni.capitalize()

                        #Cyklus s podmínkou pro kontrolu, jestli je věk v číselném formátu
                        while True:
                            vek = input("\nZadejte svůj věk: ")
                            
                            if not vek.isdigit():
                                print("Zadejte věk v číselném formátu")
                                continue
                            else:

                                #Cyklus s podmínkami pro kontrolu formátu telefonního čísla a formátování řetězce
                                while True:
                                    telefon = input("\nZadejte vaše telefonní číslo: ")
                                    telefon = "".join(telefon.split())

                                    if not telefon.isdigit():
                                        print("Zadejte telefonní číslo v číselném formátu")
                                    else:

                                        if len(telefon) != 9:
                                            print("Zadejte devítimístné telefonní číslo")
                                            continue
                                        else:
                                            
                                            uzivatel = Uzivatel(jmeno, prijmeni, vek, telefon)
                                            self.pojisteni_uzivatele.append(uzivatel)
                                            print(f"{uzivatel.__str__()} byl vytvořen")
                                            break
                            break
                    break
            break
                                

    #Tato funkce vypíše všechny uživatele ze seznamu pojisteni_uzivatele
    def vypis_vsechny_uzivatele(self):
        if self.pojisteni_uzivatele:
            print("\nSeznam pojištěných uživatelů: \n")
            for uzivatel in self.pojisteni_uzivatele:
                print(f"- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
        else:
            print("\nSeznam pojištěných uživatelů je prázdný")


    #Tato funkce vyhledá v seznamu pojisteni_uzivatele určitého uživatele podle křestního jména a příjmení
    def vyhledej_uzivatele(self):

        #Cyklus s podmínkou, která kontroluje spávný formát křestního jména
        while True:
            jmeno = input("\nZadejte křestní jméno uživatele: ")

            if not jmeno.isalpha():
                print("Zadejte křestní jméno v textovém formátu")
                continue
            else:
                #Cyklus s podmínkou, která kontroluje správný formát příjmení
                while True:
                    prijmeni = input("\nZadejte příjmení uživatele: ")
                    
                    if not prijmeni.isalpha():
                        print("Zadejte příjmení v textovém formátu")
                        continue
                    else:

                        #Kontrola, jestli je uživatel v seznamu pojisteni_uzivatele
                        nalezeny_uzivatel = False
                        for uzivatel in self.pojisteni_uzivatele:
                            if uzivatel.jmeno == jmeno and uzivatel.prijmeni == prijmeni:
                                print("\nUživatel nalezen: ")
                                print(f"\n- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
                                nalezeny_uzivatel = True
                                break
                        if not nalezeny_uzivatel:
                            print(f"\nUživatel {jmeno} {prijmeni} nebyl nalezen")
                            break
                    break
            break