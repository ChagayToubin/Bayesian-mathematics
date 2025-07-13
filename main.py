from itertools import count

import  pandas as pd
import json



def crate_table(df, question):
    dic = {}

    value_unic= df[question].unique()
    columns_df= [col for col in df.columns if col !=question][1:]


    for uniqe in value_unic :
        dic[uniqe]={}
        # מילוי של כל דבר במפתחות של העמודות שיש לו בטבלה חוץ ממנו כמובן
        for columns in columns_df:
            dic[uniqe][columns]={}

            uniqe_value_in_columns=df[columns].unique()
            for v in uniqe_value_in_columns:
                dic[uniqe][columns][v] = 0
            # עשכיו אני ייצר דאטה ביס חדש לפי התנאי שאני רוצה
            condition_df=df[df[question]==uniqe]
            for value_in_columns in condition_df[columns]:
                dic[uniqe][columns][value_in_columns]+=1

            #     אם יש 0 אז למלאות את כולם עוד 1
            if 0 in dic[uniqe][columns].values():
                dic[uniqe][columns] = {k: v + 1 for k, v in dic[uniqe][columns].items()}

    print(json.dumps(dic, indent=4))

    return dic



def print_answer(dic_count_main_value , dic, list_condition):


    sum_value_calculation={}
    for key in dic_count_main_value.keys():
        sum_value_calculation[key]=1

    div_by=0
    count=0
    for key_no_yes,value in dic.items():
        for t in value.values():
            for x,y in t.items():
                # print(x,list_condition[count])
                print(sum_value_calculation,x,y)
                if x==list_condition[count]:
                    # להסוי תנאי פשוט שאם זה לא שווה כמו לירך כנראה שהסויפו 1 ואז לחלק בעוד אחד מתחת
                    if sum(t.values())==dic_count_main_value[key_no_yes]:
                        div_by=sum(t.values())

                    else:
                        div_by=dic_count_main_value[key_no_yes]+1
                    sum_value_calculation[key_no_yes]*=(y/div_by)
            count+=1
        count=0

    return sum_value_calculation


def get_main_key_dic_count(df,question):
    values=df[question].unique()
    dic_count_main_question={}

    for i in values:
        dic_count_main_question[i]=df[df[question]==i].shape[0]
    return (dic_count_main_question)

buy_data=pd.read_csv("files/buy_computer_data.csv")

c=crate_table(buy_data,'Buy_Computer')

buy_data=pd.read_csv("files/buy_computer_data.csv")

dic_count_question_value =  get_main_key_dic_count(buy_data, 'Buy_Computer')

x=print_answer(dic_count_question_value, c,['senior', "medium", "no", 'excellent'] )
print(max(x.items())[0])
print(x)

