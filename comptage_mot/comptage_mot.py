#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

print(f"{30*'='}")

text = f""

for line in sys.stdin:
    text += line


print(f"\n{text}")

exit(0)