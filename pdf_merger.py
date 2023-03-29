import PyPDF2
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-n', '--name', metavar='name', help='name of the file', required=True)
parser.add_argument('-p', '--path', metavar='path', help='path for the pdf files', required=False)

if __name__ == "__main__":
    # parsing command line arguments
    args = parser.parse_args()
    path = args.path
    file_name = args.name

    # if path doesn't exist, set path to the current directory
    if not path:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)

    # creating merger object and combining the pdfs in the directory
    merger = PyPDF2.PdfMerger()
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            print("adding this file to the combined pdf: %s" % file)
            merger.append(file)
    merger.write(file_name + ".pdf")
    print("Final pdf has been written to this path: %s" % path)
