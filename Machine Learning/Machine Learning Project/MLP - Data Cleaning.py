## In this course, we will walk through the full data science life cycle, from data cleaning and feature selection to machine learning.


## Introduction

import pandas as pd
loans_2007 = pd.read_csv('LoanStats3a.csv', skiprows=1)
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count, axis=1)
loans_2007 = loans_2007.drop(['desc', 'url'],axis=1)
loans_2007.to_csv('loans_2007.csv', index=False)


import pandas as pd
loans_2007 = pd.read_csv("loans_2007.csv")
print(loans_2007.head())
print(len(loans_2007.columns))


## First group of columns

loans_2007 = loans_2007.drop(['id','member_id','funded_amnt','funded_amnt_inv','grade', 'sub_grade','emp_title','issue_d'],axis=1)


## Second group of columns

loans_2007 = loans_2007.drop(['zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp'],axis=1)


## Third group of features

loans_2007 = loans_2007.drop(['total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt'],axis=1)


## Target column

print(loans_2007['loan_status'].value_counts())


## Binary classification

loans_2007 = loans_2007[(loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")]

status_replace = {
    "loan_status" : {
        "Fully Paid": 1,
        "Charged Off": 0,
    }
}


## Removing single value columns

drop_columns = []
for col in loans_2007.columns:
    uniq = loans_2007[col].dropna().unique()
    len_uniq = len(uniq)
    if len_uniq == 1:
        drop_columns.append(col)
loans_2007 = loans_2007.drop(drop_columns, axis = 1)

print(drop_columns)
loans_2007 = loans_2007.replace(status_replace)
