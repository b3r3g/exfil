#!/usr/bin/python

import sys
import logging
import time
from pathlib import Path
import pandas as pd
import argparse


if __name__ == '__main__':
    '''
    script for preprocessing books and extracting valence
    example use: python run.py -i './data/raw/' -o './data/emotion_data' -t './data/tmp'
    
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', help='input folder', required=True)
    parser.add_argument('-o', '--output_path', help='output folder', required=True)
    parser.add_argument('-t', '--temp', help='temp folder', required=True)
    parser.add_argument('-n', '--normalize', help='normalize valence results', default = True, type=bool)


    args = parser.parse_args()

    logging.basicConfig(filename=args.output_path + "/script.log", level=logging.INFO)
    logging.info('inputfolder:'  + args.input_path)
    logging.info('outputfolder: ' + args.output_path)

    # pandas test

    een_tot_tien = pd.Series(range(1,11))
    print(een_tot_tien)

    # file analysis

    i = 0

    f_results = open(args.output_path + "/script_result.txt", 'w')

    pathlist = Path(args.input_path).glob("*.*")
    for f in pathlist:
        try:
            i = i +1
            fread = open(args.input_path + "/" +  f.name, "r")
            f_results.write(str(i) + ";" + f.name + ";" + fread.readline())
            f_results.write('\n')
        except:
            logging.info("An exception occurred for file: " + f.name)    

    logging.info('finished')