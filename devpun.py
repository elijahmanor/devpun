#!/usr/bin/env python3
import argparse
import collections
import json
import random
import sys
from typing import Dict, List, Union


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    action: argparse._MutuallyExclusiveGroup = parser.add_mutually_exclusive_group()
    action.add_argument(
        "--count",
        "-c",
        dest="action",
        type=int,
        help="Show up to N matching jokes",
        metavar="N",
    )
    action.add_argument(
        "--list",
        "--list-jokes",
        "-l",
        dest="action",
        action="store_const",
        const="list",
        help="List all matching jokes, instead of choosing one at random",
    )
    action.add_argument(
        "--list-tags",
        "-T",
        dest="action",
        action="store_const",
        const="list_tags",
        help="List all available tags with corresponding joke count, then exit.",
    )
    parser.add_argument(
        "--tag",
        "-t",
        nargs=1,
        action="append",
        dest="tags",
        help="Filter by tag (ANDed if repeated)",
        default=[],
    )
    opts: argparse.Namespace = parser.parse_args()

    joke_list: List[Dict[str, Union[str, List[str]]]] = json.load(
        open("jokes.json", "r")
    )

    if opts.action == "list_tags":
        tag_list: Dict[str, int] = collections.defaultdict(int)
        for j in joke_list:
            for t in j.get("tags", []):
                tag_list[t] += 1
        print("\n".join(["%3d %s" % (tag_list[t], t) for t in sorted(tag_list.keys())]))
        return 0

    if opts.tags:
        for tag in opts.tags:
            joke_list = filter(lambda j: tag[0] in j.get("tags", []), joke_list)

    # Shuffle, and also boil it back down from a filter
    joke_list: List[Dict[str, Union[str, List[str]]]] = list(joke_list)
    random.shuffle(joke_list)

    if not joke_list:
        print("No matching jokes found.")
        return 1

    if opts.action != "list":
        count: int = 1
        if isinstance(opts.action, int):
            count: int = opts.action
        joke_list = joke_list[:count]

    i: int
    j: Dict[str, Union[str, List[str]]]
    for i, j in enumerate(joke_list):
        if i:
            # Add a blank line between jokes.
            print("")

        if j.get("text", None):
            print(j["text"])
        else:
            print(f"Q. {j['question']}")
            print(f"A. {j['answer']}")


if __name__ == "__main__":
    sys.exit(main())
