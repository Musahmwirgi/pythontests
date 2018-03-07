#! /usr/bin/env python3

from datetime import datetime
import calendar

print('Enter Name:')
name = input()
print('name', name)

print('Enter Birth date (in the format dd-mm-yyyy:')
birth_date = input()
print('Birth date', birth_date)

print('Age at eight five:')
born = birth_date.split('-')
age_at_eighty_five = int(born[2]) + 85
print(born[0], '-', born[1], '-',  age_at_eighty_five)

print('Day of Birth:')

datetime.strptime(birth_date, '%d-%m-%Y').weekday()

print(calendar.day_name[datetime.strptime(birth_date, '%d-%m-%Y').weekday()])

print('Hi', name, 'you will turn 85 on', born[0],'-',born[1],'-',age_at_eighty_five,'.','You were born on', calendar.day_name[datetime.strptime(birth_date, '%d-%m-%Y').weekday()] )
