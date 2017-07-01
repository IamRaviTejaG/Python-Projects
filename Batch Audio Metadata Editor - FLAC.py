# Batch Audio Metadata Editor

"""
The example code below removes the 'comment' tag from FLAC files.
"""

from mutagen.flac import FLAC
from os import *
from sys import stdout

path = 'D:/Music/Lossless Audios/'
a = listdir(path)
for i in a:
	path = 'D:/Music/Lossless Audios/' + i + '/'
	chdir(path)
	j = listdir(path)
	for k in j:
		audio = FLAC(k)
		try:
			audio['comment'] = ''
			audio.save()
		except KeyError:
			pass
	stdout.write("Done!")
