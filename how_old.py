#How many days old were you on the eve of the new millennium?
dob_D = int(input("Day: "))
dob_M = int(input("Month: "))
dob_Y = int(input("Year: "))

import datetime

dob = datetime.datetime(dob_Y, dob_M, dob_D)
millennium = datetime.datetime(1999, 12, 31)

difference = millennium - dob

if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")


