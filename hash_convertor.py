#!/usr/bin/env python

import os
import hashlib
import csv

# Function to identify the hash type of the input string
def identify_hash_type(input_string):
    hash_types = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    for hash_type in hash_types:
        if len(input_string) == hashlib.new(hash_type).digest_size*2:
            return hash_type
    return None

# Function to convert hash into a given format
def convert_to_hash_format(input_string, input_hash_type, output_hash_types):
    if input_hash_type is None:
        return None
    try:
        input_hash = getattr(hashlib, input_hash_type)(input_string.encode()).hexdigest()
        output_hashes = []
        for output_hash_type in output_hash_types:
            output_hash = getattr(hashlib, output_hash_type)(input_hash.encode()).hexdigest()
            output_hashes.append(output_hash)
        return output_hashes
    except AttributeError:
        return None

# Function to process the input file
def process_file(input_file, output_hash_types):
    with open(input_file, 'rt') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader) # skip the header row
        output = []
        for row in reader:
            input_hash = row[0].strip()
            input_hash_type = identify_hash_type(input_hash)
            output_hashes = convert_to_hash_format(input_hash, input_hash_type, output_hash_types)
            if output_hashes is not None:
                output.append([input_hash, input_hash_type] + output_hashes)
        return output

# Function to write the output to a CSV file
def write_to_csv(output_data, output_file, output_hash_types):
    header_row = ['Original Hash', 'Input Hash Type'] + output_hash_types
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(header_row)
        for row in output_data:
            writer.writerow(row)

# Main function
if __name__ == '__main__':
    input_file = input("Enter the input file name: ")
    output_hash_types = input("Enter the output hash types (comma-separated): ").split(',')
    output_file = os.path.join(os.getcwd(), "output.csv")
    output_data = process_file(input_file, output_hash_types)
    write_to_csv(output_data, output_file, output_hash_types)
    print("Done! Output file saved to", output_file)

