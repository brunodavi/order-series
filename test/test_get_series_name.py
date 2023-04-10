from unittest import TestCase
from order_series.series_handler import get_series_name


NAO_TEM_SERIES = 'Não foi encontrada nenhuma serie'

NAO_EH_LISTA = 'Não foi passado uma lista'
VALOR_INVALIDO = 'Valor passado não é uma string'


class TestGetSeriesName(TestCase):
    def test_pega_os_nomes_das_series(self):
        entrada = [
            'Serie1 - Ep 1.mp4',
            'Serie1 2.mkv',
            'S1E1_Serie2.mov',
            'Serie2 - S1E1.wmv',
            'Serie3_ -Episódio 01.avi',
            'Serie3, - Episódio 02.webm',
            'Episódio 03 - Serie3.mp4',
            'Episódio 01 - Uma Boa Serie 4.avi',
            'Uma Boa Serie 4 - Episódio 02.avi',
            'Uma Boa Serie 4 - S1E3.mkv',
            'S1E4 - Uma Boa Serie 4.mkv',
            'S01E01 - Uma Serie 5.mp4',
            '02 Uma Serie 5.mp4',
            '03 - Uma Serie 5.mkv',
            'Uma Serie 5 S01E04.mp4',
            'Serie.6 S01E01.mp4',
            'Serie.6_Episódio 2.mp4',
            'Serie.6 Episódio 03.mp4',
        ]

        esperado = {
            'Serie1',
            'Serie2',
            'Serie3',
            'Uma Boa Serie 4',
            'Uma Serie 5',
            'Serie.6',
        }

        resultado = get_series_name(entrada)

        self.assertEqual(resultado, esperado)

    def test_ignora_nomes_que_nao_sao_seriess(self):
        entrada = [
            '0',
            'Serie1 - Ep 01.mp4',
            'Serie1 - Episódio 2.avi',
            'Serie1Ep01.wmv',
            'S1E1 - Serie2.mp4',
        ]

        esperado = {
            'Serie1',
            'Serie2',
        }

        resultado = get_series_name(entrada)

        self.assertEqual(resultado, esperado)

    def test_erro_nao_tem_series_na_lista(self):
        entrada = [
            'jfjeixniejdk',
            'nckdndkdnkd',
            'kdmdkdjjdj',
        ]

        with self.assertRaises(ValueError) as error:
            get_series_name(entrada)

        self.assertEqual(
            str(error.exception),
            NAO_TEM_SERIES,
        )

    def test_erro_algum_valor_invalido_na_lista(self):
        with self.assertRaises(ValueError) as error:
            get_series_name(['1', 2, '3'])

        self.assertEqual(
            str(error.exception),
            VALOR_INVALIDO,
        )

    def test_erro_nao_e_uma_lista(self):
        with self.assertRaises(ValueError) as error:
            get_series_name(None)

        self.assertEqual(
            str(error.exception),
            NAO_EH_LISTA,
        )

