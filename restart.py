from io import BytesIO, SEEK_SET, SEEK_END
import PyPDF2
import requests


# Create a class which convert PDF in
# BytesIO form
class ResponseStream(object):

    def __init__(self, request_iterator):
        self._bytes = BytesIO()
        self._iterator = request_iterator

    def _load_all(self):
        self._bytes.seek(0, SEEK_END)

        for chunk in self._iterator:
            self._bytes.write(chunk)

    def _load_until(self, goal_position):
        current_position = self._bytes.seek(0, SEEK_END)

        while current_position < goal_position:
            try:
                current_position = self._bytes.write(next(self._iterator))

            except StopIteration:
                break

    def tell(self):
        return self._bytes.tell()

    def read(self, size=None):
        left_off_at = self._bytes.tell()

        if size is None:
            self._load_all()
        else:
            goal_position = left_off_at + size
            self._load_until(goal_position)

        self._bytes.seek(left_off_at)

        return self._bytes.read(size)

    def seek(self, position, whence=SEEK_SET):

        if whence == SEEK_END:
            self._load_all()
        else:
            self._bytes.seek(position, whence)


# Merge PDFs using URL List
url_list = ['']
target_pdf_path = './Merged.pdf'
pdf_writer = PyPDF2.PdfFileWriter()

for url in url_list:
    response = requests.get(url)
    reader = PyPDF2.PdfFileReader(ResponseStream(response.iter_content(64)))

    for page in range(reader.getNumPages()):
        pdf_writer.addPage(reader.getPage(page))

# write to output file
with open(target_pdf_path, 'wb') as g:
    pdf_writer.write(g)