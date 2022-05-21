""""
Функция принимает на вход список сводной информации по абитуриентам (candidates) и возвращает список с именами 20 человек, 
набравших наибольшее СУММАРНОЕ количество баллов (с учетом extra баллов), которые станут студентами университета. 
В случае, если не получается однозначно определить 20 человек 
(например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют на 20 место в списке, 
стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""


import pandas as pd


def find_top_20():
    with open('task1/candidates.txt', 'r') as f:
        list = f.read()
    df = pd.DataFrame(eval(list))
    extended_df = pd.concat([df[x].apply(pd.Series).dropna(how='all').reset_index(drop=True) for x in df.columns],
                axis=1, keys=df.columns).dropna(how='all', axis=1)
    extended_df.columns = [tup[1] if tup[1] else tup[0] for tup in extended_df.columns]
    extended_df.loc[:,'total'] = extended_df.sum(axis=1, numeric_only=True)
    extended_df.loc[:,'profile'] = extended_df['math'] + extended_df['computer_science']
    sorted_df = extended_df.sort_values(by=['total', 'profile'], ascending=[False, False]).head(20)
    result = sorted_df['name'].tolist()
    return result


with open('task1/students.txt', 'w') as f:
        f.write(str(find_top_20()))
        f.close()
