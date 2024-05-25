from uzivatel import Uzivatel

class Pojistovna:
    """
    Třída reprezentující pojišťovnu.

    Attributes:
        pojisteni_uzivatele (list of Uzivatel): Seznam uživatelů, kteří mají uzavřené pojištění.
    """

    def __init__(self):
        """
        Inicializuje novou instanci třídy Pojistovna.
        """
        self.pojisteni_uzivatele = []
    
    def vytvorit_uzivatele(self, jmeno: str, prijmeni: str, vek: int, telefon: str) -> Uzivatel:
        """
        Vytvoří nového uživatele a přidá ho do seznamu pojistěných uživatelů.

        Args:
            jmeno: Jméno uživatele.
            prijmeni: Příjmení uživatele.
            vek: Věk uživatele.
            telefon: Telefonní číslo uživatele.

        Returns:
            Uzivatel: Nově vytvořený uživatel.
        """
        uzivatel = Uzivatel(jmeno, prijmeni, vek, telefon)
        self.pojisteni_uzivatele.append(uzivatel)
        return uzivatel

    def ziskat_vsechny_uzivatele(self) -> list:
        """
        Vrátí seznam všech pojistěných uživatelů.

        Returns:
            list of Uzivatel: Seznam všech pojistěných uživatelů.
        """
        return self.pojisteni_uzivatele

    def vyhledat_uzivatele(self, jmeno: str, prijmeni: str) -> Uzivatel | None:
        """
        Vyhledá uživatele podle jména a příjmení.

        Args:
            jmeno: Jméno uživatele.
            prijmeni: Příjmení uživatele.

        Returns:
            Uzivatel: Vrací nalezeného uživatele.
            None: Pokud uživatel nebyl nalezen.
        """
        for uzivatel in self.pojisteni_uzivatele:
            if uzivatel.jmeno == jmeno and uzivatel.prijmeni == prijmeni:
                return uzivatel
        return None