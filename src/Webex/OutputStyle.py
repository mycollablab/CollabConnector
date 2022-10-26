import json
import sys


class TextStyle:
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

    @staticmethod
    def __init__(*args, **kwargs):
        print(*args, **kwargs)

    @staticmethod
    def error(message):
        print(f'\033[91m{message}\033[0m', file=sys.stderr)

    @staticmethod
    def warning(message):
        print(f'\033[93m{message}\033[0m', file=sys.stderr)

    @staticmethod
    def notify(message):
        print(f'\033[94m{message}\033[0m')

    @staticmethod
    def success(message):
        print(f'\033[92m{message}\033[0m')

    @staticmethod
    def bold(message):
        print(f'\033[1m{message}\033[0m', "")

    @staticmethod
    def text(message):
        print(message)

    @staticmethod
    def json(message):
        print(json.dumps(message, indent=4))
