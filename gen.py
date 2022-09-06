# Script to generate SVGs from a CSV file of variables to write into a copy of the template.
import os
import zipfile
import csv

ODIR = './output'
IFILE = './files-to-create.csv'

TEMPLATE = './template.svg'


ZIP_FILE = None  # Give a file name to generate a zip file
CHECKLIST_FILE = './checklist.txt'  # Give a file name to write all names to a list


def zipdir(ofile, path):
    # ziph is zipfile handle
    zipf = zipfile.ZipFile(ofile, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))
    zipf.close()


def buildReplacementDict(readable):
    '''
    Builds a dictionary where the key is the value of the first row of the 
    column, and the values are an array of data in that column.
    '''
    csvrows = csv.reader(readable)
    data = list(csvrows)
    row_data = {}
    column_names = data.pop(0)
    for key in column_names:
        row_data[key] = []

    for row in data:
        assert(len(row) == len(column_names))
        for k in range(len(column_names)):
            row_data[column_names[k]].append(row[k])
    return row_data


def main():
    os.makedirs(ODIR, exist_ok=True)

    with open(IFILE, 'r') as f:
        replacements = buildReplacementDict(f)

    with open(TEMPLATE, 'r') as f:
        template_svg = f.read()

    master_key = list(replacements.keys())[0]

    checklist = []

    # For each individual file
    for i in range(len(replacements[master_key])):
        out_name = f'{replacements[master_key][i]}-{i}'
        output = template_svg
        for replace_key in replacements:
            output = output.replace(replace_key, replacements[replace_key][i])
        with open(os.path.join(ODIR, f'{out_name}.svg'), 'w') as f:
            checklist.append(f'{out_name}.svg')
            f.write(output)

    if ZIP_FILE is not None:
        zipdir(ZIP_FILE, ODIR)

    if CHECKLIST_FILE is not None:
        with open(CHECKLIST_FILE, 'w') as f:
            for line in checklist:
                f.write(line)
                f.write('\n')


if __name__ == '__main__':
    main()
