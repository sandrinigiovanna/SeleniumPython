import re
from collections import Counter
from typing import List, Optional

class StringHelper:
    textos_invalidos = [
        "“", "”", "<B>", "</B>", "<b>", "</b>", "<BR>", "<br>", "\r", "\n"
    ]

    @staticmethod
    def remover_textos_invalidos(texto: str, exceto: Optional[List[str]] = None) -> str:
        filtrado = [p for p in StringHelper.textos_invalidos if not exceto or p not in exceto]
        for texto_invalido in filtrado:
            texto = texto.replace(texto_invalido, "")
        return texto

    @staticmethod
    def comparar(str1: str, str2: str) -> bool:
        str1_is_null_or_empty = not str1
        str2_is_null_or_empty = not str2

        if str1_is_null_or_empty and str2_is_null_or_empty:
            return True
        if str1_is_null_or_empty or str2_is_null_or_empty:
            return False

        str1_normalizado = StringHelper.remover_textos_invalidos(StringHelper.remover_acentos(str1)).strip().lower()
        str2_normalizado = StringHelper.remover_textos_invalidos(StringHelper.remover_acentos(str2)).strip().lower()
        return str1_normalizado == str2_normalizado

    @staticmethod
    def contem(str1: str, str2: str) -> bool:
        str1_normalizado = StringHelper.remover_acentos(str1).strip().lower()
        str2_normalizado = StringHelper.remover_acentos(str2).strip().lower()
        return str2_normalizado in str1_normalizado

    @staticmethod
    def remover_acentos(s: str) -> str:
        if not s:
            return s

        acentos = [
            "ç", "Ç", "á", "é", "í", "ó", "ú", "ý", "Á", "É", "Í", "Ó", "Ú", "Ý",
            "à", "è", "ì", "ò", "ù", "À", "È", "Ì", "Ò", "Ù", "ã", "õ", "ñ", "ä",
            "ë", "ï", "ö", "ü", "ÿ", "Ä", "Ë", "Ï", "Ö", "Ü", "Ã", "Õ", "Ñ", "â",
            "ê", "î", "ô", "û", "Â", "Ê", "Î", "Ô", "Û"
        ]
        sem_acento = [
            "c", "C", "a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y",
            "a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "a", "o", "n", "a",
            "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "A", "O", "N", "a",
            "e", "i", "o", "u", "A", "E", "I", "O", "U"
        ]

        for acento, sem in zip(acentos, sem_acento):
            s = s.replace(acento, sem)

        s = re.sub(r"[.,:\(\)\|\\/\°]", "", s)
        s = re.sub(r"^\s+", "", s)
        s = re.sub(r"\s+$", "", s)
        s = re.sub(r"\s+", " ", s)
        return s

    @staticmethod
    def string_percentage(left: str, right: str) -> float:
        left_counts = StringHelper.words_to_counts(left)
        right_counts = StringHelper.words_to_counts(right)
        return StringHelper.dictionary_percentage(left_counts, right_counts) * 100

    @staticmethod
    def dictionary_percentage(left: Counter, right: Counter) -> float:
        if left is None or right is None:
            return 1.0 if left is None and right is None else 0.0

        all_counts = sum(left.values())
        if all_counts <= 0:
            return 0.0

        found = 0.0
        for key, count in left.items():
            found += min(count, right.get(key, 0))

        return found / all_counts

    @staticmethod
    def words_to_counts(value: str) -> Counter:
        if not value:
            return Counter()

        value = StringHelper.substituir_termos_dispensaveis_texto(value)
        words = [item.strip('.,!?":;') for item in re.split(r'[ \r\n\t]+', value) if item.strip()]
        return Counter(words)

    @staticmethod
    def substituir_termos_dispensaveis_texto(texto: str) -> str:
        termos_dispensaveis = [" DA ", " DE ", " DO ", " E ", " OU "]
        for termo in termos_dispensaveis:
            texto = texto.replace(termo, " ")
        return texto
