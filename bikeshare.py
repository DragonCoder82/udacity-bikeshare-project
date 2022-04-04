import calendar
import datetime as dt
import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
days = ['monday', 'tuesday', ' wednesday', 'thursday', 'friday', 'saturday', 'sunday']
cities = ['chicago', 'new york city', 'washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago', 'new york city', 'washington']
        city = input('Please choose one of the following cities: Chicago, New York City, and Washington:\n>>> ').lower()
        if city not in cities:
            print('"{}" is currently not a city we have information on. Please try one of the following: Chicago, New York City or Washington.'.format(city))
            continue
        else:
            break
    # TO DO: get user input on what month they want data on.
    while True:
        months= ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
        month = input('Please enter the month you would like additional information on:\n>>> ' ).lower()
        if month not in months:
            print('"{}" is not a valid month. Please choose one of the following: January, February, March, April, May, June, July, August, Septemeber, October, Novermber or December.' .format(month))
            continue
        else:
            break

    # TO DO: get user input on what day they want data on.            
    while True:
        days = ['monday', 'tuesday', ' wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input('Please enter the day you would like additional information on:\n>>> ', ).lower()
        if day not in days:
            print('"{}" is not a valid day. Please choose one of the following: Monday, Tuesday, Wednesday, Thursday, Froday, Saturday or Sunday.'.format(day))
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
  """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
  df = pd.read_csv(CITY_DATA[city])
    
    # convert Start Time column to datetime
  df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of the week from Start Time to create new columns
  df['month'] = df['Start Time'].dt.month
  df['weekday'] = df['Start Time'].dt.day_name()
  df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
  if month != 'All':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe:
        df = df[df['month']==month] 

    # filter by day of week if applicable
  if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['weekday']==day.title()]
  

  return df 
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('The most common month is: ', common_month)
    

     # TO DO: display the most common day of week
   
    common_day = df['weekday'].mode()
    print('The most common day of the week is: ', common_day)


   #TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: ", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popp_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(popp_start_station))

    # TO DO: display most commonly used end station
    popp_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(popp_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    popp_com= df['combination'].mode()[0]
    print("The most frequent combination of start and end station is {} ".format(popp_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("The total trip duration was: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))

    # TO DO: display mean travel time
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("The mean travel time was: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The mean travel time was: {} minute(s) {} second(s)".format(m,sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of each gender is: \n", user_types)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_type = df['Gender'].value_counts()
        print('The gender types are below: \n')
    else:
        print("Gender column does not exist")

        
    # Display themost common year of birth
    if "Birth Year" in df.columns:
        birth_year = df['Birth Year'].mode()
        print('The most common year of birth is: \n', birth_year)
    else:
        print("The birth year column doesn't exist")
        
    # Display the earliest year of birth
    if "Birth Year" in df.columns:
        birth_year_min = df['Birth Year'].min()
        print('The earliest year of birth is: \n', birth_year_min)
    else:
        print("The birth year column doesn't exist")
    # Display the most recent year of birth
    if "Birth Year" in df.columns:
        birth_year_max = df['Birth Year'].max()
        print('The most recent birth year is: \n', birth_year_max)
    else:
        print("The birth year column doesn't exist.")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
 

view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
start_loc = 0

while (ask):
  print(df.iloc[start_loc:start_loc +5])
  start_loc += 5
  view_data = input("Do you wish to continue?: ").lower()
  if view_display == "no":
        ask = False
        
if __name__ == "__main__":
	main()
