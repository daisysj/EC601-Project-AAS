from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six
import pdf_converter as convert

import os
from os import listdir, stat

def analyze_sentiment():
    convert.pdf_convert()
    dirs = listdir('./txts/')
    for file in dirs:
        path = "./txts/" + file
        if "Letter" in file:
            file_text = open(path)
            text = ""
            for line in file_text:
                text = text + line

            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..."
            client = language_v1.LanguageServiceClient()

            content = text

            if isinstance(content, six.binary_type):
                content = content.decode('utf-8')

            type_ = enums.Document.Type.PLAIN_TEXT
            document = {'type': type_, 'content': content}

            response = client.analyze_sentiment(document)
            sentiment = response.document_sentiment
            return "Score: " + str(sentiment.score) + " Magnitude: " + str(sentiment.magnitude)

if __name__ == '__main__':
    print(analyze_sentiment())