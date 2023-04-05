from re import sub, IGNORECASE


PATTERNS = [
    r'^{counter}[_\W]+(.+?)\.\w{{3,4}}$',
    r'^(.+?)[_\W]+{counter}\.\w{{3,4}}$',
]

LABEL_COUNTER = [
    r'S\d+E\d+',
    r'Episódios? \d+',
    r'Ep \d+',
    r'\d+'
]


def get_series_name(videos):
    if not isinstance(videos, list):
        raise ValueError('Não foi passado uma lista')

    if len(videos) == 0:
        raise ValueError('')

    series_names = set()

    for video_name in videos:
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
