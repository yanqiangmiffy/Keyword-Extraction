import pandas as pd
import jieba.analyse

data=pd.read_csv('data/simple_data.csv')

jieba.analyse.set_stop_words('data/stop_words.txt') # 设置停用词路径
keywords=[]
for text in zip(data['summarization'],data['article']):
    text=''.join(text)
    keyword=jieba.analyse.textrank(text,topK=10,allowPOS=['n','nz','v','vd','vn','l','a','d'])
    keywords.append(' '.join(keyword))
data['keywords']=keywords
data[['index','summarization','keywords']].to_csv('result/keywords_jieba_textrank.csv',index=False,header=['index','summarization','keywords'])