#!/usr/bin/env python3

from reader import set_speed, read_from_file, read_text
import argparse


def main():
    desc = "Shirah is a terminal speed reader."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        "-s",
        "--speed",
        metavar="SPEED",
        dest="speed",
        type=int,
        help="Set the words per minute. Defaults to 400 wpm.",
        default=400,
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE",
        dest="file",
        type=str,
        help="File path to read text.",
        default=None,
    )

    if parser.parse_args().file:
        wpm = parser.parse_args().speed
        set_speed(wpm)
        read_from_file(parser.parse_args().file)
    else:
        read_text(TEST, parser.parse_args().speed)


if __name__ == "__main__":
    main()
