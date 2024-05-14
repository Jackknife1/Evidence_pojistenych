from uzivatel import Uzivatel


class Pojistovna:

    def __init__(self):
        self.pojisteni_uzivatele = []
    
    def vytvorit_uzivatele(self, jmeno, prijmeni, vek, telefon):
        uzivatel = Uzivatel(jmeno, prijmeni, vek, telefon)
        self.pojisteni_uzivatele.append(uzivatel)
        return uzivatel

    def ziskat_vsechny_uzivatele(self):
        return self.pojisteni_uzivatele

    def vyhledat_uzivatele(self, jmeno, prijmeni):
        for uzivatel in self.pojisteni_uzivatele:
            if uzivatel.jmeno == jmeno and uzivatel.prijmeni == prijmeni:
                return uzivatel
            return None