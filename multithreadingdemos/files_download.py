

import requests
import time

urls = [
     'https://cdn.vox-cdn.com/thumbor/8tLchaDMIEDNzUD3mYQ7v1ZQL84=/0x0:2012x1341/920x613/filters:focal(0x0:2012x1341):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/47070706/google2.0.0.jpg',
     'https://en.wikipedia.org/wiki/Python_(programming_language)#/media/File:Python-logo-notext.svg',
     'https://images.ctfassets.net/mrop88jh71hl/6qzOQpqvOcO6xpSmoDYyCR/04b732ddfd0f23b45df4060752abe133/python-scripting-language-code.jpg',
     'https://images.ctfassets.net/mrop88jh71hl/1sXW5vBlU50GZ4qsw6L08D/aa565a6189e471ae0d33c5b8cb8a455b/open-source-programming-language.png',
     'https://en.wikipedia.org/wiki/Main_Page#/media/File:Kevin_De_Bruyne_201807091.jpg',
     'https://en.wikipedia.org/wiki/Main_Page#/media/File:Seagram_Building_(35098307116).jpg',
     'https://en.wikipedia.org/wiki/Main_Page#/media/File:G%C3%B6%C4%9Fceli_Camii.JPG'
     

 ]

def download(url):
     img_data = requests.get(url).content
     img_name = url.split('/')[4]
     img_name = f'{img_name}.jpg'
     with open(img_name, 'wb') as img_file:
         img_file.write(img_data)
         print(f'downloading {img_name}')
         print("-----------------")

t1 = time.perf_counter()
for i in urls:
    download(i)
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds') 




