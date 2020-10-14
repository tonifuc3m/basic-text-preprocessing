#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:30:23 2020

@author: antonio
"""
import os
import argparse

def argparser():
    '''
    DESCRIPTION: Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-d", "--datapath", required = True, dest = "path", 
                        help = "path to directory with txt files")
    return parser.parse_args().path

def check_first_lines(root, file):
    lines = open(os.path.join(root,file)).readlines()
    c = 0
    for line in lines:
        c = c + 1
        if line[0].islower():
            print('Check file {}, line {}: {}...'.format(file, c-1, line[0:5]\
                                                         if len(line) > 5 else line))
    
if __name__ == '__main__':
    path = argparser()
    for r, d, f in os.walk(path):
        for file in f:
            if file.split('.')[-1] != 'txt':
                continue
            check_first_lines(r, file)
