#! /usr/bin/python


"""
mknote

Usage:
mknote
"""


import subprocess # .call and .check_output
import time # .time


print "Hello from mknote"


MKNOTE_EDITOR = 'mate'
NOTE_DIR = '/Users/jon/Dropbox/life/Untitled\ Shit/mknote/'


# implemented by having timestamp be filename.
# less race-safe than tempfile.NamedTemporaryFile,
# but sufficient for a program like mknote that won't be called multiple times per sec

filename = time.time()

filename += '.txt'

filename = NOTE_DIR + filename

subprocess.call([MKNOTE_EDITOR, filename])

