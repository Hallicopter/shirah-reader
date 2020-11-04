import os
import sys
import time
import subprocess
from termcolor import colored
import argparse
import threading
import syllables
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

wpm = 400


def set_speed(input_wpm):
    global wpm
    wpm = input_wpm


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
        keybinding_msg = "Press enter to continue. \nPress ctrl+c to exit.\nPress v to view current phrase. \nEnter a number to change reading speed\nInput:  "
        try:
            option = input(keybinding_msg)
            if option and option == "v":
                print(text)
                input("Press enter to continue")
            else:
                wpm = int(option)
        except ValueError as e:
            pass
        except KeyboardInterrupt as e:
            clear()
            quit()


def chapter2text(chap):
    blacklist = [
        "[document]",
        "noscript",
        "header",
        "html",
        "meta",
        "head",
        "input",
        "script",
    ]
    output = ""
    soup = BeautifulSoup(chap, "html.parser")
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += "{} ".format(t)
    return output


def epub2text(filename):
    book = epub.read_epub(filename)
    chapters = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(chapter2text(item.get_content()))

    return chapters


def read_from_file(filename):

    if filename.split(".")[-1] == "txt":
        f = open(filename, "r")
        clear = lambda: os.system("clear")
        for text in f.readlines():
            read_text(text)
    elif filename.split(".")[-1] == "epub":
        chapters = epub2text(filename)
        for chapter in chapters:
            for text in chapter.split("\n"):
                read_text(text)
