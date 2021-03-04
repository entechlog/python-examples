#!/usr/bin/env python

# import the required library 
import html2markdown  
from markdownify import markdownify as md
import tomd

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

    parser.add_argument("--file_name", help="Input file name", required=True)
    parser.add_argument("--converter", help="html to markdown converter module to use", required=False)

    args = parser.parse_args()

    file_name = args.file_name
    converter = args.converter

    if converter:
        converter=converter
    else:
        converter="markdownify"    

    print("Input file name              : ", file_name)
    print("Converter module             : ", converter)

    return file_name, converter

def process_conversion(file_name):
    
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    output_file_name = file_name.replace("html","md")
    output_file = open(output_file_name,"w+")
    print("Output File Name             : ", output_file_name)

    with open(file_name, "r") as input_file:

        if converter == "html2markdown":
            md_str = html2markdown.convert(input_file)
            output_file.write(md_str)
        elif converter == "markdownify":
            md_str = md(input_file)
            output_file.write(md_str)
        elif converter == "tomd":
            md_str = tomd.Tomd(input_file.read()).markdown
            output_file.write(md_str)
        else:
            print("Not a valid converter")
        
    return input_file, output_file

def close_files(input_file, output_file):
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    
    # Print the header
    header_footer("started")

    # Parse the input
    file_name, converter = parse_input()

    # Process the translation
    input_file, output_file = process_conversion(file_name)

    # Print the footer
    header_footer("finished")

    # Close files
    close_files(input_file, output_file)

    sys.exit()
