#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
for characters in range(97, 123):
    if chr(characters) != 'q' and chr(characters) != 'e':
        print(f"{chr(characters)}", end="")
