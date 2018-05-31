from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

fp = open('data/신의한수.xml', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
actors = []
descs = []
actor = ''
list_items = soup.select('char')

for item in list_items:
    # 문자열로 전환, 엔터 키 치환
    str_item = str(item).replace('\n', '')
    # print("item: ", str_item)

    # 중간에 탭문자가 포함된 문자열이 대사로 봄
    if '<tab>' in str_item:
        print('raw data', str_item)
        # 첫번째 나오는 탭문자 인덱스
        idx = str_item.find('<tab>')
        # print('idx', idx)

        if idx != 6:
            temp_str = str_item[6:str_item.find('<tab>')].strip()
            if temp_str != '-':
                actor = temp_str

            print('actor', actor)
        # 액터가 없는 경우, 이전 액터 사용
        actors.append(actor)
        # 대사 추출, 마지막 </char> 제외시킴.
        idx2 = str_item.rfind('</tab>')
        desc = str_item[idx2 + 6:len(str_item) - 7].strip()
        print('script', desc)
        print()
        descs.append(desc)

df = pd.DataFrame({'actor': actors, 'desc': descs})
#df.head(90)
df.to_csv('data/one_num.csv')
