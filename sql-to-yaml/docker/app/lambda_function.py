#!/usr/bin/env python

# import the required library 
from sql_formatter.core import format_sql
import sqlparse

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
    python module 
    """)

    parser.add_argument("--file_name", help="Input file name", required=True)
    parser.add_argument("--formatter", help="Formatter module to use", required=False)

    args = parser.parse_args()

    file_name = args.file_name
    formatter = args.formatter

    if formatter:
        formatter=formatter
    else:
        formatter="sql-formatter"    

    print("Input file name              : ", file_name)
    print("formatter module             : ", formatter)

    return file_name, formatter

def process_format_sql(file_name):
    
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    output_file_name = file_name.replace(".sql","_formatted.sql")
    output_file = open(output_file_name,"w+")
    print("Output File Name             : ", output_file_name)

    with open(file_name, "r") as input_file:

        if formatter == "sql-formatter":
            formatted_sql = format_sql(input_file.read())
            output_file.write(formatted_sql)
        elif formatter == "sqlparse":
            formatted_sql = sqlparse.format(input_file.read(), reindent=True, keyword_case='upper')
            output_file.write(formatted_sql)
        else:
            print("Not a valid formatter")
        
    return input_file, output_file

def close_files(input_file, output_file):
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    
    # Print the header
    header_footer("started")

    # Parse the input
    file_name, formatter = parse_input()

    # Process the translation
    input_file, output_file = process_format_sql(file_name)

    # Print the footer
    header_footer("finished")

    # Close files
    close_files(input_file, output_file)

    sys.exit()
