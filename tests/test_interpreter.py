import unittest

from grove.interpreter import RuntimeError_, run
from grove.lexer import tokenize
from grove.parser import parse

from tests.test_lexer import FATORIAL


def execute(src):
    saida = []
    run(parse(tokenize(src)), out=saida.append)
    return saida


class InterpreterTest(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(execute(FATORIAL), ["120"])

    def test_aritmetica_e_strings(self):
        self.assertEqual(execute("CJPHONEHOME 7 / 2 × CJPHONEHOME 7 % 2 × CJPHONEHOME -3 * 2 ×"), ["3", "1", "-6"])
        self.assertEqual(execute('CJPHONEHOME "a" + "b" ×'), ["ab"])
        self.assertEqual(execute("CJPHONEHOME FULLCLIP × CJPHONEHOME 1 < 2 L2 □ GHOSTTOWN ×"), ["FULLCLIP", "FULLCLIP"])

    def test_if_else_e_break(self):
        src = """
        HESOYAM i = 0 ×
        BAGUVIX L1 FULLCLIP R1 △
            i = i + 1 ×
            AEZAKMI L1 i == 3 R1 △ CPKTNWT × ○ ASNAEB △ CJPHONEHOME i × ○
        ○
        """
        self.assertEqual(execute(src), ["1", "2"])

    def test_escopo_de_bloco(self):
        src = """
        HESOYAM x = 1 ×
        △ HESOYAM x = 2 × CJPHONEHOME x × x = 3 × ○
        CJPHONEHOME x ×
        △ x = 9 × ○
        CJPHONEHOME x ×
        """
        self.assertEqual(execute(src), ["2", "1", "9"])

    def test_erros_semanticos(self):
        casos = {
            "CJPHONEHOME y ×": "não declarada",
            "HESOYAM a = 1 × HESOYAM a = 2 ×": "já declarada",
            "CPKTNWT ×": "fora de laço",
            "CJPHONEHOME 1 / 0 ×": "divisão por zero",
            "AEZAKMI L1 1 R1 △ ○": "booleano",
            'CJPHONEHOME 1 + "a" ×': "tipos",
        }
        for src, trecho in casos.items():
            with self.subTest(src=src), self.assertRaises(RuntimeError_) as cm:
                execute(src)
            self.assertIn(trecho, str(cm.exception))


if __name__ == "__main__":
    unittest.main()
