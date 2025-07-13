import requests
import json

import ast  # מאפשר להמיר מחרוזת לרשימה אמיתית

from Models.Manger import manger

from  Models.Clean import clean

class Answer:
    @staticmethod
    def answer():
        dfm=manger.init_program("../files/buy_computer_data.csv")

        question = manger.get_question_check(dfm)

        dic = manger.enter_ask_enter_conditin(dfm, question)

        an = requests.get("http://127.0.0.1:8000/name/youth,medium,no,fair,no")

        list_condition = manger.enter_value(question, dfm)

        data_str = an.content.decode()

        data_dict = json.loads(data_str)

        list_str = data_dict["Hello"]

        final_list = ast.literal_eval(list_str)

        print(final_list)

        print(type(final_list))


