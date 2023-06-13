geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def get_list_geo_logs_rus(other_list):
    geo_logs_rus = []
    for i in other_list:
        for value in i.values():
            if value[1] == 'Россия':
                geo_logs_rus.append(i)
    return geo_logs_rus	

def get_list_unique_numbers(other_list):
    return list(set(other_list['user1']) | set(other_list['user2']) | set(other_list['user3']))

def get_company_max_sales(other_dict):
    max_value = max(other_dict.values())
    for i, value in other_dict.items():
        if value == max_value:
            return i 

    