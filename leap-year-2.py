def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        leap = True
      else:
        print("Not leap year.")
        leap = False
    else:
      print("Leap year.")
      leap = True
  else:
    print("Not leap year.")
    leap = False
  return leap

def days_in_month(year, month):
    leap = is_leap(year)
    if month > 12 or month < 1:
      return "Input a valid month!"
    if leap == False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = month_days[month - 1]  
    if leap == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = month_days[month - 1]
    return days

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)