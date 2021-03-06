""""
Функция принимает на вход список сводной информации по абитуриентам (candidates) и возвращает список с именами 20 человек, 
набравших наибольшее СУММАРНОЕ количество баллов (с учетом extra баллов), которые станут студентами университета. 
В случае, если не получается однозначно определить 20 человек 
(например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют на 20 место в списке, 
стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""


candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores": 2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores": 1},
 {"name": "Jeny",  "scores": {"math": 60, "russian_language": 33, "computer_science": 65}, "extra_scores": 2},
 {"name": "Sasha",  "scores": {"math": 56, "russian_language": 85, "computer_science": 67}, "extra_scores": 3},
 {"name": "Sergey",  "scores": {"math": 50, "russian_language": 92, "computer_science": 99}, "extra_scores": 0},
 {"name": "Anton",  "scores": {"math": 43, "russian_language": 19, "computer_science": 65}, "extra_scores": 1},
 {"name": "Vladimir",  "scores": {"math": 21, "russian_language": 36, "computer_science": 74}, "extra_scores": 2},
 {"name": "Misha",  "scores": {"math": 9, "russian_language": 78, "computer_science": 39}, "extra_scores": 2},
 {"name": "Hulio",  "scores": {"math": 71, "russian_language": 14, "computer_science": 89}, "extra_scores": 1},
 {"name": "James",  "scores": {"math": 15, "russian_language": 17, "computer_science": 61}, "extra_scores": 1},
 {"name": "Andrey",  "scores": {"math": 20, "russian_language": 21, "computer_science": 56}, "extra_scores": 0},
 {"name": "Artur",  "scores": {"math": 69, "russian_language": 36, "computer_science": 74}, "extra_scores": 0},
 {"name": "Vlad",  "scores": {"math": 52, "russian_language": 61, "computer_science": 25}, "extra_scores": 2},
 {"name": "Donald",  "scores": {"math": 52, "russian_language": 55, "computer_science": 66}, "extra_scores": 2},
 {"name": "Mike",  "scores": {"math": 33, "russian_language": 49, "computer_science": 57}, "extra_scores": 1},
 {"name": "Dima",  "scores": {"math": 35, "russian_language": 37, "computer_science": 30}, "extra_scores": 0},
 {"name": "Arsen",  "scores": {"math": 80, "russian_language": 63, "computer_science": 36}, "extra_scores": 0},
 {"name": "Tom",  "scores": {"math": 99, "russian_language": 72, "computer_science": 49}, "extra_scores": 0},
 {"name": "Jery",  "scores": {"math": 40, "russian_language": 100, "computer_science": 50}, "extra_scores": 1},
 {"name": "Dante",  "scores": {"math": 100, "russian_language": 40, "computer_science": 50}, "extra_scores": 1},
 {"name": "Bruce",  "scores": {"math": 1, "russian_language": 38, "computer_science": 41}, "extra_scores": 2},
 {"name": "Cerber",  "scores": {"math": 18, "russian_language": 1, "computer_science": 77}, "extra_scores": 1},
 {"name": "Artem",  "scores": {"math": 96, "russian_language": 68, "computer_science": 70}, "extra_scores": 0},
 {"name": "Boris",  "scores": {"math": 68, "russian_language": 96, "computer_science": 70}, "extra_scores": 0},
]


def find_top_20(candidates: list):
    result = []
    for items in candidates:
        total = sum(items['scores'].values()) + items['extra_scores']
        profile = items['scores']['math'] + items['scores']['computer_science']
        result.append([items['name'], total, profile])
        sort_result = sorted(result, key=lambda x: (-x[1], -x[2]))[:20]
    return [name[0] for name in sort_result] 


print(find_top_20(candidates))
