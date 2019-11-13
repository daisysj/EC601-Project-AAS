# Convert pdfs in the current directory into text files
import convertapi
from os import listdir, stat
from sys import argv

dirs = listdir('./pdfs/')
convertapi.api_secret = '...'

for file in dirs:
    convertapi.convert('txt', {'File': file}, from_format = 'pdf').save_files('./txts/')
    