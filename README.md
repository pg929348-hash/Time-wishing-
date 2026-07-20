# Time Based Greeting Program

## Description
A simple Python program that takes time in 24-hour format as input and wishes the user 
according to the time of day. 
Good Morning, Good Afternoon, Good Evening, Good Night

## Features
1. Takes time input from user in 24-hour format: 0 to 24
2. Shows different greetings based on time:
   - 0 to 5     : Good Morning 🌄
   - 6 to 12    : Good Afternoon 🌞  
   - 13 to 17   : Good Evening 🌆
   - 18 to 24   : Good Night 🌃
3. Input validation: Shows "invalid" if time is < 0 or > 25

## Requirements
- Python 3.x
- No external libraries needed

## How to Run
1. Save the code as `time_greeting.py`
2. Open terminal or command prompt
3. Run the command:
   python time_greeting.py
4. Enter time when asked

## Example Output
Example 1:
enter the time:8
good afternoon 🌞

Example 2:
enter the time:20
 good night 🌃

Example 3:
enter the time:30
invalid 

## Note
Time should be entered in 24-hour format.
0-5 = Morning, 6-12 = Afternoon, 13-17 = Evening, 18-24 = Night
