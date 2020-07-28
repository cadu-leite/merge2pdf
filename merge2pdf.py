from io import BytesIO

from PIL import Image
from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4 import PdfFileMerger
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas 


class MergeToPdf:

    def __init__(self, paths_list:list , output_file_path: str = 'outputfile.pdf'):
        '''
        A class to merge PDFs files. Pass a lista of File Paths to be merged

        Args:
            paths_list (list): a simples list of paths 
            output_file_path (str, optional): a string defining the outputpath.
        '''
        self.paths_list = paths_list
        self.output_file_path = output_file_path
    
    def _path_decople_(self, path_list_item)->tuple:
        '''
        a fucnction to decomple the FILE PATH and Page range 
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

    def merge_pdfs(self):
        '''

        '''
        merged_pdf= PdfFileMerger()
        # todo: check file type 
        for file_path in self.paths_list:
            file_name, page_range = self._path_decople_(file_path)
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                merged_pdf.append(fileobj = self._image_to_page_(file_name))
            else:
                if page_range:
                    merged_pdf.append(fileobj = file_name, pages = page_range)
                else:
                    merged_pdf.append(fileobj = file_name)

        # write to outputfile
        output = open(self.output_file_path, 'wb') # output file
        merged_pdf.write(output) # write merge content to file
        output.close() 
        merged_pdf.close()

    def _image_to_page_(self, image_path):
        #pdf = PdfFileWriter()
        # todo: image rotate if H > w
        imgTemp = BytesIO()
        imgDoc = canvas.Canvas(imgTemp, pagesize=A4) # todo: param page size
        imgDoc.drawImage(image_path, 20, 420)  # todo: param margin
        imgDoc.save()
        #pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
        #pdf.write(open("output_image.pdf","wb"))
        # return "output_image.pdf"
        return PdfFileReader(BytesIO(imgTemp.getvalue()))
