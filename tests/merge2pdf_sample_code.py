from merge2pdf import MergeToPdf

if __name__ == '__main__':

    image_and_pdf_files = [
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
        'tests/pdf_samples/jpeg_w_350.jpg'
    ]

    m = MergeToPdf(paths_list=image_and_pdf_files, output_file_path='pdf_gerado.pdf')
    m.merge_pdfs()
