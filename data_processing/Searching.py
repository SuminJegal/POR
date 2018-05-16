import pandas as pd
import csv
import os

#In init
def build_restaurant():
    global seoul_restaurant
    seoul_restaurant = pd.read_csv(open(os.path.join(absolute_path, 'processed_restaurant.csv'), 'rU', encoding='UTF8'), encoding='utf-8', engine='c')

def build_metro():
    global metro
    metro = pd.read_csv(open(os.path.join(absolute_path, 'processed_metro.csv'), 'rU', encoding='UTF8'), encoding='utf-8', engine='c')

def get_words_from_csvlist():
    results = list()
    with open(os.path.join(absolute_path, 'ppp.csv'), newline='', encoding='UTF8') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row[0])
    return results

def sorting_words_by_counting(words):
    global nnps
    nnps = pd.Series(words)
    nnps = nnps.value_counts().index


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

def get_picked_restaurant():
    picked = list()
    for nnp in nnps:
        try:
            if '\xa0' + nnp in dong_restaurant.unique():
                picked.append(nnp)
        except:
            pass
    print(picked)


def initializing():
    global absolute_path
    absolute_path = os.path.dirname(__file__)
    build_restaurant()
    build_metro()
    sorting_words_by_counting(get_words_from_csvlist())

def main_flow():
    pick_restaurant_using_dong_keyword(set_keyword(input_key='이태원'))
    get_picked_restaurant()

if __name__ == '__main__':
    initializing()
    main_flow()