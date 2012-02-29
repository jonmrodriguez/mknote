#! /usr/bin/python


"""
mknote

Usage:
mknote
"""


import time # .time
import os # .system

print "Hello from mknote"


MKNOTE_EDITOR = 'mate'
NOTE_DIR = '/Users/jon/Dropbox/life/Untitled\ Shit/mknote/'


# implemented by having timestamp be filename.
# less race-safe than tempfile.NamedTemporaryFile,
# but sufficient for a program like mknote that won't be called multiple times per sec

filename = str(time.time())

filename += '.txt'

filename = NOTE_DIR + filename

# weirdly, when I tried using subprocess.call to create a file,
# either via touch or mate,
# there was some permissions problem that I couldn't resolve,
# where mate prompted me for the root password,
# and even after I provided it, couldn't save the file!
# (and touch just silently failed)
os.system(MKNOTE_EDITOR + ' ' + filename)


