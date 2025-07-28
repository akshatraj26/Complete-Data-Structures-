

numDays = int(input("How many day's temperature."))
total = 0
temperature = []
for i in range(1, numDays+1):
    nextDay = int(input(f"Day {i} high temperature."))
    temperature.append(nextDay)
    total += nextDay

average = round(total/numDays, 2)

above_avg = []

for element in temperature:
    if element> average:
        above_avg.append(element)
print("Done Calculating")
print(above_avg)
print(f"There are {len(above_avg)} days above average temperature.")