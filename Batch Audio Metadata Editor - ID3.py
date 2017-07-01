# Batch Audio Metadata Editor

"""
The example code below sets the genre of all the MP3 files to 'Pop'.
"""

from mutagen.easyid3 import EasyID3
from os import *
from sys import stdout

path = 'D:/Music/MP3 320s/'
a = listdir(path)
for i in a:
	path = 'D:/Music/MP3 320s/' + i + '/'
	chdir(path)
	j = listdir(path)
	for k in j:
		try:
			audio = EasyID3 (k)
			audio['genre'] = 'Pop'
			audio.save()
		except:
			pass
