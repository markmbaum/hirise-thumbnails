# %%

from bs4 import BeautifulSoup
from os import mkdir
from os.path import join, basename
import requests
import shutil
from multiprocessing import Pool
import json
# %%
# INPUT

#base url for image display pages
urlcatalog = 'https://www.uahirise.org/catalog/'
#urlcatalog = 'https://www.uahirise.org/catalog/captions/'

#where to store the data
dirout = join('..', 'data', 'non-captioned')
#dirout = join('..', 'data', 'captioned')

#image display pages
total_pages = 3049
#total_pages = 110

#base url for the individual image pages
urlimage = 'https://www.uahirise.org/'

#number of processes
nprocs = 6

# %%
# FUNCTIONS

def download_page(url):
    r = requests.get(url)
    c = r.content.decode(r.encoding)
    return(c)

soup_page = lambda url: BeautifulSoup(download_page(url), 'html.parser')

def download_image(url, dirout):
    response = requests.get(url, stream=True)
    fn = basename(url)
    with open(join(dirout, 'images', fn), 'wb') as ofile:
        shutil.copyfileobj(response.raw, ofile)    
    return(None)

def fmt(s):
    return(s.strip())

def get_text(tag):
    if tag is None:
        return('')
    else:
        return(fmt(tag.text))

def get_title(soup):
    title = soup.find('span', class_='observation-title-milo')
    if title:
        return(fmt(title.text))
    return('')

def get_caption(soup):
    cap = soup.find('div', class_='caption-text')
    if cap:
        return(fmt(cap.text))
    cap = soup.find('div', class_='caption-text-no-extras')
    if cap:
        return(fmt(cap.text)) 
    return('')

def scrape_image_page(url):
    print('scraping:', url)
    #soup the image information page
    soup = soup_page(url)
    #take the image title
    title = get_title(soup)
    #take the caption
    caption = get_caption(soup)
    #pick apart the left column of the metadata table
    els = soup.find('td', class_='product-text-alpha')
    if title and els is not None:
        els = els.contents
        els = [get_text(el) for el in els if get_text(el)]
        meta = {els[i]: els[i+1] for i in range(0,24,2)}
        for el in els[25:]:
            x, y = el.split(':')
            meta[x] = y
        meta['title'] = title
        meta['caption'] = caption
        return(meta)
    else:
        return(None)

def scrape_catalog_page(url, dirout):
    #soup the whole page structure
    print('starting page:', url)
    soup = soup_page(url)
    #get all the individual catalog cells
    cells = soup.find_all('td', class_='catalog-cell-images')
    #download thumbnails and metadata
    data = {}
    for cell in cells:
        #take the image name/code
        name = basename(cell.find('a')['href'])
        #take the metadata apart
        meta = scrape_image_page(urlimage + name)
        #download the thumbnail image and store if metadata is there
        if meta is not None:
            download_image(cell.find('img')['src'], dirout)
            data[name] = meta
    return(data)

# %%
# MAIN

if __name__ == '__main__':

    #empty the target directory and recreate it
    shutil.rmtree(dirout)
    mkdir(dirout)
    mkdir(join(dirout, 'images'))

    print('using {} processes'.format(nprocs))
    pool = Pool(nprocs)
    tasks = []
    for i in range(1, total_pages+1):
        url = urlcatalog + 'index.php?page=' + str(i)
        tasks.append(
            pool.apply_async(
                scrape_catalog_page,
                (url, dirout)
            )
        )
    #fetch all the tasks
    res = [task.get() for task in tasks]

    #merge all the dictionaries
    meta = {}
    for r in res:
        for k in r:
            meta[k] = r[k]

    #dump all the metadata into json
    p = join(dirout, 'meta_raw.json')
    with open(p, 'w') as ofile:
        json.dump(meta, ofile, indent=True)
    print('file written:', p)

# %%