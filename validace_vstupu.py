class ValidaceVstupu:
   

    @staticmethod
    def validovat_menu(volba):
        return volba in ['1', '2', '3', '4']


    @staticmethod
    def validovat_konec_menu(volba):
        return volba.lower().strip() in ("q", "")


    @staticmethod
    def validovat_jmeno(jmeno):
        return jmeno.isalpha() and len(jmeno) > 0
    

    @staticmethod
    def validovat_vek(vek):
        return 0 < int(vek) < 120
    

    @staticmethod
    def validovat_telefon(telefon):
        return len(telefon) == 9 and telefon.isdigit()