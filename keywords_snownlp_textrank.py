import pandas as pd
from snownlp import SnowNLP

data=pd.read_csv('data/simple_data.csv')

keywords=[]
for text in zip(data['summarization'],data['article']):
    text=''.join(text)
    snow=SnowNLP(text)
    keyword=snow.keywords(limit=10)
    keywords.append(' '.join(keyword))

data['keywords'] = keywords
data[['index', 'summarization', 'keywords']].to_csv('result/keywords_snownlp_textrank.csv', index=False,
                                                        header=['index', 'summarization', 'keywords'])