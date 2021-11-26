month = ("January", "Febuary", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December")
profit = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

biggestprofit = max(profit)
thatoneannoyingindex1 = profit.index(biggestprofit)
print(thatoneannoyingindex1)

month1 = month[thatoneannoyingindex1]
print("We earned the maximum amount of " + str(biggestprofit) + " while we are selling lemons in the month of " + month1 + ".")

smolprofit = min(profit)
thatoneannoyingindex2 = profit.index(smolprofit)
print(thatoneannoyingindex2)

month2 = month[thatoneannoyingindex2]
print("We earned the minimum amount of " + str(smolprofit) + " while we are selling lemons in the month of " + month2 + ", see gearled, this is why we don't sell lemons with a stick.")

#this code is totoally not scuffed and totally not copied off of byju's future school