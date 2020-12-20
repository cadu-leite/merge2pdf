import unittest

from PyPDF4 import PdfFileReader

from merge2pdfs.merge2pdf import MergeToPdf
from merge2pdfs.merge2pdf import CommandError
from merge2pdfs import __main__

class TestClassMerge2PdfShellArgs(unittest.TestCase):

    def test_list_files(self):
        args = __main__.command_line_parser(['-f', 'requirements.txt', 'requirements-dev.txt'])
        self.assertEqual(args.filespath, ['requirements.txt', 'requirements-dev.txt'])

    def test_arg_outputfile(self):
        args = __main__.command_line_parser(['-f', 'requirements.txt', 'requirements-dev.txt'])
        self.assertEqual(args.output, 'merged_pdfs.pdf')

    def test_arg_other_outputfile(self):
        args = __main__.command_line_parser(['-o', 'outrooutput.pdf'])
        self.assertEqual(args.output, 'outrooutput.pdf')


class TestClassMerge2PdfParams(unittest.TestCase):

    def test_recieve_a_list_to_iter_on(self):
        '''
        assert if raise an custom error when path list not a list
        there is no sense to call if you dont have 2 files to merge
        after all
        '''
        with self.assertRaises(CommandError):
            MergeToPdf(paths_list=None)

class TestClassMerge2Pdf(unittest.TestCase):

    def test_init(self):
        '''
        '''
        image_paths = [

        ]
        m = MergeToPdf(paths_list=image_paths)

        self.assertEqual(len(image_paths), len(m.paths_list))

    def test_decomple_has_page_range(self):
        '''
        '''
        image_paths = [
            ('filepat.pdf', (0, 1)),
        ]
        m = MergeToPdf(paths_list=image_paths)
        r = m._path_decople_(image_paths[0])

        self.assertEqual(r, tuple(('filepat.pdf', (0, 1))), msg='page_range fail')

    def test_decomple_no_page_range(self):
        '''
        '''
        image_paths = [
            'filepath.pdf',
        ]
        m = MergeToPdf(paths_list=image_paths)
        r = m._path_decople_(image_paths[0])

        self.assertEqual(r, tuple(('filepath.pdf', None)))

    def test_merge_pdf_output(self):

        image_paths = [
            'tests/pdf_samples/jpeg_w_350.jpg',
            'tests/pdf_samples/pdf_sample_A Sample PDF_loremIpsum_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_b_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_dummy_w3c_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_googledocs_image_pages_02.pdf',
            ## the next PDF fail to read - invalid literal for int() with base 10: b'F-1.4' !!!
            # 'tests/pdf_samples/pdf_sample_googlesheet_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_ISO19005_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_format_FDF_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_hibrid_format_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_not_hybrid_ISO19005_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_pages_01.pdf',
            ('tests/pdf_samples/pdf_sample_readthedocs_pdf_networkdays_pages_019.pdf', (0, 2)),
            'tests/pdf_samples/pdf_sample_text_edit_macos_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_wikimedia_org_pages_01.pdf',
            'tests/pdf_samples/sample_pdf_commandline_xhtml2pdf_generated_pages_01.pdf',
            'tests/pdf_samples/issue_repo_pypdf4.pdf',
            'tests/pdf_samples/issue_repo_pypdf4_test.pdf',
        ]
        m = MergeToPdf(paths_list=image_paths, output_file_path='test_merged_pdf.pdf')
        m.merge_pdfs()
        with open('test_merged_pdf.pdf', "rb") as outputfile:
            generated_pdf = PdfFileReader(outputfile)
            pages = generated_pdf.getNumPages()

            self.assertEqual(pages, 23)

