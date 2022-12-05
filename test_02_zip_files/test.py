from zipfile import ZipFile
import os

zf = ZipFile('./QUIZ_ON_CMD.zip')

# Quiz Collections
def get_quiz_collection(zp_object):
    quiz_collections  = []
    for i in zp_object.filelist:
        if i.filename.endswith('.csv') == False:
            quiz_collections.append(i.filename)

    return quiz_collections

quiz_collections = get_quiz_collection(zf)

# List of CSV Files
def get_csv_files(zp_object):
    csv_files = []
    for i in zp_object.filelist:
        if i.filename.endswith('.csv'):
            csv_files.append(i.filename)
    return csv_files
csv_files  = get_csv_files(zf)