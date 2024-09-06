
import unittest
from stack import Stack

def verificar_palindromo(frase):
    pilha = Stack()

    if (frase == ''):
        return True

    frase = frase.lower().replace(' ', '').replace(',', '')

    for c in frase:
        pilha.push(c)

    for i in range(pilha.size()):
        if (i >= (pilha.size() / 2)):
            return True

        if (pilha.items[i] == pilha.peek()):
            pilha.pop()
        else:
            return False

class TestVerificarPalindromo(unittest.TestCase):
    def test_palindromo_simples(self):
        self.assertTrue(verificar_palindromo("arara"))
    def test_palindromo_frase(self):
        self.assertTrue(verificar_palindromo("A base do teto desaba"))
    def test_palindromo_nao_palindromo(self):
        self.assertFalse(verificar_palindromo("palavra"))
    def test_palindromo_maiusculas_minusculas(self):
        self.assertTrue(verificar_palindromo("Radar"))
    def test_palindromo_vazio(self):
        self.assertTrue(verificar_palindromo(""))