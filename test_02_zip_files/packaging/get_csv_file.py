from collections import defaultdict

import pandas as pd

from zipfile import ZipFile
import os

zf = ZipFile('./QUIZ_ON_CMD.zip')

def get_quiz_collection(zp_object):
    quiz_collections  = []
    for i in zp_object.filelist:
        if i.filename.endswith('.csv') == False:
            quiz_collections.append(i.filename)

    return quiz_collections

quiz_collections = get_quiz_collection(zf)

quiz_collections

# List of CSV Files
def get_csv_files(zp_object):
    csv_files = []
    for i in zp_object.filelist:
        if i.filename.endswith('.csv'):
            csv_files.append(i.filename)
    return csv_files
csv_files  = get_csv_files(zf)

# Mapping Quiz Collections to CSV Files
def create_collections_vs_quiz(quiz_collections, csv_files):
    'Map Quiz Collections to Quiz Files'
    dict_collection_vs_file = defaultdict(list)
    for quiz in quiz_collections:
        for csv_f in csv_files:
            if csv_f.startswith(quiz):
                dict_collection_vs_file[quiz].append(csv_f)
    dict_collection_vs_file = dict(dict_collection_vs_file)            
    dict_collection_vs_file = {k: sorted(v) for k,v in dict_collection_vs_file.items()}
    return dict_collection_vs_file

dict_collection_vs_file = create_collections_vs_quiz(quiz_collections, csv_files)
list_quiz_collection = list(dict_collection_vs_file)
dict_dig_vs_collection = {idx:i for (idx, i) in enumerate(list_quiz_collection)}

def open_zip_csv(idx=0, coll_no=0):
    quiz_list = dict_collection_vs_file[dict_dig_vs_collection[coll_no]]
    return pd.read_csv(zf.open(quiz_list[idx]), encoding='utf-8')