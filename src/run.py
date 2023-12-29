from datetime import date
from pprint import pprint

from src.contorllers import view


def main() -> None:
    user_json = {
        'id': 10,
        'name': 'Vlados',
        'sign_up': date.today(),
        'friends': [1, 3, 4]
    }
    response = view(user_json, title='wef')
    pprint(response)


if __name__ == '__main__':
    main()
