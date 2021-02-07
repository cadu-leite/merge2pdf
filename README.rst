
*********
merge2pdf
*********


Description
===========

**merge2pdf** was created to join multiple PDF documents into 1 file.

You may pass a list of PDF documents paths and it will generate a only file as result. 

Its possible to *merge IMAGES* too. The images will be put inside a page and merged in the same order it was listed on the documents list.

Merge2pdf is capable to add a watermark to all pages as well. 

Its possible to use **merge2pdf** on command line as an application, or as  part of your code as a Python lib. 

+-------------------+---------------+--------------------+-------------+---------------------+
| Pypi Version      | Doc Status    | Test Status        | Workflow    | Downloads           |
+===================+===============+====================+=============+=====================+
|  Not built yet    |  no docs yet  |  |badge_coverage|  |  |workflow| |  Not on Pypi yet    |
+-------------------+---------------+--------------------+-------------+---------------------+


Why?
----

Imagine you have to put together a bunch of files that is part of a collection of documents, and those files are images and PDFs. 

This lib will help you to do that with a better looking and control. 

- Images are fit inside a PDF page as images.
- Documents may be merged partially - Its possible to specify which pages of each document will be merged.
- Its possible to add a watermark on every page.

The images are merged using `reportlab canvas`.

*if you have a better solution, or you can manage it to have less dependencies drop a comments or issue* ;) 



Dependencies
============
  
- io (BytesIO)
- PyPDF4
- reportlab


How to use it
=============


How to use it in shell
----------------------

... todo    


How to use it as a lib in your code
-----------------------------------

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


Contributing
============

    Feel free to participate the way you can. 

    Its OpenSource and any contribution is welcome.

- Give some feedbacks
    + how you use it
    + How easy is to use (or not!)
- You may point errors the best way you can, on the repository
- Send some code the way you can (Don't think to much, just sent it!)


-------------------------------------------------------------------------------

Descrição (pt_BR):
    * Unifica arquivos ".pdf" e arquivos de imagens em um único PDF*

-------------------------------------------------------------------------------



.. |badge_coverage| image:: https://codecov.io/gh/cadu-leite/merge2pdf/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/cadu-leite/merge2pdf
    :alt: code coverage

.. |workflow| image:: https://github.com/cadu-leite/merge2pdf/workflows/Python%20application/badge.svg
    :alt: workflow






