import requests
import inputdigit
from bs4 import BeautifulSoup
import os
import threading
import logging
import time
import random
from fake_useragent import UserAgent
from retrying import retry
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def _result(result):
    return result is None


@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
def handler_request(url, page=None):
    if page is None:
        url = url
    else:
        url = url.replace('1', str(page))
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # logging.info(url)

    r = requests.get(url=url, headers=headers, timeout=5)
    if r.status_code != 200:
        raise requests.RequestException('my_request_get error!!!!')

    return r


def picture_list(content):
    piclist = []
    soup = BeautifulSoup(content, 'lxml')
    a_ls = soup.select('dt > a')
    for a in a_ls:
        # logging.info(a.text)
        # logging.info(a['href'])
        title_dict = {'title': a.text, 'href': a['href']}
        piclist.append(title_dict)
    return piclist


def parse(text):
    soup = BeautifulSoup(text, 'lxml')
    ul_ls = soup.select('#waterfall > li')
    # logging.info(ul_ls)
    ls = []
    for ul in ul_ls:
        name = ul.select('.t')[0].text
        href = ul.select('a')[0]['href']
        # logging.info(name)
        # logging.info(href)
        url_ls = {}
        url_ls['name'] = name
        url_ls['href'] = href
        ls.append(url_ls)
    return ls


def download_img(content, dirname):
    ua = UserAgent()
    headers = {'User-Agent': ua.random,
               'Referer': 'https://www.aisinei.org/',
               }
    soup = BeautifulSoup(content, 'lxml')
    scr_ls = soup.select('.savephotop')
    if len(scr_ls) == 0:
        logging.info('Is no picture')
        os.removedirs(dirname)
        return
    else:
        for scr in scr_ls:

            scrfile = scr.select('img')[0]['zoomfile']
            imgname = scr.select('img')[0]['alt']

            logging.info(imgname + ' is downloading......')
            # logging.info(scrfile)
            r = requests.get(scrfile, headers=headers, timeout=(6, 14))
            filepath = os.path.join(dirname, imgname)
            with open(filepath, 'wb') as fb:
                fb.write(r.content)
            time.sleep(random.randint(1, 3))


def total_page(text):
    soup = BeautifulSoup(text, 'lxml')
    href = soup.select('.chked')[0]['href']

    r = handler_request(href)

    soup = BeautifulSoup(r.text, 'lxml')
    if len(soup.select('.last')) != 0:
        t_page = soup.select('.last')[0].text
    elif len(soup.select('.pg > a')) > 1:
        t_page = soup.select('.pg > a')[-2].text
    else:
        t_page = str(1)
    return t_page


def download_handler(url, page, path, title):
    r = handler_request(url, page=page)
    href_ls = parse(r.text)
    set_num = 0
    for href in href_ls:
        set_num += 1
        logging.info('Start page{}: ({}/{}) {}...'.format(page,
                                                          set_num, len(href_ls), href['name']))
        dirname = os.path.join(path, title, href['name'].replace('/', '-'))

        if not os.path.exists(dirname):
            os.makedirs(dirname)
        else:

            logging.info(
                'No.{}/{} existed..., pass!'.format(set_num, len(href_ls)))
            continue
        if ('https://www.aisinei.org' in href['href']) is False:

            href['href'] = 'https://www.aisinei.org/' + href['href']
        r = handler_request(href['href'])
        download_img(r.text, dirname)
        if os.path.exists(dirname):
            logging.info('%s is completed.\n' % href['name'])
        time.sleep(random.randint(1, 3))
    logging.info('page{} completed.\n\n'.format(page))


def main():

    url = 'https://www.aisinei.org/'
    download_path = '/Volumes/MSDOS/pics/aisinei'
    r = handler_request(url)
    pics_list = picture_list(r.text)
    num = 1
    for pics in pics_list:
        logging.info(pics['title'] + '----' + str(num))
        num += 1
    pp = inputdigit.inputdigit('Input title number: ')
    title_url = pics_list[pp - 1]['href']
    title = pics_list[pp - 1]['title']

    r = handler_request(title_url)
    t_page = total_page(r.text)
    logging.info('You will download {}, total page is {}.'.format(
        title, t_page.strip('. ')))

    sp = inputdigit.inputdigit('Input start page: ')
    ep = inputdigit.inputdigit('Input end page: ')
    t_num = inputdigit.inputdigit('Input threading:')
    ep = ep + 1
    start_time = time.time()
    for i in range(0, (ep - sp) // t_num):
        thread_list = []
        for page in range(sp + i, ep, (ep - sp) // t_num):
            # 使用多线程下载图像
            download_thread = threading.Thread(target=download_handler, args=[
                                               title_url, page, download_path, title])
            thread_list.append(download_thread)
            download_thread.start()

        logging.info('*' * 40 + '\n' + '第{}/{}组线程开始下载.'.format(i + 1,
                                                               (ep - sp) // t_num).center(60) + '\n' + '*' * 70)

        # 等待所有线程结束后再继续后面的主线程
        for download_thread in thread_list:
            download_thread.join()
        logging.info('#' * 40 + '\n' + '第{}/{}组线程下载结束.'.format(i + 1,
                                                               (ep - sp) // t_num).center(60) + '\n' + '#' * 70)

    use_time = round(time.time() - start_time)
    logging.info('All tasks completed. The code run:({}m{}s)'.format(
        use_time // 60, use_time % 60))


if __name__ == '__main__':
    main()
