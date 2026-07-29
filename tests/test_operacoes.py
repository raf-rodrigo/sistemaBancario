import unittest
from operacoes import depositar, sacar


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


class TestSacar(unittest.TestCase):
    def test_saque_valido_atualiza_estado(self):
        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=1000,
            valor=100,
            extrato="",
            limite=500,
            numeros_saques=0,
            limite_saques=3
        )

        self.assertEqual(saldo, 900)
        self.assertIn("R$ 100.00", extrato)
        self.assertEqual(numeros_saques, 1)
        self.assertIn("Saque realizado com sucesso", mensagem)

    def test_saque_com_saldo_insuficiente_preserva_estado(self):
        saldo_inicial = 100
        extrato_inicial = "Movimento anterior"
        saques_iniciais = 1

        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=saldo_inicial,
            valor=200,
            extrato=extrato_inicial,
            limite=500,
            numeros_saques=saques_iniciais,
            limite_saques=3,
        )

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)
        self.assertEqual(numeros_saques, saques_iniciais)
        self.assertIn('saldo', mensagem)

    def test_saque_acima_do_limite_preserva_estado(self):
        saldo_inicial = 1000
        extrato_inicial = "Movimento anterior"
        saques_iniciais = 1

        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=saldo_inicial,
            valor=600,
            extrato=extrato_inicial,
            limite=500,
            numeros_saques=saques_iniciais,
            limite_saques=3,
        )

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)
        self.assertEqual(numeros_saques, saques_iniciais)
        self.assertIn('excede o limite', mensagem)

    def test_limite_de_saques_preserva_estado(self):
        saldo_inicial = 1000
        extrato_inicial = "Movimento anterior"
        saques_iniciais = 3

        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=saldo_inicial,
            valor=100,
            extrato=extrato_inicial,
            limite=500,
            numeros_saques=saques_iniciais,
            limite_saques=3,
        )

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)
        self.assertEqual(numeros_saques, saques_iniciais)
        self.assertIn("máximo de saques", mensagem)

    def test_saque_com_valor_invalido_preserva_estado(self):
        saldo_inicial = 1000
        extrato_inicial = "Movimento anterior"
        saques_iniciais = 1

        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=saldo_inicial,
            valor=0,
            extrato=extrato_inicial,
            limite=500,
            numeros_saques=saques_iniciais,
            limite_saques=3,
        )

        self.assertEqual(saldo, saldo_inicial)
        self.assertEqual(extrato, extrato_inicial)
        self.assertEqual(numeros_saques, saques_iniciais)
        self.assertIn("inválido", mensagem)


if __name__ == "__main__":
    unittest.main()
