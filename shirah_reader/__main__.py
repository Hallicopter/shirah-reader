#!/usr/bin/env python3

from shirah_reader import reader
import argparse


TEST = "A human being should be able to change a diaper, plan an invasion, \
 butcher a hog, conn a ship, design a building, write a sonnet, balance accounts,\
 build a wall, set a bone, comfort the dying, take orders, give orders,\
 cooperate, act alone, solve equations, analyze a new problem, pitch manure,\
 program a computer, cook a tasty meal, fight efficiently, die gallantly.\
 Specialization is for insects."


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
        reader.set_speed(wpm)
        reader.read_from_file(parser.parse_args().file)
    else:
        wpm = parser.parse_args().speed
        reader.set_speed(wpm)
        reader.read_text(TEST)


if __name__ == "__main__":
    main()
