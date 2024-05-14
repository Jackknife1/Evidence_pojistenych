from pojistovna import Pojistovna
from spravce_io import SpravceIO



def main():
    
    pojistovna = Pojistovna()

    while True:
            SpravceIO.vypsat_menu("hlavni_menu")
            volba_menu = SpravceIO.ziskat_volbu_menu()
            if volba_menu == "1":
                jmeno, prijmeni, vek, telefon = SpravceIO.ziskat_vstupni_udaje()
                uzivatel = pojistovna.vytvorit_uzivatele(jmeno, prijmeni, vek, telefon)
                SpravceIO.vypsat_vytvoreni_uzivatele(uzivatel)
            elif volba_menu == "2":
                seznam = pojistovna.ziskat_vsechny_uzivatele()
                SpravceIO.vypsat_seznam_uzivatelu(seznam)
            elif volba_menu == "3":
                jmeno, prijmeni = SpravceIO.ziskat_jmeno_prijmeni()
                uzivatel = pojistovna.vyhledat_uzivatele(jmeno, prijmeni)
                SpravceIO.vypsat_vyhledani_uzivatele(uzivatel)
            elif volba_menu == "4":
                break
            SpravceIO.vypsat_menu("konec_menu")
            volba_konec_menu = SpravceIO.ziskat_volbu_konec_menu()
            if volba_konec_menu:
                break
            continue

if __name__ == "__main__":
    main()