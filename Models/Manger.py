from Clean import clean
from Models.Loader import  loader
from Training_models import training_models
from Models.Classified import classified
from Models.check_precent import check
import json


class manger:
    def __init__(self):

        self.dfm = manger.init_program("../files/buy_computer_data.csv")
        self.choice = manger.chose_whate_to_do()
        self.question = manger.get_question_check(self.dfm)
        self.dic = manger.enter_ask_enter_conditin(self.dfm, self.question)





    @staticmethod
    def chose_whate_to_do():
        print('------------------\n'
              'To ask a question to check whate the answer by statistics press 1\n'
              'Check how many percent is correct press 2 ')
        return input()

    @staticmethod
    def init_program(name):
        file=loader.load_file(name)
        return  clean.clean_file(file)

    @staticmethod
    def enter_ask_enter_conditin(file,question):
        dic=training_models.training_model_question(file,question)
        return dic


    @staticmethod
    def get_question_check(df):
        return training_models.get_question(df)

    @staticmethod
    def enter_value(que, df):
        exemple = ''
        list = []
        list_colmuns = [col for col in df.columns if col != que]
        for inp in list_colmuns:
            exemple = df[inp].unique()
            print(f" please enter  {inp} \nexeple {exemple}")
            list.append(input())

        return list


    def control_all(self):
        if   self.choice == '1':

            list_condition = manger.enter_value(self.question, self.dfm)

            answer=classified.classified_by_input(self.dfm,self.dic,self.question,list_condition)

            print(f"The highest probability is that  {self.question} it is {answer} ")

        elif self.choice=='2':

            check.precent_right(self.dfm,self.dic, self.question)
        else:
            print('unvalide inpute')


