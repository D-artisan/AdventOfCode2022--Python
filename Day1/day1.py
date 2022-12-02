calories = [calorie.strip() for calorie in open('calories.txt')]

calories_list = []


for elf in ('\n'.join(calories)).split('\n\n'):
    counter = 0
    for e in elf.split('\n'):
        counter += int(e)
    calories_list.append(counter)
sorted_calories_list = sorted(calories_list)


print(sorted_calories_list[-1])
print(sorted_calories_list[-1]+sorted_calories_list[-2]+sorted_calories_list[-3])