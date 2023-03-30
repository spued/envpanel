#!/usr/bin/env python3

motd_file = open("templates/motd.txt", "r")
lines = motd_file.readlines()
motd_file.close
print(lines)
