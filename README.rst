.. image:: https://codecov.io/gh/cadu-leite/networkdays/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/cadu-leite/networkdays
    :alt: code coverage

.. image:: https://github.com/cadu-leite/merge2pdf/workflows/Python%20application/badge.svg
    :alt: workflow passed


*********
merge2pdf
*********


Description
-----------

Merges ".pdf" and image files into one ".pdf" file.


Why?
----

Imagine you have to put together a bunch of files that is part of a processes, and those files are images, PDFs, and other docs. This little piece of code will help you to do that with a better looking not just converting images to PDF Format. 

The images are merged using `reportlab canvas`.

*if you have a better solution, or you can manage it to have less dependencies drop a comments or issue* ;) 

Dependencies
------------
  
- io (BytesIO)
- PyPDF4
- reportlab


How to use
----------

.. code-block:: python 

    from merge2pdf import MergeToPdf

    if __name__ == '__main__':
        # make a list fo PDF files and images
        image_and_pdf_files = [
            'tests/pdf_samples/pdf_sample_A Sample PDF_loremIpsum_pages_01.pdf',
            'tests/pdf_samples/sample_pdf_commandline_xhtml2pdf_generated_pages_01.pdf',
            # ...
            # ...
            # ...
            'tests/pdf_samples/issue_repo_pypdf4.pdf',
            'tests/pdf_samples/issue_repo_pypdf4_test.pdf',
            'tests/pdf_samples/jpeg_w_350.jpg'
        ]
        # instantiate a class
        m = MergeToPdf(paths_list=image_and_pdf_files, output_file_path='pdf_gerado.pdf')
        # merge.
        m.merge_pdfs()


------------------------------------------------------------

Descrição (pt_BR):
    * Unifica arquivos ".pdf" e arquivos de imagens em um único PDF*

-------------------------------------------


