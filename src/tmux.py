#!/usr/bin/env python3
import json
import argparse

from common import run_command, AlfredJsonFormatList


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["list"])
    return parser.parse_args()


def list_tmux_sessions():
    cmd = "tmux ls | cut -d: -f1"
    stdout = run_command(cmd, shell=True)

    alfred_json_list = AlfredJsonFormatList.from_list(stdout.split("\n"))
    return alfred_json_list.to_json_str()


def main():
    args = parse_args()
    if args.action == "list":
        output = list_tmux_sessions()
    return output


if __name__ == "__main__":
    print(main())
