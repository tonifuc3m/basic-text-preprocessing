#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:44:49 2020

@author: antonio
"""


from sentence_splitter import SentenceSplitter # recommended by jordi
import os

fout = open('out.tsv', 'w')
path = '/home/antonio/Documents/Work/BSC/corpus'
subdirs = [f.path for f in os.scandir(path) if f.is_dir()]

def split_to_sentences(text, target_lang='es'):
    '''
    DESCRIPTION: Split text into sentences.

    Parameters
    ----------
    text : string
        String with entire document.

    Returns
    -------
    sentences: list of str
        List with sentences of document

    '''  
    splitter = SentenceSplitter(language=target_lang)
    return splitter.split(text) 

def cc2tsv(r, file_, fout):
    txt = open(os.path.join(r, file_)).read()
    s = split_to_sentences(txt)
    s = list(filter(lambda x: len(x)>0, s))
    
    n_s = len(s)
    c = 0
    
    file_name = '.'.join(file_.split('.')[0:-1])
    for sentence in s:
        fout.write(file_name + '\t' + str(n_s) + '\t' + str(c) + 
                   '\t' + sentence + '\n')
        c = c + 1
    
for subdir in subdirs:
    fout = open(os.path.join(subdir, 'out.tsv'), 'w')
    for r,d,f in os.walk(subdir):
        for file_ in f:
            cc2tsv(r, file_, fout)
                
    fout.close()