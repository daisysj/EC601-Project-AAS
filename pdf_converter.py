# Convert pdfs in the current directory into text files
import cloudconvert
import os
from os import listdir, stat
from sys import argv
api = cloudconvert.Api('...')

def pdf_convert():
    dirs = listdir('./pdfs/')
    for file in dirs:
        current_path = os.getcwd()
        path = current_path + "\\pdfs\\" + file 
        process = api.convert({
            "inputformat": "pdf",
            "outputformat": "txt",
            "input": "upload",
            "file": open(path, 'rb')
        })
        process.wait()
        process.downloadAll("./txts/")

if __name__ == '__main__':
    pdf_convert()