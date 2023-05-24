#This project focuses on statistics methods to perform descriptive analysis on the bikeshare data from 3 major U.S. cities - Chicago, Washington, and New York City
#to display information such as most popular days or most common stations.
### Date created
#23/05/2023

<<<<<<< HEAD
#Import time, pandas and numpy
import time 
import pandas as pd
import numpy as np
||||||| 015ee2e
This is the repo for [Udacity's Version Control with Git course](https://www.udacity.com/course/version-control-with-git--ud123). In the course, students will learn version control while learning the basics to intermediate knowledge of Git.
=======
## Project Title
#Bikeshare Statistics
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
chicago=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\chicago.csv")
new_york_city=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\new_york_city.csv")
washington=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\washington.csv")
||||||| 015ee2e
This repo contains the source code of a blog project that will be used throughout the course.
=======
### Description
#This project focuses on statistics methods to perform descriptive analysis on the bikeshare data from 3 major U.S. cities - Chicago, Washington, and New York City #to display information such as most popular days or most common stations.
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
||||||| 015ee2e
## Table of Contents
=======
#Import time, pandas and numpy import time import pandas as pd import numpy as np
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
def takerequest():
||||||| 015ee2e
* [Instructions](#instructions)
* [Creator](#creators)
=======
chicago=pd.read_csv("C:\Users\Jaimi\Desktop\Python\chicago.csv") new_york_city=pd.read_csv("C:\Users\Jaimi\Desktop\Python\new_york_city.csv") washington=pd.read_csv("C:\Users\Jaimi\Desktop\Python\washington.csv")
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
#Asks user to specify a city, month and day to analyze.
#Returns:
#City - name of the city to analyze
#Month - name of the month or all months to analyze
#Day - name of the day or all days to analyze
    
    print('\nHey...Let\'s explore US bikeshare data\n')
    while True:
        city = input('Select a city - lower case : chicago, new york city, washington: ').lower()
        print(CITY_DATA[city])
        if city not in CITY_DATA:
            print('Please select correct city name in lower case')
        else:
           break
        
    while True:
        month = input('Select a month from january to june - lower case OR type "all" to get data for all months: ').lower()
        print(month)
        months = ['january', 'february', 'march','april', 'may', 'june'] 
        if month != 'all' and month not in months:
            print('Please type correct month name')
        else:
            break
        
    while True:
        day = input('Enter a day of the week - lower case OR type "all" to get data for all days: ').lower()
        print(day)
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day != 'all' and day not in days:
            print('Please type correct day')
        else:
            break
    return city, month, day
    
def showdata(city, month, day):
||||||| 015ee2e
## Instructions
=======
CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
#Returns the record of city, month and day selected by the user"""
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        return df
    
def showrawdata(city):
||||||| 015ee2e
* clone the project
* open the index file in a browser
=======
def takerequest():
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
#Displays 5 records from the selected city."""
#Asks user to type 'yes' or 'no' if user wants to see more record or not"""
    
    df = pd.read_csv(CITY_DATA[city])
    answers = ['no','yes']
    user_input = ''
||||||| 015ee2e
## Creators
=======
#Asks user to specify a city, month and day to analyze. #Returns: #City - name of the city to analyze #Month - name of the month or all months to analyze #Day - name of the day or all days to analyze
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
    i = 0
||||||| 015ee2e
* Richard Kalehoff
    - [https://github.com/richardkalehoff](https://github.com/richardkalehoff)
    - [https://twitter.com/richardkalehoff](https://twitter.com/richardkalehoff)
=======
print('\nHey...Let\'s explore US bikeshare data\n')
while True:
    city = input('Select a city - lower case : chicago, new york city, washington: ').lower()
    print(CITY_DATA[city])
    if city not in CITY_DATA:
        print('Please select correct city name in lower case')
    else:
       break
    
while True:
    month = input('Select a month from january to june - lower case OR type "all" to get data for all months: ').lower()
    print(month)
    months = ['january', 'february', 'march','april', 'may', 'june'] 
    if month != 'all' and month not in months:
        print('Please type correct month name')
    else:
        break
    
while True:
    day = input('Enter a day of the week - lower case OR type "all" to get data for all days: ').lower()
    print(day)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if day != 'all' and day not in days:
        print('Please type correct day')
    else:
        break
return city, month, day
def showdata(city, month, day):
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
    while user_input not in answers:
        print("\nDisplay first 5 data records : yes/no?")
        user_input = input().lower()
||||||| 015ee2e
With the help of:
=======
#Returns the record of city, month and day selected by the user"""
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b

<<<<<<< HEAD
        if user_input == "yes":
            print(df.head())
        elif user_input not in answers:
            print("\ntype correct answer.")

    while user_input == 'yes':
        print("\nDisplay more data records?\n")
        i += 5
        user_input = input().lower()
        if user_input == "yes":
             print(df[i:i+5])
        elif user_input != "yes":
             break

def showstatsfortime(city):

#Displays stats on the most frequent times of travel"""
           
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

#Displays stats on the most popular month"""
    
    popularmonth = df['month'].mode()[0]
    print('most popular month:', popularmonth)

#Displays stats on the most popular day of the week"""
    
    popularday = df['day_of_week'].mode()[0]
    print('most popular day of the week:', popularday)

#Displays stats on the most popular hour of the day"""
    
    df['hour'] = df['Start Time'].dt.hour
    popularhour = df['hour'].mode()[0]
    print('most popular hour of the day:', popularhour)
   
    print('\n')

def showstatsforstation(city):

#Displays stats on the most popular stations and trip"""
    
    df = pd.read_csv(CITY_DATA[city])

#Displays stats on the most popular start station"""   
     
    popularstarttime = df['Start Station'].mode()[0]
    print('most popular start station:', popularstarttime)

#Displays stats on the most popular end station"""
    
    popularendtime = df['End Station'].mode()[0]
    print('most popular end station:', popularendtime)

#Displays stats on the most popular trip from start to end station"""
    
    popular_start_and_end_time = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('most popular trip from start to end:', popular_start_and_end_time)
    
def showstatsfortripduration(city):

#Displays stats on the total and average trip duration"""
    
    df = pd.read_csv(CITY_DATA[city])

#Displays stats on the total travel time for the trip"""
        
    total_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time:', total_time, ' seconds, or ', total_time/3600, ' hours')

#Displays stats on the average travel time for the trip"""
     
    avg_time = df['Trip Duration'].mean()
    print('Average travel time:', avg_time, ' seconds, or ', avg_time/3600, ' hours')
     
    print('\n')

def showstatsforuser(city):

#Displays stats on bikeshare users"""
   
    df = pd.read_csv(CITY_DATA[city])

#Displays count of each user types"""
        
    print('Counts of each user type:\n', df['User Type'].value_counts());

#Displays count of each gender"""
    
    if 'Gender' in df:
        print('Counts of each gender:\n', df['Gender'].value_counts())

#Displays earliest birth year, recent birth year and popular birth year"""
        
    if 'Birth Year' in df:
        earliestbirthyear = int(df['Birth Year'].min())
        print('\n Earliest birth year :\n', earliestbirthyear)
        recentbirthyear = int(df['Birth Year'].max())
        print('\n most recent birth year:\n', recentbirthyear)
        popularbirthyear = int(df['Birth Year'].mode()[0])
        print('\n Most common year of birth:\n', popularbirthyear)
        
        print('\n')        
               
def main():
    while True:
        city, month, day = takerequest ()
        df = showdata (city, month, day)
        showrawdata (city)
        showstatsfortime (city)
        showstatsforstation (city)
        showstatsfortripduration(city)
        showstatsforuser (city)

#Asks user if user wants to start analysis again?"""
        
        repeat = input('\nStart again?: yes or no:\n')
        if repeat.lower() == 'no':
            break
          
if __name__ == "__main__":
   main()
||||||| 015ee2e
* Colt
* James
* Julia
=======
df = pd.read_csv(CITY_DATA[city])

df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.day_name()

if month != 'all':
    months = ['january','february','march','april','may','june']
    month = months.index(month) + 1
    
    df = df[df['month'] == month]
    
if day != 'all':
    df = df[df['day_of_week'] == day.title()]
    return df
def showrawdata(city):

#Displays 5 records from the selected city.""" #Asks user to type 'yes' or 'no' if user wants to see more record or not"""

df = pd.read_csv(CITY_DATA[city])
answers = ['no','yes']
user_input = ''

i = 0

while user_input not in answers:
    print("\nDisplay first 5 data records : yes/no?")
    user_input = input().lower()

    if user_input == "yes":
        print(df.head())
    elif user_input not in answers:
        print("\ntype correct answer.")

while user_input == 'yes':
    print("\nDisplay more data records?\n")
    i += 5
    user_input = input().lower()
    if user_input == "yes":
         print(df[i:i+5])
    elif user_input != "yes":
         break
def showstatsfortime(city):

#Displays stats on the most frequent times of travel"""

df = pd.read_csv(CITY_DATA[city])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.day_name()
#Displays stats on the most popular month"""

popularmonth = df['month'].mode()[0]
print('most popular month:', popularmonth)
#Displays stats on the most popular day of the week"""

popularday = df['day_of_week'].mode()[0]
print('most popular day of the week:', popularday)
#Displays stats on the most popular hour of the day"""

df['hour'] = df['Start Time'].dt.hour
popularhour = df['hour'].mode()[0]
print('most popular hour of the day:', popularhour)

print('\n')
def showstatsforstation(city):

#Displays stats on the most popular stations and trip"""

df = pd.read_csv(CITY_DATA[city])
#Displays stats on the most popular start station"""

popularstarttime = df['Start Station'].mode()[0]
print('most popular start station:', popularstarttime)
#Displays stats on the most popular end station"""

popularendtime = df['End Station'].mode()[0]
print('most popular end station:', popularendtime)
#Displays stats on the most popular trip from start to end station"""

popular_start_and_end_time = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
print('most popular trip from start to end:', popular_start_and_end_time)
def showstatsfortripduration(city):

#Displays stats on the total and average trip duration"""

df = pd.read_csv(CITY_DATA[city])
#Displays stats on the total travel time for the trip"""

total_time = df['Trip Duration'].sum()
print('\nTotal Travel Time:', total_time, ' seconds, or ', total_time/3600, ' hours')
#Displays stats on the average travel time for the trip"""

avg_time = df['Trip Duration'].mean()
print('Average travel time:', avg_time, ' seconds, or ', avg_time/3600, ' hours')
 
print('\n')
def showstatsforuser(city):

#Displays stats on bikeshare users"""

df = pd.read_csv(CITY_DATA[city])
#Displays count of each user types"""

print('Counts of each user type:\n', df['User Type'].value_counts());
#Displays count of each gender"""

if 'Gender' in df:
    print('Counts of each gender:\n', df['Gender'].value_counts())
#Displays earliest birth year, recent birth year and popular birth year"""

if 'Birth Year' in df:
    earliestbirthyear = int(df['Birth Year'].min())
    print('\n Earliest birth year :\n', earliestbirthyear)
    recentbirthyear = int(df['Birth Year'].max())
    print('\n most recent birth year:\n', recentbirthyear)
    popularbirthyear = int(df['Birth Year'].mode()[0])
    print('\n Most common year of birth:\n', popularbirthyear)
    
    print('\n')        
def main(): while True: city, month, day = takerequest () df = showdata (city, month, day) showrawdata (city) showstatsfortime (city) showstatsforstation (city) showstatsfortripduration(city) showstatsforuser (city)

#Asks user if user wants to start analysis again?"""

    repeat = input('\nStart again?: yes or no:\n')
    if repeat.lower() == 'no':
        break
if name == "main": main()
>>>>>>> 64226bbf93c71ee9e53ae858083ab7d353024b4b
