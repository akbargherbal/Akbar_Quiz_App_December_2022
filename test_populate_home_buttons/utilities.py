from collections import defaultdict
import pandas as pd
from zipfile import ZipFile
import os
from datetime import datetime


def get_datetime_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_quiz_collection(zip_file_path, file_ext='csv'):
    zf = ZipFile(zip_file_path)
    quiz_collections  = []
    for i in zf.filelist:
        if i.filename.endswith(f'.{file_ext}'):
            quiz_collections.append(i.filename)

    return quiz_collections

    