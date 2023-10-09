num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

#Q_1
for num in num_list:
    print(num)

#Q_2 
if (num>45):
    print(num)

#Q_3
if (num>45):
    print("Over 45")
else:
    print("Under 45")

#Q_4
for index, num in enumerate(num_list):
    if (num == 36):
        print ("Number found at position ", index)
#Q_5, 6, 7,8:
count=0
for index, num in enumerate(num_list):
   if (num == 36):
        count += 1
        print ("Number found at position ", index)
        break
print("Total value of count= ",count)
