import os
import sys
import time
import subprocess
from termcolor import colored
import argparse
import threading
import syllables


TEST = """
The Art of War is an ancient Chinese military treatise dating from the Late Spring and Autumn Period (roughly 5th century BC). The work, which is attributed to the ancient Chinese military strategist Sun Tzu ("Master Sun", also spelled Sunzi), is composed of 13 chapters. Each one is devoted to an aspect of warfare and how it applies to military strategy and tactics. For almost 1,500 years it was the lead text in an anthology that was formalised as the Seven Military Classics by Emperor Shenzong of Song in 1080. The Art of War remains the most influential strategy text in East Asian warfare[1] and has influenced both Eastern and Western military thinking, business tactics, legal strategy, lifestyles and beyond.

The book contained a detailed explanation and analysis of the Chinese military, from weapons and strategy to rank and discipline. Sun also stressed the importance of intelligence operatives and espionage to the war effort. Because Sun has long been considered to be one of history's finest military tacticians and analysts, his teachings and strategies formed the basis of advanced military training for millennia to come.

The book was translated into French and published in 1772 (re-published in 1782) by the French Jesuit Jean Joseph Marie Amiot. A partial translation into English was attempted by British officer Everard Ferguson Calthrop in 1905 under the title The Book of War. The first annotated English translation was completed and published by Lionel Giles in 1910.[2] Military and political leaders such as the Chinese communist revolutionary Mao Zedong, Japanese daimyō Takeda Shingen, Vietnamese general Võ Nguyên Giáp, and American military general Norman Schwarzkopf Jr. have drawn inspiration from the book. """

wpm = 400


def read_text(text):
    global wpm

    wps = wpm / 60.0
    pause = False
    clear = lambda: os.system("clear")
    cursor_loc = 0
    try:
        time.sleep(0.1)
        for i, word in enumerate(text.strip().split()[cursor_loc:]):
            cursor_loc = i
            word_len = len(word)
            t_wait_sec = (1 / wps) * (1 + syllables.estimate(word) ** 4 / 100)
            highlight_letter_index = min(3, round(word_len / 2))
            clear()
            spaces = abs(3 - highlight_letter_index) * " "
            print(
                "\t"
                + spaces
                + word[:highlight_letter_index]
                + colored(word[highlight_letter_index], "red")
                + word[highlight_letter_index + 1 :]
            )
            if "." in word:
                time.sleep(0.2)
            if (
                "," in word
                or "'" in word
                or '"' in word
                or "`" in word
                or "-" in word
                or "(" in word
                or ")" in word
                or ":" in word
            ):
                time.sleep(0.15)
            time.sleep(t_wait_sec)
    except KeyboardInterrupt as e:
        clear()
        print("Current wpm:", wpm)
        keybinding_msg = "Press enter to continue. \nPress ctrl+c to exit.\nEnter a number to change reading speed: "
        try:
            option = input(keybinding_msg)
            if option:
                wpm = int(option)
        except ValueError as e:
            pass
        except KeyboardInterrupt as e:
            clear()
            quit()


def read_from_file(filename):
    f = open(filename, "r")
    clear = lambda: os.system("clear")
    for text in f.readlines():
        read_text(text)


if __name__ == "__main__":
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
        read_from_file(parser.parse_args().file)
    else:
        read_text(TEST, parser.parse_args().speed)
