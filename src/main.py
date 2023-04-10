from pathlib import Path

from src.cli import get_parser
from src.series_handler import (
    get_series_name,
    filter_files_exists,
)


def main(args = None):
    parser = get_parser()
    args = parser.parse_args(args)

    path_list = args.video_series
    path_list_exists = filter_files_exists(path_list)

    path_list_exists = list(
        map(str, path_list_exists)
    )

    series_names_list = get_series_name(path_list_exists)

    series_names_list = sorted(
        series_names_list,
        reverse=True,
        key=len,
    )

    for serie_name in series_names_list:
        dir_name = Path(serie_name)
        dir_name.mkdir()

        for video_path in Path().iterdir():
            if not video_path.is_dir():
                if serie_name in video_path.name:
                    new_path = dir_name / video_path.name
                    video_path.rename(new_path)


if __name__ == "__main__":
    main()
