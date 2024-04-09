#!/usr/bin/env python3

import sys

from plot import plot_tree
from rbtree import RedBlackTree

COMMANDS = {
    "insert": lambda rbt, x: rbt.insert(x),
    "delete": lambda rbt, x: rbt.delete(x),
    "search": lambda rbt, x: print(rbt.search(x).get_key()),
    "print": lambda rbt: rbt.print_tree(),
    "plot": lambda rbt: plot_tree(rbt.get_root()),
    "exit": lambda rbt: exit(""),
}


def repl_loop() -> None:
    rbt = RedBlackTree()

    while True:
        try:
            line = input(">> ").rstrip()
        except EOFError:
            exit("")

        tokens = line.split()

        if not tokens:
            continue

        cmd = tokens[0]

        if cmd not in COMMANDS:
            print(f"Error: unknown command: {cmd}.")
            continue

        if cmd in {"print", "exit", "plot"}:
            if len(tokens) != 1:
                print("Error: extra argument.")
                continue
            COMMANDS[cmd](rbt)
            continue
        elif len(tokens) != 2:
            print("Error: expected 2 arguments.")
            continue
        COMMANDS[cmd](rbt, tokens[1])


def main() -> None:
    prompt = (
        "Welcome to RB-Tree REPL.\n"
        "Commands available: insert, delete, search, print, plot, exit.\n"
    )

    print(prompt)
    repl_loop()


if __name__ == "__main__":
    main()
