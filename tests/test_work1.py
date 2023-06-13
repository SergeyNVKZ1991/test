from unittest import TestCase 
from work1 import get_company_max_sales, get_list_geo_logs_rus, get_list_unique_numbers

class TestGetGeoLogsRus(TestCase):
    def setUp(self):
        self.list_input = [
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
        self.list_output = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 
'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
    
    def test_type(self):
        result = get_list_geo_logs_rus(self.list_input)
        self.assertEqual(type(result), list)

    def test_count_logs(self):
        self.assertEqual(len(get_list_geo_logs_rus(self.list_input)), 6)
    
    def test_correct_answer(self):
        self.assertEqual(get_list_geo_logs_rus(self.list_input), self.list_output)

class TestGetCompMaxSales(TestCase):
    def setUp(self):
        self.dict_input = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        self.true_answer = 'yandex'

    def test_name_company(self):
        self.assertEqual(get_company_max_sales(self.dict_input), self.true_answer)

class TestUniqNumbers(TestCase):
    def setUp(self):
        self.dict_input = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]
               }
        self.true_list = [98, 35, 213, 15, 54, 119]
        
    def test_uniq_numbers(self):
        self.assertEqual(len(get_list_unique_numbers(self.dict_input)), len(self.true_list))
        for i in self.true_list:
            self.assertIn(i, get_list_unique_numbers(self.dict_input))
    
    
        