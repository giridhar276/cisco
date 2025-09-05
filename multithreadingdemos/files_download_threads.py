import logging
import threading
import time
import requests
urls = [
     'https://cdn.vox-cdn.com/thumbor/8tLchaDMIEDNzUD3mYQ7v1ZQL84=/0x0:2012x1341/920x613/filters:focal(0x0:2012x1341):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/47070706/google2.0.0.jpg',
     'https://images.ctfassets.net/mrop88jh71hl/6qzOQpqvOcO6xpSmoDYyCR/04b732ddfd0f23b45df4060752abe133/python-scripting-language-code.jpg',
     'https://images.ctfassets.net/mrop88jh71hl/1sXW5vBlU50GZ4qsw6L08D/aa565a6189e471ae0d33c5b8cb8a455b/open-source-programming-language.png',
     'https://sixfeetup.com/blog/TIOBE_Index.png',
     'https://sixfeetup.com/blog/Udemy_PythonSpeed.png',
     'https://en.wikipedia.org/wiki/Main_Page#/media/File:G%C3%B6%C4%9Fceli_Camii.JPG',
     'https://www.datasciencecentral.com/wp-content/uploads/2021/10/9430449274.png',
     'https://www.loggly.com/wp-content/uploads/2015/05/Linux-Cheat-Sheet-Sponsored-By-Loggly.pdf'
     

 ]
def download(url):
     img_data = requests.get(url).content
     img_name = url.split('/')[4]
     img_name = f'{img_name}.jpg'
     with open(img_name, 'wb') as img_file:
         img_file.write(img_data)
         print(f'downloading {img_name}')
         print("-----------------")


start = time.perf_counter()
threads = []
for i in urls:
      t = threading.Thread(target=download, args=[i])
      t.start()
      threads.append(t)
for thread in threads:
      thread.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds') 




#The two loops can be replaced with Executor() object from concurrent.futures:
#The Executor object creates a thread for each function call and blocks the main thread’s execution until each of these threads is terminated. 

import concurrent.futures
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
     executor.map(download, urls)
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds') 
