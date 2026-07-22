import unittest
from operacoes import depositar


class TestDepositar(unittest.TestCase):
    def test_deposito_positivo_atualiza_saldo_e_extrato(self):
        saldo, extrato = depositar(100, "", 0)

        self.assertEqual(saldo, 100.00)
        self.assertIn("R$ 100.00", extrato)

    def test_deposito_zero_preserva_saldo_e_extrato(self):
        saldo_inicial = 50
        extrato_inicial = "Movimento anterior"

        saldo, extrato = depositar(0, extrato_inicial, saldo_inicial)

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)

    def test_deposito_negativo_preserva_saldo_e_extrato(self):
        saldo_inicial = 50
        extrato_inicial = "Movimento anterior"

        saldo, extrato = depositar(-20, extrato_inicial, saldo_inicial)

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)


if __name__ == "__main__":
    unittest.main()
