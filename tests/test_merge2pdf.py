import unittest
import datetime

from PyPDF2 import PdfFileReader

# todo: move to PyTest 

from merge2pdf import MergeToPdf

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
            ('filepat.pdf', (0,1)),
        ]
        m = MergeToPdf(paths_list=image_paths)
        r = m._path_decople_(image_paths[0])

        self.assertEqual(r, tuple(('filepat.pdf', (0,1))), msg='page_range fail' )
    
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
        import os 
        
        image_paths = [
            'tests/pdf_samples/pdf_sample_A Sample PDF_loremIpsum_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_b_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_dummy_w3c_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_googledocs_image_pages_02.pdf',
            # 'tests/pdf_samples/pdf_sample_googlesheet_pages_02.pdf', # fail to read  invalid literal for int() with base 10: b'F-1.4' !!!
            'tests/pdf_samples/pdf_sample_libreoffice_exported_ISO19005_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_format_FDF_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_hibrid_format_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_libreoffice_exported_not_hybrid_ISO19005_pages_02.pdf',
            'tests/pdf_samples/pdf_sample_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_readthedocs_pdf_networkdays_pages_019.pdf',
            'tests/pdf_samples/pdf_sample_text_edit_macos_pages_01.pdf',
            'tests/pdf_samples/pdf_sample_wikimedia_org_pages_01.pdf',
            'tests/pdf_samples/sample_pdf_commandline_xhtml2pdf_generated_pages_01.pdf',
        ]
        m = MergeToPdf(paths_list=image_paths, output_file_path='merged_pdf.pdf')
        m.merge_pdfs()
        generated_pdf = PdfFileReader(open('merged_pdf.pdf', "rb"))
        pages = generated_pdf.getNumPages()
        
        self.assertEqual(pages, 37)

