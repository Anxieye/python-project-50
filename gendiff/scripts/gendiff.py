#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.cli import args


def main():
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
