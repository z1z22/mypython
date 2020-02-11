import requests
import os
import time
import logging
from bs4 import BeautifulSoup
from inputdigit import inputdigit
import threading
from retrying import retry
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Download meitulu\'s pictures')


def _result(result):
    return result is None


@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
def handle_request(url, page=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    }
    if page >= 2:
        url = url + "{}.html".format(page)
    # print(url)
    r = requests.get(url=url, headers=headers, timeout=5)
    if r.status_code != 200:
        raise requests.RequestException('my_request_get error!!!!')
    r.encoding = 'utf-8'
    return r


def get_url(content):
    soup = BeautifulSoup(content, 'lxml')
    ul_ls = soup.select('.img > li')
    url_list = []
    for li in ul_ls:
        href = li.select('a > img')[0]['src']
        name = li.select('.p_title > a')[0].text
        num = li.select('p')[0].text
        img_dict = {
            'href': href,
            'name': name,
            'number': num.split()[1]
        }
        url_list.append(img_dict)
    return url_list


def zong_page(content):
    soup = BeautifulSoup(content, 'lxml')
    div = soup.select('.content > center > img')
    src_ls = []
    for img in div:
        # print(img)
        i = img['src']
        src_ls.append(i)
    return src_ls


def down_img(src, dirname, image):

    filename = os.path.basename(src)
    filepath = os.path.join(dirname, filename)
    referer = 'https://www.meitulu.com/img.html?img=' + src
    headers = {
        'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        'Referer': referer}
    r = requests.get(src, headers=headers, timeout=(3, 7))
    with open(filepath, 'wb') as fp:
        fp.write(r.content)
    logging.info('    {1}(共{0}张)下载完成.'.format(image['number'], filename))
    time.sleep(2)


def down_hander(image):
    dirpath = '/Volumes/MSDOS/pics/meitulu'
    dirname = os.path.join(dirpath, image['name'])
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    else:
        logging.info('\n{}已存在,跳过下载.\n'.format(image['name']))
        print('\n{}已存在,跳过下载.\n'.format(image['name']))
        return
    logging.info('\n {}开始下载...\n'.format(image['name']))

    for k in range(1, int(image['number']) + 1):
        img_url = image['href'][0:-5] + str(k) + '.jpg'

        down_img(src=img_url, dirname=dirname, image=image)
        time.sleep(1)

    logging.info('\n**{}下载结束.**\n'.format(image['name']))
    # print('\n**{}下载结束.**\n'.format(image['name']))
    time.sleep(2)


def main():

    url = 'https://www.meitulu.com/t/aiss/'
    # url = 'https://www.meitulu.com/guochan/'
    page = inputdigit('input download page: ')
    r = handle_request(url=url, page=page)
    url_list = get_url(r.text)
    num = 1
    for image in url_list:
        print(image['name'] + image['number'] + '--' + str(num))
        num += 1
    sp = inputdigit('Input start number: ')
    ep = inputdigit('Input end number: ')
    t_num = inputdigit('Input threading number(1-15): ')

    start_time = time.time()
    for i in range(0, (ep - sp) // t_num):
        thread_list = []
        for image in url_list[sp + i:ep:(ep - sp) // t_num]:
            # 使用多线程下载图像
            download_thread = threading.Thread(
                target=down_hander, args=[image, ])
            thread_list.append(download_thread)
            download_thread.start()
        logging.info('*' * 60 + '\n' + '第{}/{}组线程开始下载.'.format(i + 1,
                                                               (ep - sp) // t_num).center(80) + '\n' + '*' * 85)

        # 等待所有线程结束后再继续后面的主线程
        for download_thread in thread_list:
            download_thread.join()
        logging.info('#' * 60 + '\n' + '第{}/{}组线程下载结束.'.format(i + 1,
                                                               (ep - sp) // t_num).center(80) + '\n' + '#' * 85)
    use_time = round(time.time() - start_time)
    endtext = '\n全部线程下载结束(用时:{}分{}秒).\n\n'.format(
        use_time // 60, use_time % 60) + '*' * 85 + '\n\n'
    logging.info(endtext)


if __name__ == '__main__':
    main()
