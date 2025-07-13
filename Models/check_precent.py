from operator import index

from rich.prompt import Prompt

from Classified import classified
from Clean import clean
import pandas as  pd
from Classified import classified
from Loader import loader

class check:
    @staticmethod
    def precent_right(df ,dic,question):

        df_check=loader.load_file('../files/computer_buy_data_check.csv')

        df_check=clean.clean_file(df_check)

        count_right=0

        list_columns_check=df_check.values.tolist()

        index_to_remov = df_check.columns.get_loc(question)

        for i in list_columns_check :
            copy = i.copy()
            copy.pop(index_to_remov)

            if classified.classified_by_input(df,dic,question,copy)==i[index_to_remov]:
                count_right+=1
        print((count_right/ df_check.shape[0]) * 100, "%")

