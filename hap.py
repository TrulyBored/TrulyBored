
import datetime as dt

AllTime = True
while AllTime:
  current_time = dt.datetime.now()
  if not current_time.day == dt.datetime.now().day:
    print("Wish you a great day today! ^_^")

