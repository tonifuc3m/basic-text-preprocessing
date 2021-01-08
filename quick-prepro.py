#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:52:49 2020

@author: antonio
Quick preprocessing for txt files
"""
import os
import argparse
import re
import unicodedata

def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-d", "--datapath", required = True, dest = "path", 
                        help = "path to directory with txt files")
    return parser.parse_args().path

def quick_prepro(file, old2new_simple, old2new_regex):
    '''
    Substitute/remove patterns in text file
    
    Parameters
    ----------
    file: str
        path to .txt file
    old2new_simple: dict
        Substitution patterns that will be dealt with str.replace() python method
        key: old pattern
        value: new pattern
    old2new_regex: dict
        Substitution patterns that will be dealt with re.sub() python method
        key: old pattern
        value: new pattern
    
    Returns
    -------
    None
    '''
    
    # Open file
    print(file)
    txt = open(os.path.join(r, file)).read()
    
    # Quick preprocessing
    for k,v in old2new_simple.items():
        txt = txt.replace(k, v) 
    for k,v in old2new_regex.items():
        txt = re.sub(k,v, txt)
        
    # Rewrite good file with NFKC Unicode
    with open(os.path.join(r, file), 'w') as f:
        f.write(unicodedata.normalize('NFKC', txt))

if __name__ == '__main__':
    path = argparser()
    
    # Define substitution dictionaries
    old2new_simple = {u'\xa0':u' ', # Substitute Latin1 non-breaking space by blankspace
                      u'\uf0fc':'', # Remove 
                      u'\uf0b7':'', # remove 
                      u'\u200c':'', # Substitute zero width non-joiner by blankspace
                      '  ':' ', # Remove double blankspaces
                      u'\t': ' ', # Substitute tabs by blankspace
                      u'”':'"', # substitute ” by "
                      u'“':'"', # substitute “ by "
                      u'’':'"'} # substitute ’ by '
                      #u'\uFFFD':' '} # Subst � by blankspace -> I am not doing this
    
    old2new_regex = {':(?=[A-Za-z])':': ', # add space after all :
                     '•(?=[A-Za-z])':'• '} # add space after all •
    
    for r, d, f in os.walk(path):
        for file in f:
            if file.split('.')[-1] != 'txt':
                continue
            quick_prepro(file, old2new_simple, old2new_regex)
