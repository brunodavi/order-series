from tempfile import TemporaryDirectory
from unittest import TestCase
from pathlib import Path

from contextlib import chdir
from os import listdir

from order_series import main


class TestMain(TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.contexto = chdir(self.tmp.name)
        self.contexto.__enter__()

        self.pastas_extras = [
            'pasta/',
            'Uma boa serie 4/',
            'Uma Serie 3/'
        ]

        self.entrada_de_arquivos_em_pasta = [
            'pasta/Uma boa serie 4 - Episódio 01.mp4',
            'pasta/Uma boa serie 4 - Episódio 02.mp4',
            'pasta/Uma boa serie 4 - Episódio 03.mp4',
            'pasta/Uma boa serie 4 - Episódio 04.mp4',
        ]

        self.entrada_de_arquivos = [
            'serie2 - ep 1.avi',
            'serie.1 season 2 - ep 1.mp4',
            'serie.1 - ep 1.mp4',
            'serie.1 - ep 2.mp4',
            'serie.1 season 2 - ep 2.mp4',
            'Episódio 1 - Uma Serie 3.mp4',
            'Episódio 2 - Uma Serie 3.mp4',
            'arquivo.txt',
            'serie.1 - ep 3.mp4',
            *self.entrada_de_arquivos_em_pasta,
        ]

        self.lista_esperada = [
            'pasta',
            'serie.1',
            'serie.1 season 2',
            'Uma Serie 3',
            'Uma boa serie 4',
            'arquivo.txt'
        ]

        for pasta in self.pastas_extras:
            Path(pasta).mkdir()

        for arquivo_camimho in self.entrada_de_arquivos:
            if arquivo_camimho != self.entrada_de_arquivos[0]:
                Path(arquivo_camimho).touch()

    def tearDown(self) -> None:
        self.contexto.__exit__()
        self.tmp.cleanup()


    def test_criar_pastas_com_nome_das_series(self):
        main(self.entrada_de_arquivos)

        lista_de_arquivos = listdir()

        self.assertCountEqual(
            set(lista_de_arquivos),
            self.lista_esperada,
        )

    def test_series_movidas_para_pastas_corespondente(self):
        main(self.entrada_de_arquivos)

        lista_esperada_serie1 = [
            'serie.1 - ep 1.mp4',
            'serie.1 - ep 2.mp4',
            'serie.1 - ep 3.mp4',
        ]

        lista_esperada_serie1_season2 = [
            'serie.1 season 2 - ep 1.mp4',
            'serie.1 season 2 - ep 2.mp4',
        ]

        lista_esperada_serie3 = [
            'Episódio 1 - Uma Serie 3.mp4',
            'Episódio 2 - Uma Serie 3.mp4',
        ]


        lista_esperada_serie4 = [
            'Uma boa serie 4 - Episódio 01.mp4',
            'Uma boa serie 4 - Episódio 02.mp4',
            'Uma boa serie 4 - Episódio 03.mp4',
            'Uma boa serie 4 - Episódio 04.mp4',
        ]

        lista_serie1 = listdir('serie.1/')
        lista_serie1_season = listdir('serie.1 season 2/')
        lista_serie3 = listdir('Uma Serie 3/')
        lista_serie4 = listdir('Uma boa serie 4/')

        self.assertCountEqual(
            lista_serie1,
            lista_esperada_serie1,
        )

        self.assertCountEqual(
            lista_serie1_season,
            lista_esperada_serie1_season2,
        )

        self.assertCountEqual(
            lista_serie3,
            lista_esperada_serie3,
        )

        self.assertCountEqual(
            lista_serie4,
            lista_esperada_serie4,
        )
