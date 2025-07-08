import  pandas as pd
import json
buy_data=pd.read_csv("buy_computer_data.csv")


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
                if not v in dic[uniqe][columns]:
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



def print_answer(dic,list_condition):
    yes_sum=1
    no_sum=1
    count=0
    for key_no_yes,value in dic.items():
        for t in value.values():
            for x,y in t.items():
                # print(x,list_condition[count])
                if x==list_condition[count]and key_no_yes=='yes':
                    yes_sum*=y/sum(t.values())
                    # print('-yes--',yes_sum)

                elif( x==list_condition[count]and key_no_yes=='no'):
                    no_sum*=y/sum(t.values())
                    # print('--no--',no_sum)

            count+=1
        count=0
    print(no_sum,yes_sum)
    if no_sum>yes_sum:
        print('no')
    else:
        print('yes')




c=crate_table(buy_data,'Buy_Computer')

print_answer(c, ['senior', "medium", "no",'excellent'])
