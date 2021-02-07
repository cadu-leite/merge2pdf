from io import BytesIO

from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4 import PdfFileMerger

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.lib.colors import Color
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import inch

class CommandError(Exception):
    """
    """

    def __init__(self, *args, returncode=1, **kwargs):
        self.returncode = returncode
        super().__init__(*args, **kwargs)


class MergeToPdf:

    def __init__(self, paths_list: list, output_file_path: str = 'outputfile.pdf', watermak_text=''):
        '''
        A class to merge PDFs files. Pass a lista of File Paths to be merged

        Args:
            paths_list (list): a list of paths(string) ou a lists of tuples
                      like (<path[str]>, <pagerange[tuple(page_ini, page_end)]>
            output_file_path (str, optional): a string defining the outputpath.
        '''
        if not isinstance(paths_list, list):
            raise CommandError('Its not a list')

        self.paths_list = paths_list
        self.output_file_path = output_file_path
        self.watermak_text = None

    def _image_to_page_(self, image_path):
        '''
        "draw" a image inside a PDF Page

        the reason to djust not use PIL was aesthetic,
        to have an image inside a real PDF page not just an image converted to PDF

        todo: an option to rotate the image  if H > w.
        todo: an option to PDF Page Size

        Args:
            image_path (str): a path to a bitmap image file, jpeg, gif ...

        Returns:
            PdfFileReader object: its a PDF file to be merged into the result PDF.
        '''

        imgTemp = BytesIO()
        imgDoc = canvas.Canvas(imgTemp, pagesize=A4)  # todo: param page size
        imgDoc.drawImage(image_path, 20, 420)  # todo: param margin
        imgDoc.save()
        return PdfFileReader(BytesIO(imgTemp.getvalue()))

    def _path_decople_(self, path_list_item) -> tuple:
        '''
        Decomple the file path list into the FILE PATH and Page range ..

        the list could be

            [
                ('path_to_file', (pag_start, pag_ends)),
                ...
            ]

        to indicade the range of pages of a pdf to be merged

        Args:
            path_list_item ([type]): a list os files path

        Returns:
            tuple: (<fiel_path>, (<page_range_tuple>))
        '''
        if not isinstance(path_list_item, str):
            return tuple((path_list_item[0], path_list_item[1]))
        else:
            return tuple((path_list_item, None))


    def apply_watermark(self, page):
        '''
        merge a watermark text on a reportlab.page
        '''



    def merge_pdfs(self):
        '''
        merge files into a PDF

        # todo: check file type
        '''
        merged_pdf = PdfFileMerger()
        # merge files
        for file_path in self.paths_list:

            file_name, page_range = self._path_decople_(file_path)
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                merged_pdf.append(fileobj=self._image_to_page_(file_name))
            else:
                if page_range:
                    merged_pdf.append(fileobj=file_name, pages=page_range)
                else:
                    merged_pdf.append(fileobj=file_name)

        # print(f'{len(merged_pdf.pages)}')
        # write to outputfile
        output = open(self.output_file_path, 'wb')  # output file
        merged_pdf.write(output)  # write merge content to file
        output.close()
        merged_pdf.close()

        # WATERMARK
        c = canvas.Canvas('watermark.pdf')
        c.setFontSize(58)
        c.setFont('Helvetica-Bold', 58)

        PAGE_WIDTH = defaultPageSize[0]
        PAGE_HEIGHT = defaultPageSize[1]
        # print(f'{A4} , width:{PAGE_WIDTH} height:{PAGE_HEIGHT} inch:{inch}')

        red50transparent = Color(100, 0, 0, alpha=0.3)
        c.setStrokeColor((1, 0, 0))
        c.setFillColor(red50transparent)
        c.setLineWidth(1)
        c.setFont('Helvetica', 150)
        text = 'MERGED'

        # c.rect(0.2*inch,0.2*inch,PAGE_WIDTH,PAGE_HEIGHT, fill=1)
        c.rotate(45)

        c.drawCentredString(PAGE_WIDTH / 1.2, (PAGE_HEIGHT / 145), text)
        # c.rotate(45) # rotate,
        #c.showPage()
        c.save()
        watermark = PdfFileReader(open("watermark.pdf", "rb"))
        input_file = PdfFileReader(open(self.output_file_path, "rb"))
        output_file = PdfFileWriter()
        for pagenum in range(input_file.getNumPages()):
            page = input_file.getPage(pagenum)

            page.mergePage(watermark.getPage(0))
            output_file.addPage(page)
        with open('outputfile_merged_wtrmark.pdf', 'wb') as file:
            output_file.write(file)

