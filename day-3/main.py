with open("input.txt") as file:
    rucksacks = file.read().splitlines()

# Part 1
# priority_sum = 0

# for rucksack in rucksacks:
#     compartment_1 = rucksack[: len(rucksack) // 2]
#     compartment_2 = rucksack[len(rucksack) // 2 :]

#     duplicate_item = next(iter(set(compartment_1).intersection(compartment_2)))

#     if duplicate_item < "a":
#         item_priority = ord(duplicate_item) - 38
#     else:
#         item_priority = ord(duplicate_item) - 96

#     priority_sum += item_priority

# print(priority_sum)

# Part 2

elf_groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

priority_sum = 0

for rucksack_1, rucksack_2, rucksack_3 in elf_groups:
    badge_set = set(rucksack_1).intersection(rucksack_2).intersection(rucksack_3)
    badge = next(iter(badge_set))

    if badge < "a":
        badge_priority = ord(badge) - 38
    else:
        badge_priority = ord(badge) - 96

    priority_sum += badge_priority

print(priority_sum)
