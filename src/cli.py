from pathlib import Path
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser(
        prog='order-series',
        description=(
            'Move arquivos de series '
            'para pastas com seus nomes'
        ),
    )

    parser.add_argument(
        'video_series',
        type=Path,
        nargs='+',
        help=(
            'Arquivos de series com o nome da series'
            ' e seu contador de episódios'
            ' (ex: Serie - Episódio 01)'
        ),
    )

    return parser

