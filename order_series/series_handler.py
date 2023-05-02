from typing import Iterable
from collections import abc

from re import sub, IGNORECASE
from pathlib import Path


PATTERNS = [
    r'^{counter}[_\W]+(.+?)\.\w{{3,4}}$',
    r'^(.+?)[_\W]+{counter}\.\w{{3,4}}$',
]

LABEL_COUNTER = [
    r'S\d+E\d+',
    r'Episódios? \d+',
    r'Ep \d+',
]


def filter_files_exists(path_list: Iterable[Path]) -> list[Path]:
    def path_exists(path: Path):
        return path.exists()

    path_list_exists = filter(path_exists, path_list)
    path_list_exists = list(path_list_exists)

    return path_list_exists


def get_series_name(path_videos: Iterable[str]) -> set[str]:
    if not isinstance(path_videos, abc.Iterable):
        raise ValueError('Não foi passado uma lista')

    series_names = set()

    for video_name in path_videos:
        if not isinstance(video_name, str):
            raise ValueError('Valor passado não é uma string')

        value = video_name

        for pattern in PATTERNS:
            counter = '|'.join(LABEL_COUNTER)
            counter = f'(?:{counter})'
            pattern = pattern.format(counter=counter)

            value = sub(
                pattern,
                r'\1',
                video_name,
                flags=IGNORECASE,
            )

            if value != video_name:
                break

        if value != video_name:
            series_names.add(value)

    if len(series_names) == 0:
        raise ValueError('Não foi encontrada nenhuma serie')

    return series_names
