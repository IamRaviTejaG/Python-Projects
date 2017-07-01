# Batch File Renamer - Renames files conditionally.
"""
The example code below renames files with names in the following format:

----> Album Name - Track Number - Song Name.extension

to

----> Track Number - Song Name.extension
"""

from os import *

t = "D:/Music/Lossless Audios/"
list1 = listdir(t)
for y in list1:
	a = t + y + "/"
	b = listdir(a)
	for c in b:
		e = [j for j, d in enumerate(c) if d == '-']
		name = c[e[0]+2:e[0]+4] + " - " + c[e[1]+3:len(c)-6] + ".flac"
		print (c + "    ->    " + name)
		p = a + c
		q = a + name
		rename(p, q)
