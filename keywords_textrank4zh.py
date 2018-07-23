import pandas as pd
from textrank4zh import TextRank4Keyword, TextRank4Sentence

stop_words_file='data/stop_words.txt'
pos=['n','nz','v','vd','vn','l','a','d']
tr4w = TextRank4Keyword(stop_words_file=stop_words_file,allow_speech_tags=pos)

data=pd.read_csv('data/simple_data.csv')
keywords=[]
for text in zip(data['summarization'],data['article']):
    text=''.join(text)
    tr4w.analyze(text=text, lower=True, window=2)
    keyword=[item.word for item in tr4w.get_keywords(10, word_min_len=2)]
    keywords.append(' '.join(keyword))

    # print('关键短语：')
    # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
    #     print(phrase)
    #
    # tr4s = TextRank4Sentence()
    # tr4s.analyze(text=text, lower=True, source='all_filters')
    #
    # print()
    # print('摘要：')
    # for item in tr4s.get_key_sentences(num=3):
    #     print(item.index, item.weight, item.sentence)  # index是语句在文本中位
data['keywords']=keywords
data[['index','summarization','keywords']].to_csv('result/keywords_textrank4zh.csv',index=False,header=['index','summarization','keywords'])