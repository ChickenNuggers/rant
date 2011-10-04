from rant.installer import install
import os
try:
    import argparse
except ImportError:
    raise

def main():

    parser = argparse.ArgumentParser(description='Tool to interface with rant. Provides methods to create and edit pages in yaml/markdown, and generate html sites from them.')

    subparsers = parser.add_subparsers(help='sub-command help', dest='parser')

    subparsers.add_parser(
        'install',
        help='Create a new rant project in current directory'
    )

    subparsers.add_parser(
        'post',
        help='Create a new rant post in current directory'
    )

    args = parser.parse_args()

    if args.parser == 'install':
        install(os.getcwd())
        pass