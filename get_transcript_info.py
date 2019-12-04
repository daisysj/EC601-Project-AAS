import csv
import os
from os import listdir, stat

import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pdf_converter as convert

def get_transcript_info():
    convert.pdf_convert()
    dirs = listdir('./txts/')
    for file in dirs:
        path = "./txts/" + file
        if "Transcript" in file:
            file_text = open(path)
            text = ""
            grade = []
            output_lst = []
        for line in file_text:
            text = text + line
            if "," in line and "." not in line:
                output_lst.append("Student Name: " + line)
            elif "A+" in line and len(line) == 1:
                grade.append("A+")
            elif "A" in line and "." not in line and len(line) == 2:
                grade.append("A")
            elif "A-" in line and len(line) == 2:
                grade.append("A-")
            elif "B+" in line and len(line) == 2:
                grade.append("B+")
            elif "B" in line and "." not in line and len(line) == 1:
                grade.append("B")
            elif "B-" in line and len(line) == 2:
                grade.append("B-")
            elif "C+" in line and len(line) == 2:
                grade.append("C+")
            elif "C" in line and "." not in line and len(line) == 1:
                grade.append("C")
            elif "C-" in line and len(line) == 2:
                grade.append("C-")
            elif "D" in line and "." not in line and len(line) == 1:
                grade.append("D")
            elif "F" in line and "." not in line and len(line) == 1:
                grade.append("F")
        
        with open('./university courses/US Universities.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            course_count = 0
            for row in csv_reader:
                if line_count == 0:
                    output_lst.append(row["school"])
                if row["course_id"] in text:
                    output_lst.append(row["course_id"] + " " + row["title"] + " " + grade[course_count])
                    course_count += 1
                line_count += 1

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..."

        client = language.LanguageServiceClient()
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        nums = []
        entities = client.analyze_entities(document).entities
        for entity in entities:
            entity_type = enums.Entity.Type(entity.type)
            if entity_type.name == "NUMBER" and float(entity.name) >= 0 and float(entity.name) <= 4:
                nums.append(entity.name)
        #print(nums)
        output_lst.append("Cumulative GPA: " + str(nums[-1]))
        return output_lst

if __name__ == '__main__':
    output = get_transcript_info()
    print(output)

   