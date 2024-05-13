import numpy as np 
import pandas as pd 
from flask import request

def change_num(number_options, number_questions):
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    options =  [abc[i] for i in range(number_options)]
    list_options = [i+1 for i in range(number_questions)]
    return options



def creation_test(number_questions, number_options, options):
    df = { i+1:[ 'O' for _ in range(number_options)] for i in range(number_questions)}
    df = pd.DataFrame(df)
    options = change_num(number_options, number_questions)
    df.index = options
    return df




# def correct_answer(df):
#     for name_col in df:
#         name_row = request.form.get('response')
#         if name_row in df.index:
#             df.loc[name_row, name_col] = 'X'
#         else:
#             while name_row  not in df[name_col].index:
#                 name_row = request.form.get(name_col)
#             df.loc[name_row, name_col] = 'X'
 

# correct_answer(df)
# print(df)