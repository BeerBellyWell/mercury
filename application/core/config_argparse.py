import argparse


def configure_argument_parser(
    available_modes: dict
) -> argparse.ArgumentParser:
    """
    Takes a dictionary as an argument and converts
    the keys of the dictionary into positional argparse arguments.
    """
    parser = argparse.ArgumentParser(description='Working with Mercury.')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Operation modes'
    )
    return parser
