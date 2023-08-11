import dbm
import time

print('Welcome to our dated numbers!')

# create a new dbm file called 'datednumbers'.
datednumbers = dbm.open('datednumbers', 'c')

data = input('-> type a to add, r to retrieve : ')

'''
When the user wants to add a number, we want to add the date/time it was added and put it into a tuple where the first item is the time and second being the number input. 
Once that's done, we print the notification that the number has been stored at the given time, and we add that entry into our dbm file.
'''
if data == 'a':
    (a, b) = (time.ctime(), input('-> give a number : '))
    print("stored ('" + a + "',", b + ")")
    datednumbers[str(len(datednumbers))] = b + ' was stored on ' + a

'''
Now, we can retrieve our entries in our dbm file to show what number was put in at any given date.
However, our input for our key will be the amount of entries that was in the dbm file before the latest entry was made.
'''
elif data == 'r':
    c = input('-> enter a natural number < ' + str(len(datednumbers)) + ' : ')
    print(str(datednumbers[str(c)]))