#!/usr/bin/env python

# import the required library 
import html2markdown  

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

    args = parser.parse_args()

    file_name = args.file_name

    print("Input File Name              : ", file_name)

    return file_name

def process_conversion(file_name):
    
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    output_file_name = file_name.replace("html","md")
    output_file = open(output_file_name,"w+")
    print("Output File Name             : ", output_file_name)

    with open(file_name, "r") as input_file:
        md_str = html2markdown.convert(input_file)
        output_file.write(md_str)
        # print(md_str)

    return input_file, output_file

def close_files(input_file, output_file):
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    
    # Print the header
    header_footer("started")

    # Parse the input
    file_name = parse_input()

    # Process the translation
    input_file, output_file = process_conversion(file_name)

    # Print the footer
    header_footer("finished")

    # Close files
    close_files(input_file, output_file)

    sys.exit()
