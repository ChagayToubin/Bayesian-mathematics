from statistics import quantiles

import pandas as pd

from Clean import clean
from Loader import  loader
from Training_models import training_models
from Classified import classified
import json


class manger:

    @staticmethod
    def chose_whate_to_do():
        print('------------------\n'
              'To ask a question to check whate the answer by statistics press 1\n'
              'Check how many percent is correct press 2 ')
        return input()

    @staticmethod
    def init_program():
        file=loader.load_file()
        return  clean.clean_file(file)

    @staticmethod
    def enter_ask_enter_conditin(file,question):
        dic=training_models.training_model_question(file,question)
        return dic


    @staticmethod
    def get_question_check(df):
        return training_models.get_question(df)

    @staticmethod
    def control_all():
        file=manger.init_program()
        choice=manger.chose_whate_to_do()

        if   choice == '1':

            question=manger.get_question_check(file)

            dic=manger.enter_ask_enter_conditin(file,question)

            answer=classified.classified_by_input(file,dic,question)

            print(answer)




        #
        # elif choice=='2':
        #     print('ss')
        # else:
        #     print('unvalide inpute')



manger.control_all()