class Uzivatel:
    """
    Třída reprezentující uživatele.

    Attributes:
        jmeno (str): Jméno uživatele.
        prijmeni (str): Příjmení uživatele.
        vek (int): Věk uživatele.
        telefon (str): Telefonní číslo uživatele.
    """

    def __init__(self, jmeno: str, prijmeni: str, vek: int, telefon: str):
        """
        Inicializuje novou instanci třídy Uzivatel.

        Args:
            jmeno: Jméno uživatele.
            prijmeni: Příjmení uživatele.
            vek: Věk uživatele.
            telefon: Telefonní číslo uživatele.
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self) -> str:
        """
        Vrací textovou reprezentaci uživatele.

        Returns:
            str: Textová reprezentace uživatele.
        """
        return (f"Uživatel: {self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}")