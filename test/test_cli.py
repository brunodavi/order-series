from unittest import TestCase
from pathlib import Path

from order_series import get_parser


class TestCLI(TestCase):
    def setUp(self):
        self.parser = get_parser()

    def test_obtem_argumentos_de_video_series(self):
        entrada = [
            'serie1 - ep 1',
            'serie2 - episódio 1',
            'serie1 - ep 2',
        ]

        esperado = [
            Path('serie1 - ep 1'),
            Path('serie2 - episódio 1'),
            Path('serie1 - ep 2'),
        ]

        args = self.parser.parse_args(entrada)
        resultado = args.video_series

        self.assertEqual(resultado, esperado)
