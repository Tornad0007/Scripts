import os
import hashlib
import csv



# Working : give txt file as input and result will be saved as out put || Requires hashlib csv
# Function to identify the hash type of the input string
def identify_hash_type(input_string):
    hash_types = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    for hash_type in hash_types:
        if len(input_string) == hashlib.new(hash_type).digest_size*2:
            return hash_type
    return None

# Function to convert hash into SHA256 format
def convert_to_sha256(input_string, input_hash_type):
    if input_hash_type is None:
        return None
    try:
        input_hash = getattr(hashlib, input_hash_type)(input_string.encode()).hexdigest()
        sha256_hash = hashlib.sha256(input_hash.encode()).hexdigest()
        return sha256_hash
    except AttributeError:
        return None

# Function to process the input file
# Function to process the input file
def process_file(input_file):
    with open(input_file, 'rt') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader) # skip the header row
        output = []
        for row in reader:
            input_hash = row[0].strip()
            input_hash_type = identify_hash_type(input_hash)
            sha256_hash = convert_to_sha256(input_hash, input_hash_type)
            if sha256_hash is not None:
                output.append([input_hash, input_hash_type, sha256_hash])
        return output



# Function to write the output to a CSV file
def write_to_csv(output_data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Original Hash', 'Identified Hash Type', 'SHA256 Hash'])
        for row in output_data:
            writer.writerow(row)

# Main function
if __name__ == '__main__':
    input_file = input("Enter the input file name: ")
    output_file = os.path.join(os.getcwd(), "output.csv")
    output_data = process_file(input_file)
    write_to_csv(output_data, output_file)
    print("Done! Output file saved to", output_file)
