
#Get into right directory
#cd ./Desktop/Python/Raw

#get into ipython
ipython --pylab

#Define numpy, pandas, and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the Crunchbase API as a .csv file (from their email) and remove commas in the numbers so Python sees the numbers as numeric
df = pd.read_csv('Investment.csv', thousands = ',')

#Just FYI -  List the headers
list(df2.columns.values)

#Remove rows with NA values
df2 = df.dropna()

#For conveneience, rename columns company_category_code and raised_amount_usd to catCode and rAmount, respectively
df3 = df2.rename(columns={'company_category_code' : 'catCode', ' raised_amount_usd ' : 'rAmount'})

#Get sum of each company category.
#Follows this syntax: grouped = df['data1'].groupby(df['key1'])
grouped = df3['rAmount'].groupby(df5['catCode'])
grouped
grouped.sum()

#Plot results below
done = grouped.sum()
done.plot(kind = 'barh', rot=0)


#Rename titles of cbase data:
df = df.rename(columns={'company_category_code' : 'catCode', ' raised_amount_usd ' : 'rAmount', 'funded_year' : 'fundYear', 'investor_country_code' : 'invCountry', 'company_country_code' : 'coCountryCode'})
#Create new dataframe with desired columns (so when I delete NaN rows, I don't delete too many cuz other columns have NaN)
df2 = df[['catCode', 'rAmount', 'coCountryCode']]
#Drop Na's (dropped 10990 rows from 81234 to 70244)
df2 = df2.dropna()
#Group (or Sort) columns in right order
df3 = df2.groupby(['coCountryCode', 'catCode']).sum()
#plot bar graph 
df3.plot(kind = 'barh', rot=0)


####FIX: Strangely, column headers disappear once I use groupby.
#Still graph is too big. Compare 2 countries (US & France)
states = np.array(['USA', 'USA', 'USA', 'ARG', 'ARG', 'ARG'])
category = np.array(['advertising', 'mobile', 'games_video','advertising', 'mobile', 'games_video'])
df2['rAmount'].groupby([states, category]).sum()
df2.groupby(['coCountryCode', 'catCode']).sum() #follows df['datdf.groupby(['key1', 'key2']).mean()
df.groupby(['key1', 'key2']).size()

#separate dataframe into diff. sets, organized by 1 column. Very comprehensive of sorting data
for name, group in df2.groupby('coCountryCode'):
    print name
    print group

#Sort data using multiple columns.
for (k1, k2), group in df2.groupby(['coCountryCode', 'catCode']):
    print k1, k2
    print group

#Gather all rows of a value in a column (ie: all mobile investments)
pieces = dict(list(df2.groupby('catCode')))
pieces['mobile']

#Column-wise and Multiple Function Application (p. 262)
#Import tips file
tips = pd.read_csv('tips.csv')

#create new column called tip_pct, which is tip % of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']

#Define a variable
def peak(arr):
   .....:     return arr.max() - arr.min()
grouped.agg(peak)

#Group by diff. columns sex/smoker
grouped = tips.groupby(['sex', 'smoker'])
#Pass name of fn as a string
grouped_pct = grouped['tip_pct']
#Calculate mean of tip_pct
grouped_pct.agg('mean')
#Give me std too!
grouped_pct.agg(['mean', 'std', peak])
####COOOL: Can make a fn apply to a list of columns or specific ones
#Here, I apply count, mean, and max fns to tip_pct and total_bill column
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
result
#If I just want to show the functions done to one column
result['tip_pct']
#Can also change names of columns (shown in book)

#Apply diff. functions to diff. columns
#style is -    column : function
grouped.agg({'tip' : np.max, 'size' : 'sum'})

#Give many functions to tip_pct column but 1 function to size column
grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'], 'size' : 'sum'}) 

#Return Data in 'unindexed' form
tips.groupby(['sex', 'smoker'], as_index=False).mean()

#APPLY fn
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')

#Run fn on certain columns
result = tips.groupby('smoker')['tip_pct'].describe()
result


#Fill NA (NAN) spots values (p. 270)
#Random Sampling, correlation, linear (p. 271)


#Sum up columns together and organize them by dicts (p. 257)
########### 6/5/14 Analysis  ##################
1. What have been the hottest investments in each decade?
2. What industry gets the most funding at what fundraising stage?
3. What regions invest in what industry the most?

#Out of Investment.csv file, rename and make new df
df = df.rename(columns={'company_category_code' : 'catCode', ' raised_amount_usd ' : 'rAmount', 'funded_year' : 'fundYear', 'investor_country_code' : 'invCountry', 'company_country_code' : 'coCountryCode'})
df1 = df[['catCode', 'invCountry', 'fundYear', 'rAmount']]

#Remove NaN values - reduces from 81,234 rows to 55,480 rows
df1 = df1.dropna()
df1

#Organize each catCode by their year (first, organizes by fund yr. Second, organizes by catCode)
for (k1, k2), group in df1.groupby(['fundYear', 'catCode']):
	print k1, k2
	print group

#Organize data by catCode, then fundYear amount (p. 257)
df2 = df1.groupby(['catCode', 'fundYear'])[['rAmount']].sum()
df2.plot(kind = barh)

#Remove organizing
tips.groupby('smoker', group_keys=False).apply(top)

#Fill NA (NAN) spots values (p. 270)
#Random Sampling, correlation, linear (p. 271)

#SAME THING AS ABOVE, but Pivot Tables & Cross-Tabulation
tips.pivot_table(rows=['sex', 'smoker'])

#aggregate only tip_pct and size, and additionally group by day. I’ll put smoker in the table columns and day in the rows:
tips.pivot_table(['tip_pct', 'size'], rows=['sex', 'day'], cols = 'smoker')
#Add mean to all columns at last row called ALL
tips.pivot_table(['tip_pct', 'size'], rows=['sex', 'day'], cols = 'smoker', margins = True)
#'count' or len gives me count or frequency and fill_value puts 0 in empty or Na areas
tips.pivot_table(['tip_pct'], rows=['sex', 'smoker'], cols = 'day', aggfunc = len, margins = True, fill_value = 0)



