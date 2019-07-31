#!/usr/bin/env python3

'''
Month_by_Month_Total_Home_Screen_Views.csv
Month_by_Month_Total_Trainer_Page_Views.csv
Month_by_Month_Total_Workout_Detail_Views.csv
Month_by_Month_Total_Workout_List_Views.csv
Month_by_Month_Unique_Days_Viewed_Home_Screen.csv
Month_by_Month_Unique_Days_Viewed_Trainer_Page.csv
Month_by_Month_Unique_Days_Viewed_Workout_Detail.csv
Month_by_Month_Unique_Days_Viewed_Workout_List.csv
Subscribers_with_Dates_Created_Trial_Start_First_Pay_Expiration.csv
Total_Classes_Taken_Per_User_Per_Month_Post_Feb_1_2017.csv
Unique_Days_Classes_Taken_Per_User_Per_Month_Post_Feb_1_2017.csv
'''

import numpy as np
import pandas as p

total_class_details = p.DataFrame.from_csv('data_files/Month_by_Month_Total_Workout_Detail_Views.csv')
unique_class_details = p.DataFrame.from_csv('data_files/Month_by_Month_Unique_Days_Viewed_Workout_List.csv')
subscribers = p.DataFrame.from_csv('data_files/Subscribers_with_Dates_Created_Trial_Start_First_Pay_Expiration.csv')

# print(p.to_datetime(subscribers['account_created_at']))

# print(unique_class_details.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9], axis=0))

subscribers['subscription_expiration_date'] = p.to_datetime(subscribers['subscription_expiration_date'])
subscribers['first_payment_date'] = p.to_datetime(subscribers['first_payment_date'])
subscribers['months'] = subscribers['subscription_expiration_date'] - subscribers['first_payment_date']

print(subscribers['months'])


'''
f = month_on_month
print(f[1:, 2:])
activities = np.sum(f[1:, 2:], axis=1)
sorted_activities = np.sort(activities)
quartile = np.percentile(sorted_activities, np.arange(0, 100, 25))
decile = np.percentile(sorted_activities, np.arange(0, 100, 10))


print(activities)
print(sorted_activities)


print(quartile)
print(decile)

count = 0
row = 0
for i in sorted_activities:
    row = row + 1
    if i < 1:
        count = count + 1
        print(row, count)
'''
