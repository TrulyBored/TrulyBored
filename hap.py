
import datetime as dt

AllTime = 1
while AllTime:
  current_time = dt.datetime.now()
  if not current_time.day == dt.datetime.now().day:
    print("Wish you a great day today! ^_^")

