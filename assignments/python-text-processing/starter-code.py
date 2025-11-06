#!/usr/bin/env python3
"""starter-code.py

Simple starter code for the "Python Text Processing" assignment.

Usage examples:
    python3 starter-code.py --input sample.txt --count words
    python3 starter-code.py --input sample.txt --top 10

This file provides a minimal CLI and helper functions that students can extend.
"""
import argparse
import collections
import re
import sys
from pathlib import Path


def read_text(path: Path) -> str:
    """Read the full text from a file and return as a string."""
    with path.open("r", encoding="utf-8", errors="replace") as f:
        return f.read()


def count_words(text: str) -> int:
    words = re.findall(r"\b\w+\b", text.lower())
    return len(words)


def count_lines(text: str) -> int:
    return text.count("\n") + (0 if text.endswith("\n") or not text else 1)


def count_chars(text: str) -> int:
    return len(text)


def top_n_words(text: str, n: int = 10):
    words = re.findall(r"\b\w+\b", text.lower())
    return collections.Counter(words).most_common(n)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple text-processing starter script")
    parser.add_argument("--input", "-i", required=True, help="Path to input text file")
    parser.add_argument("--count", choices=["words", "lines", "chars"], help="Count words/lines/chars")
    parser.add_argument("--top", type=int, help="Show top N most common words")
    parser.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Find-and-replace OLD with NEW (prints result)")
    parser.add_argument("--output", "-o", help="Optional output file to write results")
    parser.add_argument("--inplace", action="store_true", help="If set, perform replace in-place (overwrites input) ")
    args = parser.parse_args(argv)

    path = Path(args.input)
    if not path.exists() or not path.is_file():
        print(f"Error: input file not found: {path}", file=sys.stderr)
        sys.exit(2)

    text = read_text(path)

    output_lines = []

    if args.count:
        if args.count == "words":
            output_lines.append(f"Words: {count_words(text)}")
        elif args.count == "lines":
            output_lines.append(f"Lines: {count_lines(text)}")
        elif args.count == "chars":
            output_lines.append(f"Chars: {count_chars(text)}")

    if args.top:
        output_lines.append("Top words:")
        for w, c in top_n_words(text, args.top):
            output_lines.append(f"{w}: {c}")

    if args.replace:
        old, new = args.replace
        replaced = text.replace(old, new)
        if args.inplace:
            path.write_text(replaced, encoding="utf-8")
            output_lines.append(f"In-place replace: wrote changes to {path}")
        else:
            output_lines.append("--- Replaced text preview ---")
            output_lines.append(replaced[:1000])

    if args.output:
        outp = Path(args.output)
        outp.write_text("\n".join(output_lines), encoding="utf-8")
        print(f"Wrote results to {outp}")
    else:
        print("\n".join(output_lines))


if __name__ == "__main__":
    main()
