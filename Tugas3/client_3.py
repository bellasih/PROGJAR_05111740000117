import logging
import requests
import threading
import os


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    gambar = []
    threads = []
    gambar.extend(['https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/White-noise-mv255-240x180.png/220px-White-noise-mv255-240x180.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Highimgnoise.jpg/330px-Highimgnoise.jpg'])
    
    for i in range(len(gambar)):
        t = threading.Thread(target=download_gambar, args=(gambar[i],))
        threads.append(t)

    for thr in threads:
        thr.start()
