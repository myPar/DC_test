import pandas as pd
import numpy as np
import os
import re

additional_names_dict = dict({
    'МСК': 'Москва',
    'СПБ': 'Санкт-Петербург',
    'Питер': 'Санкт-Петербург',
    'Питербург': 'Санкт-Петербург',
    'НСК': 'Новосибирск',
    'Сиб': 'Новосибирск',
    'Новосиб': 'Новосибирск',
    'ЕКБ': 'Екатеринбург',
    'Нижний': 'Нижний Новгород',
    'Нижнем': 'Нижний Новгород',
    'Тагил': 'Нижний Тагил',
    'АСТ': 'Астана',
    'АЛМ': 'Алматы',
    'Семей': 'Семипалатинск'
})

datasets_dir = 'data/'
datasets_files_names = os.listdir(datasets_dir)
datasets_files_names.remove('data.csv')
countries = [name.split('_')[0] for name in datasets_files_names]


def get_country_cities_df(country_name: str):
    file_name = country_name + "_cities.csv"

    if os.path.isfile(datasets_dir + file_name):
        return pd.read_csv(datasets_dir + file_name)
    else:
        raise Exception(f"No file with such name '{file_name}' exists")


def get_all_cities_df():
    result_df = pd.DataFrame({})

    for country in countries:
        result_df = pd.concat([result_df, get_country_cities_df(country)], ignore_index=True)

    return result_df


def get_tokens(text: str):
    pattern = re.compile(r'\b[А-Яа-я]+\b')  # bounded word regex pattern

    return pattern.findall(text)


def calc_hamming_dist(string1: str, string2: str):
    len1 = len(string1)
    len2 = len(string2)

    min_len = min(len1, len2)
    max_len = max(len1, len2)
    delta = max_len - min_len
    dist = 0

    for i in range(min_len):
        if string1[i] != string2[i]:
            dist += 1

    dist += delta

    return dist
