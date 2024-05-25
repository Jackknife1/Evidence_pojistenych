class ValidaceVstupu:
    """
    Třída obsahující statické metody pro validaci různých uživatelských vstupů.
    """

    @staticmethod
    def validovat_menu(volba: str) -> bool:
        """
        Ověřuje platnost vstupní volby pro hlavní menu.

        Args:
            volba: Uživatelská volba.

        Returns:
            bool: True, pokud je volba platná, jinak False.
        """
        return volba in ['1', '2', '3', '4']

    @staticmethod
    def validovat_konec_menu(volba: str) -> bool:
        """
        Ověřuje platnost vstupní volby pro menu ukončení.

        Args:
            volba: Uživatelská volba.

        Returns:
            bool: True, pokud je volba platná, jinak False.
        """
        return volba.lower().strip() in ("q", "")

    @staticmethod
    def validovat_jmeno(jmeno: str) -> bool:
        """
        Ověřuje platnost vstupního jména.

        Args:
            jmeno: Jméno k ověření.t
        Returns:
            bool: True, pokud je jméno platné, jinak False.
        """
        return jmeno.isalpha() and len(jmeno) > 0

    @staticmethod
    def validovat_vek(vek: str) -> bool:
        """
        Ověřuje platnost vstupního věku.

        Args:
            vek: Věk k ověření.

        Returns:
            bool: True, pokud je věk platný, jinak False.
        """
        return 0 < int(vek) < 120

    @staticmethod
    def validovat_telefon(telefon: str) -> bool:
        """
        Ověřuje platnost vstupního telefonního čísla.

        Args:
            telefon: Telefonní číslo k ověření.

        Returns:
            bool: True, pokud je telefonní číslo platné, jinak False.
        """
        return len(telefon) == 9 and telefon.isdigit()