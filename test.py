import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'foo',
        help="string to echo")
    parser.add_argument('--test', '--t',
        action='store_true',
        help="T flag.")
    parser.add_argument('--bar',
        help="Bar")
    args = parser.parse_args()
    print(args)