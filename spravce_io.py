from validace_vstupu import ValidaceVstupu
class SpravceIO():




    HLAVNI_MENU = (
'''
------------------
Evidence pojištění
------------------

Vyberte z možností:
1 - Přidat nového pojištěného uživatele
2 - Vypsat všechny pojištěné uživatele
3 - Vyhledat pojištěného uživatele  
4 - Ukončit
'''
)
    
    
    KONEC_MENU = (
'''
Enter - návrat do hlavního menu
Q - ukončení
'''
)

    @staticmethod
    def ziskat_udaj(udaj, validace):
        while True:
            vstup = input(f"Zadejte {udaj}: ")
            if validace(vstup):
                return vstup
            else:
                print(f"\nZadejte {udaj} ve správném formátu")


    @staticmethod
    def ziskat_vstupni_udaje():
        jmeno = SpravceIO.ziskat_udaj("jméno", ValidaceVstupu.validovat_jmeno)
        prijmeni = SpravceIO.ziskat_udaj("příjmení", ValidaceVstupu.validovat_jmeno)
        vek = SpravceIO.ziskat_udaj("věk", ValidaceVstupu.validovat_vek)
        telefon = SpravceIO.ziskat_udaj("telefon", ValidaceVstupu.validovat_telefon)
        return jmeno, prijmeni, vek, telefon
    

    @staticmethod
    def ziskat_jmeno_prijmeni():
        jmeno = SpravceIO.ziskat_udaj("jméno", ValidaceVstupu.validovat_jmeno)
        prijmeni = SpravceIO.ziskat_udaj("příjmení", ValidaceVstupu.validovat_jmeno)
        return jmeno, prijmeni


    @staticmethod
    def ziskat_volbu_menu():
        volba = SpravceIO.ziskat_udaj("možnost", ValidaceVstupu.validovat_menu)
        return volba


    @staticmethod
    def ziskat_volbu_konec_menu():
        volba = SpravceIO.ziskat_udaj("možnost", ValidaceVstupu.validovat_konec_menu)
        return volba


    @staticmethod
    def vypsat_menu(menu):
        if menu == "hlavni_menu":
            print(SpravceIO.HLAVNI_MENU)
        elif  menu == "konec_menu":
            print(SpravceIO.KONEC_MENU)
        else:
            print("Nesprávný typ menu")
    

    @staticmethod
    def vypsat_seznam_uzivatelu(seznam_uzivatelu):
        if seznam_uzivatelu:
            print("\nSeznam pojištěných uživatelů: \n")
            for uzivatel in seznam_uzivatelu:
                print(f"- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
        else:
            print("\nSeznam pojištěných uživatelů je prázdný")

    
    @staticmethod
    def vypsat_vytvoreni_uzivatele(uzivatel):
        print(f"\nUživatel {uzivatel.jmeno} {uzivatel.prijmeni} byl úspěšně vytvořen.")


    @staticmethod
    def vypsat_vyhledani_uzivatele(uzivatel):
        if uzivatel is not None:
            print(f"\nUživatel {uzivatel.jmeno} {uzivatel.prijmeni} nalezen: \n")
            print(f"- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
        else:
            print(f"\nUživatel nebyl nalezen")