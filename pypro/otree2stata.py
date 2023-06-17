import csv
import argparse

parser = argparse.ArgumentParser(
    description='This program renames csv column headers of oTree app-data files such that they are suitable for STATA')
parser.add_argument('input_file', nargs=1)
args = parser.parse_args()

input_path = args.input_file[0]
name, postfix = input_path.split('.')
output_filename = '%s_stata.csv' % name

with open(input_path, 'r',encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    new_header = []
    for column_name in header:
        if '.' in column_name:
            prefix, name = column_name.split('.')
            if name in new_header:
                name = prefix + '_' + name
            new_header.append(name)
    data = [row for row in reader]

with open(output_filename, 'w', newline='',encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(new_header)
    writer.writerows(data)
