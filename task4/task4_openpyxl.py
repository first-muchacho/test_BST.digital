"""
Функция make_report_about_top3 принимает словарь (students_avg_scores), в котором ключами являются имена студентов, а значениями — средний балл за всю учебу. 
Функция находит ТОП-3 студентов, чей средний балл выше, чем у других. 
Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который потом будет передан в бухгалтерию. 
Сам файл необходимо создать внутри функции. Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без проблем получить всю нужную информацию.
"""


import openpyxl as op


students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(students_avg_scores: dict):
    legasy = list(sorted(students_avg_scores.items(), key=lambda x: -x[1])[:3])
    return legasy


wb = op.Workbook()
sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Points'
for sheets in wb.worksheets:
    for row in make_report_about_top3(students_avg_scores):
        sheets.append(row)
wb.save('task4/legasy.xlsx')
