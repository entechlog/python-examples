#!/usr/bin/env python

# import the required library 
from google_trans_new import google_translator  

# import defaults
import os, sys, time
import argparse
import json
import socket
import datetime

def header_footer(process):
    # Display the program start time
    print('-' * 40)
    print((os.path.basename(sys.argv[0])).split('.')[0], process, " at ", time.ctime())
    print('-' * 40)
    
def parse_input():

    print('Number of arguments          :', len(sys.argv))

    # Uncomment only to debug
    # print('Argument List:', str(sys.argv))

    parser = argparse.ArgumentParser(description="""
    Uses py-translate to translate text from source to target language 
    """)

    parser.add_argument("--file_name", help="Input File Name", required=True)
    parser.add_argument("--src_lang_cd", help="Source Language Code", required=True)
    parser.add_argument("--tgt_lang_cd", help="Target Language Code", required=True)

    args = parser.parse_args()

    file_name = args.file_name
    src_lang_cd = args.src_lang_cd
    tgt_lang_cd = args.tgt_lang_cd

    print("Input File Name              : ", file_name)
    print("Source Language Code         : ", src_lang_cd)
    print("Target Language Code         : ", tgt_lang_cd)

    return file_name, src_lang_cd, tgt_lang_cd

def process_translation(file_name, src_lang_cd, tgt_lang_cd):
    
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    output_file_name = file_name.split(".")[0]  + '_' +  str(tgt_lang_cd)+ '.' + file_name.split(".")[1]
    output_file = open(output_file_name,"w+")
    print("Output File Name             : ", output_file_name)

    with open(file_name, "r") as input_file:
        for line in input_file:
            translator = google_translator()
            translation = translator.translate(line, lang_src=src_lang_cd, lang_tgt=tgt_lang_cd)
            output_file.write(translation)
            # print(translation)

    return input_file, output_file

def close_files(input_file, output_file):
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    
    # Print the header
    header_footer("started")

    # Parse the input
    file_name, src_lang_cd, tgt_lang_cd = parse_input()

    # Process the translation
    input_file, output_file = process_translation(file_name, src_lang_cd, tgt_lang_cd)

    # Print the footer
    header_footer("finished")

    # Close files
    close_files(input_file, output_file)

    sys.exit()
