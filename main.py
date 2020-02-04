from urllib.request import urlopen
import requests as req
import argparse

from bs4 import BeautifulSoup

url_info = "http://www.google.co.kr/search?"

params = {
    "q": "마음의소리",
    "tbm":"isch",
    "safe":"image",
    "tbs":"ift:jpg"
}
html_object = req.get(url_info, params)

if html_object.status_code == 200:
    bs_object = BeautifulSoup(html_object.text, "html.parser")
    img_data = bs_object.find_all("img")

    for i in enumerate(img_data[1:]):
        try:
            if int(i[1].attrs["width"]) <= 100:
                continue
            t = urlopen(i[1].attrs["src"]).read()
            filename = "./images/test_" + str(i[0] + 1) + '.jpg'

            with open(filename, "wb") as f:
                f.write(t)
            print("saved as ./" + filename)
        except KeyError:
            # key doesn't exist in dic
            print('src not exist')
print('done')

