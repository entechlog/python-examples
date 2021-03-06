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

# Setup logging
import logging
import logging.config

logging.config.fileConfig(fname='log.conf')
logger = logging.getLogger(__name__)

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
        formatter="sqlparse"    

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
            formatted_sql = sqlparse.format(input_sql_file.read(), keyword_case='upper', reindent=True, reindent_aligned=True,indent_tabs=True,output_format='python',comma_first=True)
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
        
        # empty dictionary
        schema_dict = {}

        schema_dict['version'] = 2
        schema_dict['models'] = []

        model_counter = -1

        # print(full_statements)
        # Process a CREATE statement
        for individual_statement in full_statements[0].split(';'):
            # print(individual_statement)
            if "CREATE TABLE" in individual_statement or "CREATE VIEW" in individual_statement:
                object_identify_regex = r"(?i)CREATE.* \("
                object_split_regex = r"(?i)[^.(][A-Z_0-9]* *"
                object_details = re.findall(object_identify_regex, individual_statement)[0]
                object_details_list = re.findall(object_split_regex,object_details)
                # Debug Logging
                # print("object_details               : ",object_details)
                # print("object_details               : ",object_details_list)
                # print("Length of object array       : ",str(len(object_details_list)))
                valid_object_name = True
                try:
                    object_type = object_details_list[1].strip()
                    database_name = object_details_list[2].strip()
                    schema_name = object_details_list[3].strip()
                    object_name = object_details_list[-1].strip()

                    logging.info ("object_type            : {0}".format(object_type))
                    logging.info ("database_name          : {0}".format(database_name))
                    logging.info ("schema_name            : {0}".format(schema_name))
                    logging.info ("object_name            : {0}".format(object_name))

                    models_name = {'name':object_name}
                    schema_dict['models'].append(models_name)
                    model_counter = model_counter + 1
                except:
                    valid_object_name = False
                    if len(object_details_list) == 3:
                        logging.warning("DDL is missing database and schema details")
                    else:
                        logging.warning("Could not parse the object details")

                if valid_object_name:
                    # Process each attribute in a CREATE statement
                    attribute_count = 0
                    attribute_regex = r"(?i)[^, ][A-Z_0-9(),.]*"
                    sql_line_regex = r"(?i)[A-Z_0-9].*,"
                    schema_dict['models'][model_counter]['columns'] = []
                    # Identify attributes by spliting the individuals sql statements ending by comma
                    for sql_line in re.findall(sql_line_regex, individual_statement):
                        
                        logging.debug ("sql_line                     : {0}".format(sql_line))
                        
                        attribute_count = attribute_count + 1
                        attribute_details=re.findall(attribute_regex, sql_line)
                        attribute_name = attribute_details[0].strip()
                        attribute_type = attribute_details[1].strip()
                        
                        logging.debug ("attribute_details     : {0}".format(attribute_details))
                        logging.info ("attribute_name         : {0}".format(attribute_name))
                        logging.info ("attribute_type         : {0}".format(attribute_type))
                        
                        column_name = {'name':attribute_name}
                        schema_dict['models'][model_counter]['columns'].append(column_name)
    
    schema_yaml = yaml.dump(schema_dict,default_flow_style=False, sort_keys=False)
    print("schema_dict                  : ",schema_dict)    
    print("schema_yaml                  : \n",schema_yaml)    
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
