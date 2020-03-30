import requests
url = 'http://www.chitumm.net/forum.php'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'Connection': 'keep-alive',
    'Cookie': 'dialogs=hide; Hm_lvt_e88802ce5dc34c05147f549c8161c0c2=1585460213,1585460889,1585461078; p_h5_u=68104CD1-0230-4231-B6BB-295F2D729E64; ZNb8_2132_sid=xi4SCe; ZNb8_2132_saltkey=FIMBbGGg; ZNb8_2132_lastvisit=1585469898; ZNb8_2132_seccode=7171.3aa13a07e1a517a12e; ZNb8_2132_ulastactivity=71e2K6dQ2x6d8a4TRcCDsPp2gay%2FWVqHuekyD7AyjTL1Eih8dejl; ZNb8_2132_auth=0acd1BkJEVRkvz%2BErjYPykeUt%2BLk42gFObrYYVfFXIOkP9K6DQP6b9dlWAFTtuNfIYoH3mnXruw1O1xckmH3lT4RdA; ZNb8_2132_lastcheckfeed=23318%7C1585473533; ZNb8_2132_lip=111.205.14.43%2C1585473150; ZNb8_2132_nofavfid=1; ZNb8_2132_lastact=1585474188%09forum.php%09; ZNb8_2132_onlineusernum=191; Hm_lpvt_e88802ce5dc34c05147f549c8161c0c2=1585474189',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69'
}
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
with open('data/h.html','w') as f:
    f.write(r.text)





