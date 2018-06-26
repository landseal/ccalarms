import pandas as pd
import matplotlib.pyplot as plt
import os

# create a blank dataframe to store data in
alarms = pd.DataFrame()

# walk through ccalarms to get csv files and add them to alarms dataframe
for root, dirs, files in os.walk('C:\\Users\\jsealand\\Documents\\ccalarms'):
    for i in files:
        if i[-4:] == '.csv':
            print(i)
            df = pd.read_csv(i, index_col=0)
            df = df.dropna(axis=0) # drop Nan rows
            df.index = pd.DatetimeIndex(df.index) # convert index to datetime
            alarms = alarms.append(df)

# open alarm logs file
f = open('alarmlogs.txt', 'w')

# go through the state column and find all times when it goes from 1 -> 0
for i in range(1, len(alarms.State)):
    if alarms.State.iloc[i-1] == 1 and alarms.State.iloc[i] == 0:
        print('alarm at ', alarms.index[i])
        f.write(str(alarms.index[i])+'\n')

# close alarm logs file
f.close()

# plot the state over time
alarms.plot()
plt.show()
