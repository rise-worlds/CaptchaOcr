import time

import requests


def download():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Cookie': 'NuIFm04Y=1babdf0533a29e3925da35d44f9ca6c7; TS0195d947=01f2bcf907b800638e3b6dc0d85a16bfe515f54a3715f00f2a57065e6b2f5ec048e0b0a9b56891dfc4ceacff0d65a2d58f932370bebe04f9defb9e52f9b66253c3b5a9af26; JSESSIONID=0001V6v90bova32yAn2XqdOzo1m:2VE3VVHD4O; TS01ec737d=01f2bcf907cde1a977a6e142caa6803afa469ebc1315f00f2a57065e6b2f5ec048e0b0a9b527df5bad62af8a94d40814d8c463d8555d332b7a51d7a0058c8da96b02542086; resolution=2560x1440; BIGipServerWEB_RIB_pool_8100=204646592.42015.0000; TS0123203c=01f2bcf907e6999b71655096a68665fe19b1d0b61f15f00f2a57065e6b2f5ec048e0b0a9b5fc5281a1840522a666e48193a07e3bdbbf09bf26027e13ea972366ddca22d907',
        'Cache-Control': 'no-cache',
        'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Pragma': 'no-cache',
        'Referer': 'https://www.digital.peoplesbank.lk/sde.ib.web/D1moFyYsvHvK2kdRPBo2ag'
    }
    for i in range(1000):
        r = requests.get('https://www.digital.peoplesbank.lk/sde.ib.web/aVV90u6u0HQ1bQr0qYHkdF-LucmkqJS351-agQcIB8o', headers=headers)
        f = open("OCR_Dataset/{:0>4d}.jpg".format(i), 'wb')
        f.write(r.content)
        f.close()

        time.sleep(0.5)


if __name__ == '__main__':
    download()
