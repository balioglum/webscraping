# http://docs.wand-py.org/en/0.5.9/
# http://www.imagemagick.org/script/formats.php
# brew install freetype imagemagick
# brew install PIL
# brew install tesseract
# pip3 install wand
# pip3 install pyocr
import pyocr.builders
import requests
from io import BytesIO
from PIL import Image as PI
from wand.image import Image

if __name__ == '__main__':
    pdf_url = 'https://www.vbgov.com/government/departments/city-clerk/city-council/Documents/CurrentBriefAgenda.pdf'
    req = requests.get(pdf_url)
    content_type = req.headers['Content-Type']
    modified_date = req.headers['Last-Modified']
    content_buffer = BytesIO(req.content)
    search_text = 'tourism investment program'

    if content_type == 'application/pdf':
        tool = pyocr.get_available_tools()[0]
        lang = 'eng' if tool.get_available_languages().index('eng') >= 0 else None
        image_pdf = Image(file=content_buffer, format='pdf', resolution=600)
        image_jpeg = image_pdf.convert('jpeg')

        for img in image_jpeg.sequence:
            img_page = Image(image=img)
            txt = tool.image_to_string(
                PI.open(BytesIO(img_page.make_blob('jpeg'))),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            if search_text in txt.lower():
                print('Alert! {} {} {}'.format(search_text, txt.lower().find(search_text),
                                               modified_date))

    req.close()