class classified:
    @staticmethod
    def classified_by_input(df,dic,question):
        # ['middle_age', "high", "yes", 'fair']
        list_condition = (classified.enter_value(question,df))
            # ['senior','low','no','excellent']
            #
        dic_count_main_value=classified.get_main_key_dic_count(df,question)


        sum_value_calculation = {}
        for key in dic_count_main_value.keys():
            sum_value_calculation[key] = 1
        div_by = 0
        count = 0
        for key_no_yes, value in dic.items():
            for t in value.values():
                for x, y in t.items():
                    # print(x,list_condition[count])
                    if x == list_condition[count]:
                        # להסוי תנאי פשוט שאם זה לא שווה כמו לירך כנראה שהסויפו 1 ואז לחלק בעוד אחד מתחת
                        if sum(t.values()) == dic_count_main_value[key_no_yes]:
                            div_by = sum(t.values())
                        else:
                            div_by = dic_count_main_value[key_no_yes] + 1
                        sum_value_calculation[key_no_yes] *= (y/ div_by)
                count += 1
            count = 0
        print(sum_value_calculation)
        return max(sum_value_calculation, key=sum_value_calculation.get)




    @staticmethod
    def get_main_key_dic_count(df, question):
        values = df[question].unique()
        dic_count_main_question = {}

        for i in values:
            dic_count_main_question[i] = df[df[question] == i].shape[0]
        return (dic_count_main_question)

    @staticmethod
    def enter_value(que,df):
        exemple=''
        list=[]
        list_colmuns=[col for col in df.columns if col != que]
        for inp in list_colmuns:

            exemple=df[inp].unique()
            print(f" please enter  {inp} \n exeple {exemple}")
            list.append(input())

        return list



