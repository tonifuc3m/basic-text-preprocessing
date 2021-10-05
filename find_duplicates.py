#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:05:14 2021

@author: antonio
"""

import os
import pandas as pd
import shutil
from datetime import datetime
import time
from Levenshtein import distance as levenshtein_distance
from collections import Counter
import argparse

def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-d", "--datapath", required = True, dest = "path", 
                        help = "path to directory with txt files")
    return parser.parse_args().path

def Flatten(ul):
    '''
    DESCRIPTION: receives a nested list and returns it flattened
    
    Parameters
    ----------
    ul: list
    
    Returns
    -------
    fl: list
    '''
    
    fl = []
    for i in ul:
        if type(i) is list:
            fl += Flatten(i)
        else:
            fl += [i]
    return fl

def find_triplicates(duplicated):
    '''
    I do not know how to deal with triplicates. Then, I have this flag 
    function. If there are triplicates, I print them and we will have to deal 
    with them

    Parameters
    ----------
    duplicated : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    dup_fl = Flatten(duplicated)
    dup_counter = Counter(dup_fl)
    triplicates = [(k,v) for k, v in dup_counter.items() if v>1]
    if len(triplicates)==0:
        print(f"There are triplicates. Deal with them before continuing \n{triplicates}")
    
def find_duplicates(final_txt, levenshtein_threshold=100):
    duplicated = []
    for txt in final_txt:
        for txt2 in final_txt:
            if txt==txt2:
                continue
            if sorted((txt, txt2)) in duplicated:
                continue
            if abs(os.path.getsize(txt2) - os.path.getsize(txt)) > 10:
                continue
            if levenshtein_distance(open(txt).read(), open(txt2).read()) < levenshtein_threshold:
                duplicated.append(sorted((txt, txt2)))
    return duplicated

if __name__ == '__main__':
    folder_path = argparser()
    file_list = os.listdir(folder_path)
    final_file_list = list(map(lambda x: os.path.join(folder_path, x), file_list))
    
    duplicated = find_duplicates(final_file_list)
    find_triplicates(duplicated)
    assert len(duplicated)==0, f"There are duplicates. Deal with them before continuing \n{duplicated}"
