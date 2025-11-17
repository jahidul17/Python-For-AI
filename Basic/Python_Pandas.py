
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

"""**Pandas Series**"""

#A Pandas Series is like a column in a table.
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

"""**Labels**"""

#If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

#print(myvar)
print(myvar["y"])

"""**Pandas DataFrames**"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df,"\n\n")

#refer to the row index:
print(df.loc[0])

#use a list of indexes:
print("\n")
print(df.loc[[0,1]])

"""**Named Indexes**"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

print("\n\n")

#refer to the named index:
print(df.loc["day2"])

"""**Load Files Into a DataFrame**"""

import pandas as pd

df = pd.read_csv('titanic.csv')
# df.head(10)
# df.head() #By default print 5 rows
# print(df.tail())
df.tail(10)

# print(df)

# print(df.duplicated())


#The DataFrames object has a method called info(), that gives you more information about the data set.
# df.info()


#Convert to string.
# print(df.to_string())



# Load the JSON file into a DataFrame:
# df = pd.read_json('titanic.json')
# print(df.to_string())

import pandas as pd

titanic = pd.read_csv('titanic.csv')
type(titanic["Age"])

import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic["Age"].shape

import pandas as pd

titanic = pd.read_csv('titanic.csv')
age_sex=titanic[["Age","Sex"]]
age_sex.head()

import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic[["Age","Sex"]].shape

import pandas as pd

titanic = pd.read_csv('titanic.csv')
above_35=titanic[titanic["Age"]>35]
above_35.head()

import pandas as pd

titanic = pd.read_csv('titanic.csv')
class_23=titanic[titanic["Pclass"].isin([2,3])]
class_23.head()

class_23=titanic[(titanic["Pclass"]==2) | (titanic["Pclass"]==3)]
class_23.head()

age_no_na=titanic[titanic["Age"].notna()]
age_no_na.head()

adult_names=titanic.loc[titanic["Age"]>35]
adult_names.head()

adult_names=titanic.loc[titanic["Age"]>35,"Name"]
adult_names.head()

titanic.iloc[9:25,2:5]

anon=titanic.iloc[0:3,3]="anonymous"
anon

titanic["Age"].mean() #mean called avarage

titanic[["Age","Fare"]].median()

titanic[["Age","Fare"]].describe()

titanic.agg({
    "Age":["min","max","median","skew"],
    "Fare":["min","max","median","mean"]
})

titanic[["Sex","Age"]].groupby("Sex").mean()

titanic[["Sex","Age"]].groupby("Sex").max()

titanic[["Sex","Age"]].groupby("Sex").min()

titanic[["Sex","Age"]].groupby("Sex").first()

titanic.groupby("Sex")["Age"].mean()

titanic.groupby(["Sex","Pclass"])["Fare"].mean()

titanic["Pclass"].value_counts()

titanic.groupby("Pclass")["Pclass"].count()

titanic.sort_values(by="Age",ascending=False).head()

titanic.sort_values(by="Age",ascending=True).head()

titanic.sort_values(by=["Pclass","Age"],ascending=False).head()

titanic.dtypes

titanic["Name"].str.lower()

titanic["Name"].str.split(",")

titanic["Surname"]=titanic["Name"].str.split(",").str.get(0)
titanic["Surname"]

titanic["Name_main"]=titanic["Name"].str.split(",").str.get(1)
titanic["Name_main"]

titanic["Name"].str.split(",")

titanic["Real_Name"]=titanic["Name"].str.split(",").str.get(0)
titanic.head()

titanic["Surname"]=titanic["Name"].str.split(",").str.get(1)
titanic.head()

titanic["Salutation"]=titanic["Surname"].str.split(",").str.get(0)
titanic.head()

titanic["Name"].str.contains("Mr")

titanic[titanic["Name"].str.contains("Countess")]

titanic["Name"].str.len()

titanic["Name"].str.len().idxmax()

titanic.loc[titanic["Name"].str.len().idxmax(),"Name"]

titanic["sex_short"]=titanic["Sex"].replace({"male":'M',"female":"F"})
titanic["sex_short"]

titanic["sex_short"]=titanic["Sex"].str.replace("female",'F')
titanic["sex_short"]=titanic["sex_short"].str.replace("male",'M')

titanic["sex_short"]