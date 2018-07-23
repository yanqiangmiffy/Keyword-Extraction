import json
import csv

csv_file=open('simple_data.csv','w',encoding='utf-8',newline='')
csv_writer=csv.writer(csv_file)
headers=['index','summarization','article']
csv_writer.writerow(headers)

with open('simple_data.txt','r',encoding='utf-8') as f:
    for line in f:
        data=json.loads(line)
        csv_writer.writerow((data['index'],data['summarization'].strip(),data['article'].replace('<Paragraph>','').strip()))