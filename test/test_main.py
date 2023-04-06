from tempfile import TemporaryDirectory
from unittest import TestCase
from pathlib import Path

from contextlib import chdir
from os import listdir

from src.main import main


class TestMain(TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory(dir='.')
        self.contexto = chdir(self.tmp.name)
        self.contexto.__enter__()

        self.entrada_de_arquivos = [
            'serie.1 - ep 1.mp4',
            'serie.1 - ep 2.mp4',
            'serie.1 - ep 3.mp4',
            'serie2 - ep 1.avi',
            'Episódio 1 - Uma Serie 3.mp4',
            'Episódio 2 - Uma Serie 3.mp4',
            'arquivo.txt',
        ]

        for arquivo_camimho in self.entrada_de_arquivos:
            if arquivo_camimho != self.entrada_de_arquivos[0]:
                Path(arquivo_camimho).touch()

        self.lista_esperada = {
            'serie.1',
            'Uma Serie 3',
        }

    def tearDown(self) -> None:
        self.contexto.__exit__()
        self.tmp.cleanup()


    def test_criar_pastas_com_nome_das_series(self):
        main(self.entrada_de_arquivos)

        lista_de_arquivos = listdir()

        self.assertEqual(
            lista_de_arquivos,
            self.lista_esperada,
        )

    def test_series_movidas_para_pastas_corespondente(self):
        main(self.entrada_de_arquivos)

        lista_esperada_serie1 = [
            'serie.1 - ep 1.mp4',
            'serie.1 - ep 2.mp4',
            'serie.1 - ep 3.mp4',
        ]

        lista_esperada_serie3 = [
            'Episódio 1 - Uma Serie 3.mp4',
            'Episódio 2 - Uma Serie 3.mp4',
        ]

        lista_serie1 = listdir('serie.1')
        lista_serie3 = listdir('Uma Serie 3')

        self.assertListEqual(
            lista_serie1,
            lista_esperada_serie1,
        )

        self.assertListEqual(
            lista_serie3,
            lista_esperada_serie3,
        )