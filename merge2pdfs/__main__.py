import sys
import argparse
from merge2pdfs.merge2pdf import MergeToPdf

DESCRIPTION = '''
    Merge files into one pdf file.
'''


def command_line_parser(sys_args):
    print(f'sys args:{sys_args}')
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        '-o', '--output',
        # dest='output_file_path',
        default='merged_pdfs.pdf',
        help='Path and name to the outputfile')
    parser.add_argument(
        '-f', '--filespath',
        type=str,
        nargs='+',
        help='list of files to merge (images and PDF)')

    args = parser.parse_args(sys_args)
    return args


def main(args):
    m = MergeToPdf(args.filespath, args.output)
    m.merge_pdfs()


if __name__ == '__main__':
    args = command_line_parser(sys.argv[1:])
    print(f'args: {args}')
    main(args)
