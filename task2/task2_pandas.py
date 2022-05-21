"""
Функция get_inductees принимает 3 списка одинаковой длины. В первом списке (names) — имена студентов, позволяющие их точно идентифицировать. 
Во втором (birthday_years) — год рождения. В третьем (genders) — пол студента. Частично они отсутствуют ввиду испорченного листа бумаги. 
Функция возвращает список с именами студентов мужского пола, которые достигли или могут достигнуть 18 лет в 2021 году, но при этом не старше 30 лет. 
Cтуденты, по которым невозможно точно установить - попадают они в список или нет (из-за порчи данных), должны быть выведены отдельно.       
"""


import pandas as pd


def get_inductees():
    df = pd.read_csv('task2/students.csv')
    coffee_student = df.loc[(df['birthday_years'].isin(['None'])) | (df['genders'].isin(['None']))]
    clear_df = df.mask(df.eq('None')).dropna()
    military = clear_df.loc[(pd.to_numeric(clear_df['birthday_years']) >= 1991) & (pd.to_numeric(clear_df['birthday_years']) < 2003) & (clear_df['genders'].isin(['Male']))]
    result = pd.DataFrame()
    result.loc[:,'coffee_student'] = coffee_student['names'].reset_index(drop=True)
    result.loc[:,'military'] = military['names'].reset_index(drop=True)
    return result


get_inductees().to_csv('task2/military_coffee-stud.csv', index=False)
