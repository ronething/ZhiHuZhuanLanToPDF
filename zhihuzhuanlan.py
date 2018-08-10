#coding=utf-8
import time
import re
import os
import requests
import re
from bs4 import BeautifulSoup

def get_list():
    url = 'https://www.zhihu.com/api/v4/columns/{0}/articles?\
    include=data%5B%2A%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following&limit=10&offset=0'.format(author)
    print(url)
    article_dict = {}
    while True:
        print('fetching', url)
        try:
            resp = requests.get(url, headers=headers)
            j = resp.json()
            data = j['data']
        except:
            print('get list failed')

        for article in data:
            aid = article['id']
            akeys = article_dict.keys()
            if aid not in akeys:
                article_dict[aid] = article['title']

        if j['paging']['is_end']:
            break
        url = j['paging']['next']
        time.sleep(2)

    with open('zhihu_ids.txt', 'w',encoding='utf-8') as f:
        items = sorted(article_dict.items())
        for item in items:
            f.write('%s %s\n' % item)
            
def get_html(aid, title, index):
    title = re.sub('[\/:*?"<>|]','-',title) #正则过滤非法文件字符
    print(title)
    file_name = '%03d. %s.html' % (index, title)
    if os.path.exists(file_name):
        print(title, 'already exists.')
        return
    else:
        print('saving', title)
    url = 'https://zhuanlan.zhihu.com/p/' + aid
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    try:
        content = soup.find("div",{"class":"Post-RichText"}).prettify()
    except:
        print("saving",title,"error")
        return
    content = content.replace('data-actual', '')
    content = content.replace('h1>', 'h2>')
    content = re.sub(r'<noscript>.*?</noscript>', '', content)
    content = re.sub(r'src="data:image.*?"', '', content)
    content = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body><h1>%s</h1>%s</body></html>' % (
        title, content)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.write(content)
    time.sleep(2)

def get_details():
    with open('zhihu_ids.txt','r',encoding='utf-8') as f:
        i = 1
        for line in f:
            lst = line.strip().split(' ')
            aid = lst[0]
            title = '_'.join(lst[1:])
            get_html(aid, title, i)
            i += 1
        print("done")

"""
建议别用 看不到进度条还有速度不知为何很慢
"""
def to_pdf():
    import pdfkit
    print('exporting PDF...')
    htmls = []
    for root, dirs, files in os.walk('.'):
        print(root)
        print(dirs)
        print(files)
        htmls += [name for name in files if name.endswith(".html")]
        print(htmls)
        pdfkit.from_file(sorted(htmls), author + '.pdf')
    print("done")
    
"""
直接调用 wkhtmltopdf 生成 pdf 文档
"""
def get_args():
    import pdfkit
    print('exporting PDF...')
    htmls = ""
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith(".html"):
                htmls += '"'+name+'"'+" "
        print(htmls) 
    return htmls

if __name__ == '__main__':
    author = input('Please input author name:(default vczh-nichijou)')
    if not author:
        author = 'vczh-nichijou'
    headers = {
        'origin': 'https://zhuanlan.zhihu.com',
        'referer': 'https://zhuanlan.zhihu.com/{0}'.format(author),
        'User-Agent': 'Mozilla/5.0'
    }
    get_list()
    get_details()
    pdfArgs=get_args()
    pdfEnd = 'wkhtmltopdf '+pdfArgs+author+".pdf"
    if(os.system(pdfEnd)==0):
        print("exporting PDF success")
    else:
        print("exporting PDF failed")
        
    