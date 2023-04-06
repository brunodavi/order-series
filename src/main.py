from src.series_handler import get_series_name
from src.cli import get_parser


def main(args = None):
    parser = get_parser()
    args = parser.parse_args(args)

    path_list = args.video_series
    
