with open("input.txt") as file:
    elf_calories = file.read()

elf_calories_split = elf_calories.split("\n\n")

elf_calories_sum = []

for elf_caliores in elf_calories_split:
    calory_numbers = map(int, elf_caliores.split("\n"))
    calory_sum = sum(calory_numbers)
    elf_calories_sum.append(calory_sum)

sorted_calories = sorted(elf_calories_sum, reverse=True)

print(sum(sorted_calories[:3]))
