#!/usr/bin/env python

# import the required library 
from sql_formatter.core import format_sql
import sqlparse

import yaml
import re

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

    print('Number of arguments          : ', len(sys.argv))

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
    print("Files in                     : %r are %s" % (cwd, files))

    output_sql_file_name = file_name.replace(".sql","_formatted.sql")
    output_sql_file = open(output_sql_file_name,"w+")
    print("Output file name             : ", output_sql_file_name)

    with open(file_name, "r") as input_sql_file:

        if formatter == "sql-formatter":
            formatted_sql = format_sql(input_sql_file.read())
            output_sql_file.write(formatted_sql)
        elif formatter == "sqlparse":
            formatted_sql = sqlparse.format(input_sql_file.read(), keyword_case='upper', reindent=True, reindent_aligned=True,indent_tabs=True,output_format='python')
            output_sql_file.write(formatted_sql)
        else:
            print("Not a valid formatter")
    
    output_sql_file.close()
    return input_sql_file, output_sql_file, output_sql_file_name

def generate_yaml(output_sql_file_name):
    
    output_yaml_file_name = file_name.replace(".sql",".yml")
    output_yaml_file = open(output_yaml_file_name,"w+")
    print("Output YAML file             : ", output_yaml_file_name)

    with open(output_sql_file_name, "r") as formatted_sql_file:
        full_statements = sqlparse.split(formatted_sql_file.read())
        # Process a CREATE statement
        for individual_statement in full_statements[0].split(';'):
            if "CREATE TABLE" in individual_statement or "CREATE VIEW" in individual_statement:
                object_regex = r"([A-Z_]*)\W+"
                object_details = re.findall(object_regex, individual_statement.split('(')[1])
                print("Object type                  : ",object_details[2])
                print("Database name                : ",object_details[3])
                print("Schema name                  : ",object_details[4])
                print("Object name                  : ",object_details[-1])
                # Process each attribute in a CREATE statement
                attribute_count = 0
                attribute_regex = r"([A-Z_a-z0-9(),]*)\W+"
                for sql_line in individual_statement.split(' ,'):
                    attribute_count = attribute_count + 1
                    attribute_details=re.findall(attribute_regex, sql_line)
                    if attribute_count > 1:
                        print("Attribute name               : ",attribute_details[1])
                        print("Type name                    : ",attribute_details[2])
        
    return output_yaml_file_name, output_yaml_file

def close_files(input_sql_file, output_sql_file, output_yaml_file):
    input_sql_file.close()
    output_sql_file.close()
    output_yaml_file.close()

if __name__ == "__main__":
    
    # Print the header
    header_footer("started")

    # Parse the input
    file_name, formatter = parse_input()

    # Process sql formating
    input_sql_file, output_sql_file, output_sql_file_name = process_format_sql(file_name)

    # Generate yaml
    output_yaml_file_name, output_yaml_file = generate_yaml(output_sql_file_name)

    # Print the footer
    header_footer("finished")

    # Close files
    close_files(input_sql_file, output_sql_file, output_yaml_file)
    

    sys.exit()
