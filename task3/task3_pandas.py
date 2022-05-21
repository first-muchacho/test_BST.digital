"""
Функция find_athlets принимает 3 списка с именами студентов. В первом списке (know_english) — список тех, кто хорошо владеет английским языком. 
Второй (sportsmen) — содержит имена тех, кто увлекается спортом. Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет. 
Функция возвращает список имен студентов, которые подходят под все три критерия.
"""


import pandas as pd


def find_athlets():
    df = pd.read_csv('task3/students.csv')
    result = df.loc[df['know_english'].isin(df['sportsmen']) & df['know_english'].isin(df['more_than_20_years']), 'know_english'].reset_index(drop=True)
    return result


find_athlets().to_csv('task3/champions.csv', index=False, header=False)