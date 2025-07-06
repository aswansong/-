import json
import time

import requests
import re
from bs4 import BeautifulSoup
headers = {
'Cookie':'BIDUPSID=D3F5655846D67A10288E6DFCAFE76B40; PSTM=1639983699; BAIDU_WISE_UID=wapp_1645890802015_867; BAIDUID=06EE723E9BF7176FACCF4C56F96FB4A5:FG=1; BAIDUID_BFESS=06EE723E9BF7176FACCF4C56F96FB4A5:FG=1; jsdk-uuid=9631745e-37ef-4e9f-a382-e4bea519fbf5; MCITY=-%3A; __bid_n=183f3519c203a9a1f04207; FEID=v10-49c7980f6f27742ac4685bb570e1d21d2359cc92; __xaf_fpstarttimer__=1672837776149; __xaf_thstime__=1672837776217; __xaf_fptokentimer__=1672837776231; ZFY=lVnljRGGnGebrQL5ZZWhABUG22ZDRWlex17BIQenuKo:C; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1676191405,1676310360,1676892395,1678021334; USER_JUMP=-1; BAIDU_SSP_lcr=https://www.bing.com/; st_key_id=17; video_bubble3891223389=1; 3891223389_FRSVideoUploadTip=1; wise_device=0; FPTOKEN=zzfvu0XLuaDEOlyZUlkbUnVTkxpatCnivZnSIy7sNnuF5smtjTQzxfUvW3u4GhYCxq0Udj8mVULNf6ddLLBft6pGDWj9MuWx6oBoAE+PDHEx0p+TS1WTuh7oDwZZcK87m7rHmU4m8B8TFnZsxkbWKvix2PVxG6nRc2EaQSxGVoPJow+WS/8qSiPIK6dLWqnPXQfZWoWlUtCX6IED563GIKt268C0QTD9Pg5o68qJc61kOvfEnJivTeVVNgBHgLCDu7INm3+bBaZsGvIO...j43bRTLP-yfI5dbh63QfJ6hP-UyPvMWh37QmJlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHIC4e5_BDMK; H_BDCLCKID_SF_BFESS=tbIJoDK5JDD3fP36q45HMt00qxby26PDfNO9aJ5nQI5nhKIzb5jtDUL05JoObfIHM6bA-CI5QUbmjRO206oay6O3LlO83h52aC5NKl0MLPb5qKjkWxvYBUL10UnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRjj8KjjbBDHRf-b-XKD600PK8Kb7Vbnvyyfnkbft7jttjqCrbJDFe-fO_Q4nKOCopyfvq-tI73b3B5h3NJ66ZoIbPbPTTSROzMq5pQT8r5-OD3RQ23ejdKl3Rab3vOpRTXpO13fAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjttJnut_KLhf-3bfTrP-trf5DCShUFsqpolB2Q-5M-a3KtBKJ-Cb6bTbn8A2h5ZJqbpbmQ4afbmLncjSM_GKfC2jMD32tbp5-r0LeTxoUJ2bIPWMq49XqnpQptebPRiWPb9QgbP2pQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hIKmD6_bj6oM5pJfetjK2CntsJOOaCvnbKJOy4oT35L1DauLKT5ht27wXU5y-qFKSUQGyxok3h0rMxbnQjQDWJ4J5tbX0MQjDJT-Qft20b03eaAtWTvuX2Txbb7jWhvdep72yhodQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet60HJRkqoCv5b-0_HRjYbb__-P4DepbMBMRZ5m7n_l0Mf66fMRLRLUv83JkXyG5ULJQZ3mQn-UJ_KMbCMtj_D5OI5bFd3xbLalj43bRTLP-yfI5dbh63QfJ6hP-UyPvMWh37QmJlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHIC4e5_BDMK',
    'Host': 'tieba.baidu.com',
'Pragma': 'no-cache',
'Referer': 'https://tieba.baidu.com/f?kw=%E6%8A%97%E5%8E%8B%E8%83%8C%E9%94%85',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
titles = ''
hrefs = []
for n in range(60,90):
    time.sleep(1)
    page = n*50
    name ='抗压背锅'
    url =f'https://tieba.baidu.com/f?kw={name}&ie=utf-8&pn={n}'
    html = requests.get(url,headers=headers,verify=False).text
    # print(html)
    pattern1 = r'class="threadlist_lz clearfix"'
    matches1 = re.finditer(pattern1, html)
    pattern2 = r' j_thread_list clearfix thread_item_box'
    matches2 =re.finditer(pattern2, html)
    html_select = ''
    match1_sle = 1000000
    for match1,match2 in zip(matches1,matches2):
        # print(match1.start(),match2.start())
        html_select+=html[match1_sle:match2.start()]
        match1_sle = match1.start()


    soup = BeautifulSoup(html_select,'html5lib')
    results1 = soup.select('a')
    results2 = soup.select('div')

    for result in results1:
        try:
            href = result['href']
            hrefs.append(href)
            content = result['title']
            titles+=content.strip()+'\n'
        except:
            pass

print(titles,len(titles))
with open('tieba.txt','a',encoding='utf-8')as f:
    f.write(titles)