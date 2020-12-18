import sys
import argparse
from merge2pdf import MergeToPdf

DESCRIPTION = '''
    Search for corrupted records on PostgreSQL table

'''


def command_line_parser(sys_args):
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('file', dest='paths_list', type=argparse.FileType('r'), nargs='+', help='list of files to merge (images and PDF)')
    parser.add_argument('--outputfilepath', dest='output_file_path', help='Path and name to the outputfile')
    args = parser.parse_args()
    return args


def main(sys_args):
    args = command_line_parser(sys_args)
    m = MergeToPdf(*args)
    m.merge_pdfs()


if __name__ == '__main__':
    main(sys.argv[1:])
    print('CHAMOU ')
