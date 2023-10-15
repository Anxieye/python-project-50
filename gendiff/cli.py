import argparse


def get_args():
    TEXT = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=TEXT)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    return args.first_file.lower(), args.second_file.lower(), args.format
