#!/usr/bin/env python3

import sys

from plot import plot_tree
from rbtree import RedBlackTree


def search(rbt: RedBlackTree, x: str) -> None:
    print(rbt.search(x).get_key())


def plot(rbt: RedBlackTree) -> None:
    plot_tree(rbt.get_root())


COMMANDS = {
    "insert": RedBlackTree.insert,
    "delete": RedBlackTree.delete,
    "search": search,
    "print": RedBlackTree.print_tree,
    "plot": plot,
    "exit": lambda rbt, *tokens: sys.exit(),
}

COMMANDS_LIST = ", ".join(COMMANDS)


def repl_loop() -> None:
    rbt = RedBlackTree()

    while True:
        try:
            line = input(">> ").rstrip()
        except EOFError:
            print()
            sys.exit()

        tokens = line.split()

        if not tokens:
            continue

        cmd = tokens[0].casefold()

        if cmd not in COMMANDS_LIST:
            print(f"Error: unknown command: {cmd}.")
            continue

        try:
            COMMANDS[cmd](rbt, *tokens[1:])
        except TypeError:
            print("Error: invalid number of arguments.")


def main() -> None:
    prompt = "Welcome to RB-Tree REPL.\n" f"Commands available: {COMMANDS_LIST}.\n"

    print(prompt)
    repl_loop()


if __name__ == "__main__":
    main()
