import io
import re
from konlpy.tag import Twitter
import codecs
import csv

# "."을 기준으로 문장을 나누고, 영어, 특수문자 등을 지움
def data_preprocessing():
    objects = io.open('crawled.txt', 'r', encoding='utf-8')
    with io.open('data_cleansed.txt', 'w', encoding='utf-8') as fw:
        split_word = " . ".split()

        for item in objects:
            for s in split_word:
                item = item.replace(s,'\n')

            # Extract only Korean
            item =  ''.join(re.findall(u'[\u000a\u0020\u050c\u3131-\u3163\uac00-\ud7a3]+', item))
            # print(item)
            fw.writelines(item)

# 명사만 추출
def extract_phrases_txt():
    twitter = Twitter()
    read_file = io.open('data_cleansed.txt', 'r', encoding='utf-8')
    write_file = codecs.open('phrases.txt', 'w', encoding='utf-8')
    for line in read_file:
        item = ' '.join(("{}".format(word)) for word in twitter.phrases(line))
        write_file.write(item)
        # print(item)
    read_file.close()
    write_file.close()


#구로 추출 csv로 저장
def extract_phrases_csv():
    print("\nNow extract phrases ... ")
    data = io.open('data_cleansed.txt', 'r', encoding='utf-8')
    words = list()
    tw = Twitter()
    for item in data:
        words = words + tw.phrases(item)
    print("\nNow save as csv file ... ")
    csvfile = 'phrases.csv'
    with open(csvfile, 'w', encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in words:
            writer.writerow([val])



def main():
    # print("Data preprocessing ... ")
    # data_preprocessing()
    extract_phrases_csv()

if __name__ == '__main__':
    main()