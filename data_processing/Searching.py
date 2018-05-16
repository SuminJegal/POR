import pandas as pd
import csv
import os
from collections import Counter
from django.conf import settings


absolute_path = os.path.dirname(__file__)
ranked_restaurant = {}

#In init
def build_restaurant():
    global seoul_restaurant
    seoul_restaurant = pd.read_csv(open(os.path.join(absolute_path, 'processed_restaurant.csv'), 'rU', encoding='UTF8'), encoding='utf-8', engine='c')

def build_metro():
    global metro
    metro = pd.read_csv(open(os.path.join(absolute_path, 'processed_metro.csv'), 'rU', encoding='UTF8'), encoding='utf-8', engine='c')

def get_words_from_csvlist():
    results = list()
    #csvfile = os.path.join(absolute_path, '도곡동_맛집_phrases.csv')
    csvfile = os.path.join(absolute_path, 'phrases_서울.csv')
    with open(csvfile, newline='', encoding='UTF8') as inputfile:
        for row in csv.reader(inputfile):
            results += row
    return results

def sorting_words_by_counting(words):
    global nnps
    nnps = pd.Series(words)
    nnps = nnps.value_counts().index

def load_restaurant_rank_file(keyword):
    folder = "restaurant_data_v1"
    csvfile = os.path.join(absolute_path, folder, keyword + '_restaurant.csv')
    print(csvfile)
    df = pd.read_csv(csvfile, converters={"counter":int}, engine='python', encoding='UTF8')
    print(df)
    ranked_restaurant[keyword] = df.sort_values(by=['counter'], ascending=False)


#In main flow
def set_keyword(input_key):
    if input_key in metro['name'].unique():
        return metro.loc[metro['name'] == input_key, 'dong'].iloc[0]
    else :
        return input_key

def pick_restaurant_using_dong_keyword(dong_keyword):
    global dong_restaurant
    try:
        dong_restaurant = seoul_restaurant.loc[seoul_restaurant['dong'] == dong_keyword, 'name']
    except:
        print("There is not dong-name in the list.")
    return dong_restaurant

def get_picked_restaurant():
    picked = list()
    for nnp in nnps:
        try:
            if '\xa0' + nnp in dong_restaurant.unique():
                picked.append(nnp)
        except:
            pass
    #print(picked)
    return picked


def initializing():
    build_restaurant()
    build_metro()
    sorting_words_by_counting(get_words_from_csvlist())

def initializing_v2():
    for key in settings.LOCATIONS:
        load_restaurant_rank_file(key)

def main_flow(location):
    pick_restaurant_using_dong_keyword(set_keyword(location))
    return get_picked_restaurant()
