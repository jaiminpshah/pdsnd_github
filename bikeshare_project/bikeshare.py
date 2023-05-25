Type: test
This is the test scripting to check bikeshare statistics.

Subject: Bikeshare project

Description:

This scripting focuses on pandas library usage and simple statics methods to perform descriptive analysis on the bikeshare data.
Bikeshare project

This project display information such as most popular days or most common stations from 3 U.S cities - Chicago, Washington and New York City. This project also provides the data as per user request.

This scripting focuses on pandas library usage and simple statics methods to perform descriptive analysis on the bikeshare data.

fixes # all good

import time 
import pandas as pd
import numpy as np

chicago=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\chicago.csv")
new_york_city=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\new_york_city.csv")
washington=pd.read_csv("C:\\Users\\Jaimi\Desktop\\Python\\washington.csv")

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def takerequest():

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

#Displays 5 records from the selected city."""
#Asks user to type 'yes' or 'no' if user wants to see more record or not"""
    
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
