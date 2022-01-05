#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:15:43 2021

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
        List of filepaths that are triplicated.

    Returns
    -------
    None.

    '''
    dup_fl = Flatten(duplicated)
    dup_counter = Counter(dup_fl)
    triplicates = [(k,v) for k, v in dup_counter.items() if v>1]
    assert len(triplicates)==0, f"There are triplicates. Themove them re-run this code \n{triplicates}"
    
def find_duplicates(txt_paths, levenshtein_threshold=100):
    """
    

    Parameters
    ----------
    txt_paths : list
        List of paths to TXT files I am checking.
    levenshtein_threshold : int, optional
        Threshold to consider duplicated files. The default is 100.

    Returns
    -------
    duplicated : List of lists
        List of filepaths that are duplicated.

    """
    duplicated = []
    for txt in txt_paths:
        for txt2 in txt_paths:
            if txt==txt2:
                continue
            if sorted((txt, txt2)) in duplicated:
                # If we already have stored this pair, skip
                continue
            if abs(os.path.getsize(txt2) - os.path.getsize(txt)) > levenshtein_threshold:
                # If the length difference is greater than the threshold, skip
                continue
            if levenshtein_distance(open(txt).read(), open(txt2).read()) < levenshtein_threshold:
                duplicated.append(sorted((txt, txt2)))
    return duplicated

def main(corpus_path, levenshtein_threshold=100):
    txt_paths = list(map(lambda x: os.path.join(corpus_path, x), os.listdir(corpus_path)))
    duplicated = find_duplicates(txt_paths, levenshtein_threshold)
    find_triplicates(duplicated)
    assert len(duplicated)==0, f"There are duplicates. Deal with them before continuing \n{duplicated}"
    print("There are no duplicates")
    return txt_paths
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("--corpus", required = True, dest = "corpus_path", 
                        help = "path to input TXT corpus")
    args = parser.parse_args()
    
    main(args.corpus_path)
    #path_corpus = '/home/antonio/Documents/Work/BSC/Projects/phenotypes/annotation/available-data-to-select/txt'

