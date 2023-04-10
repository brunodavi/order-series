from unittest import TestCase
from pathlib import Path

from order_series.series_handler import filter_files_exists


class TestFilterFilesExists(TestCase):
    def setUp(self):
        self.caminho_serie = Path('Serie1 - EP 02.mp4')
        self.caminho_serie.touch()

    def tearDown(self):
        self.caminho_serie.unlink()


    def test_filtra_em_arquivos_existentes(self):
        entrada = [
            Path('Serie1 - EP 01.mp4'),
            Path('Serie2 - EP 01.mp4'),
            Path('Serie1 - EP 02.mp4'),
        ]

        esperado = [
            self.caminho_serie
        ]

        resultado = filter_files_exists(entrada)

        self.assertEqual(resultado, esperado)

