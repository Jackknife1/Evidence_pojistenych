from validace_vstupu import ValidaceVstupu
from uzivatel import Uzivatel

class SpravceIO:
    """
    Třída pro správu uživatelských vstupů a výstupů.
    """

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
    def ziskat_udaj(udaj: str, validace) -> str:
        """
        Získává vstup od uživatele a validuje ho pomocí zadané validace.

        Args:
            udaj: Textový popis očekávaného vstupu.
            validace: Funkce validace vstupu.

        Returns:
            str: Získaný a validovaný vstup od uživatele.
        """
        while True:
            vstup = input(f"Zadejte {udaj}: ")
            if validace(vstup):
                return vstup
            else:
                print(f"\nZadejte {udaj} ve správném formátu")

    @staticmethod
    def ziskat_vstupni_udaje() -> tuple:
        """
        Získává vstupní údaje pro vytvoření nového uživatele.

        Returns:
            tuple: Jméno, příjmení, věk a telefon nového uživatele.
        """
        jmeno = SpravceIO.ziskat_udaj("jméno", ValidaceVstupu.validovat_jmeno)
        prijmeni = SpravceIO.ziskat_udaj("příjmení", ValidaceVstupu.validovat_jmeno)
        vek = SpravceIO.ziskat_udaj("věk", ValidaceVstupu.validovat_vek)
        telefon = SpravceIO.ziskat_udaj("telefon", ValidaceVstupu.validovat_telefon)
        return jmeno, prijmeni, vek, telefon

    @staticmethod
    def ziskat_jmeno_prijmeni() -> tuple:
        """
        Získává jméno a příjmení pro vyhledání uživatele.

        Returns:
            tuple: Jméno a příjmení uživatele.
        """
        jmeno = SpravceIO.ziskat_udaj("jméno", ValidaceVstupu.validovat_jmeno)
        prijmeni = SpravceIO.ziskat_udaj("příjmení", ValidaceVstupu.validovat_jmeno)
        return jmeno, prijmeni

    @staticmethod
    def ziskat_volbu_menu() -> str:
        """
        Získává volbu z hlavního menu.

        Returns:
            str: Volba z hlavního menu.
        """
        volba = SpravceIO.ziskat_udaj("možnost", ValidaceVstupu.validovat_menu)
        return volba

    @staticmethod
    def ziskat_volbu_konec_menu() -> str:
        """
        Získává volbu z menu ukončení.

        Returns:
            str: Volba z menu ukončení.
        """
        volba = SpravceIO.ziskat_udaj("možnost", ValidaceVstupu.validovat_konec_menu)
        return volba

    @staticmethod
    def vypsat_menu(menu: str) -> None:
        """
        Vypisuje menu na standardní výstup.

        Args:
            menu: Typ menu (hlavni_menu nebo konec_menu).
        """
        if menu == "hlavni_menu":
            print(SpravceIO.HLAVNI_MENU)
        elif  menu == "konec_menu":
            print(SpravceIO.KONEC_MENU)
        else:
            print("Nesprávný typ menu")

    @staticmethod
    def vypsat_seznam_uzivatelu(seznam_uzivatelu: list) -> None:
        """
        Vypisuje seznam pojištěných uživatelů na standardní výstup.

        Args:
            seznam_uzivatelu: Seznam pojištěných uživatelů.
        """
        if seznam_uzivatelu:
            print("\nSeznam pojištěných uživatelů: \n")
            for uzivatel in seznam_uzivatelu:
                print(f"- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
        else:
            print("\nSeznam pojištěných uživatelů je prázdný")

    @staticmethod
    def vypsat_vytvoreni_uzivatele(uzivatel: Uzivatel) -> None:
        """
        Vypisuje potvrzení vytvoření uživatele na standardní výstup.

        Args:
            uzivatel: Vytvořený uživatel.
        """
        print(f"\nUživatel {uzivatel.jmeno} {uzivatel.prijmeni} byl úspěšně vytvořen.")

    @staticmethod
    def vypsat_vyhledani_uzivatele(uzivatel: Uzivatel) -> None:
        """
        Vypisuje výsledek vyhledání uživatele na standardní výstup.

        Args:
            uzivatel: Nalezený uživatel.
            None: Pokud uživatel nebyl nalezen.
        """
        if uzivatel is not None:
            print(f"\nUživatel {uzivatel.jmeno} {uzivatel.prijmeni} nalezen: \n")
            print(f"- {uzivatel.jmeno}    {uzivatel.prijmeni}    {uzivatel.vek}    {uzivatel.telefon} -")
        else:
            print(f"\nUživatel nebyl nalezen")