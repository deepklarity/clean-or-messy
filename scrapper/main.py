import time
import pandas as pd

import urllib.request
import requests

from PIL import Image
from io import BytesIO
from selenium import webdriver

from config import *

DRIVER_PATH = chromedriver_path
wd = webdriver.Chrome(executable_path = DRIVER_PATH)

def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    wd.get(search_url.format(q=query))
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        for img in thumbnail_results[results_start:number_results]:
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))
            image_count = len(image_urls)
            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")
        results_start = len(thumbnail_results)
    return image_urls

print("Starting scrape from the given query files ")

df = pd.read_csv(query_file_path)
for ind in df.index:
    q = df['keyword'][ind]
    print("Selected keyword " + q)
    n = df['no'][ind]
    print("Number of pictures downloading for the keyword "+str(n))
    images = fetch_image_urls(q,n,wd)
    print("Image URLS fetched for the keyword")
    i = 0
    x = df['pwidth'][ind]
    y = df['pheight'][ind]
    print("The resolution of the images ("+ str(x)+","+str(y)+")")
    try:
        for url in images:
            i = i+1
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            newsize = (x,y)
            img = img.resize(newsize)
            img.save(download_path+q+"_"+str(i)+".jpeg","JPEG")
        print('Download Complete for keyword : '+q)

        i = 0
    except:
        print("Error occured while fetching for the keyword : "+q)
        continue
