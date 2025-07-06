import os

from transformers import AutoModelForSequenceClassification , AutoTokenizer, pipeline
import openpyxl

model_name = "liam168/c2-roberta-base-finetuned-dianping-chinese"
class_num = 2
with open('train_yao.csv','r',encoding='gb18030') as f:
    word_list = f.readlines()
print(word_list)
_list = [s.strip() for s in word_list]
new_list = list(set(_list))
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=class_num)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
if not os.path.exists('sentimen.xlsx'):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'sentiment'
    sheet['A1']='sentence'
    sheet['B1']='label'
    workbook.save(filename='sentimen.xlsx')
workbook = openpyxl.load_workbook('sentimen.xlsx')
sheet = workbook.get_sheet_by_name('sentiment')
for i in range(len(new_list)):
    label = classifier(new_list[i])[0]['label']
    if label == 'positive':
        label=1
    else:
        label = 0
    sheet[f'A{i+2}']=new_list[i]
    sheet[f'B{i+2}']=label
    # print(label)
workbook.save('data_sentimen.xlsx')
print('写入成功')
# print(classifier('你哈珀')[0]['label'])
# classifier(ts_texts[1])


