with open("input.txt") as file:
    input = file.read()

assignment_pairs = input.splitlines()

# Part 1
fully_contained_count = 0

for pair in assignment_pairs:
    first, second = pair.split(",")

    start_first, end_first = map(int, first.split("-"))
    start_second, end_second = map(int, second.split("-"))

    # First contains second
    if start_first <= start_second and end_first >= end_second:
        fully_contained_count += 1
    # Second contains first
    elif start_second <= start_first and end_second >= end_first:
        fully_contained_count += 1

print(fully_contained_count)

# Part 2
overlap_count = 0

for pair in assignment_pairs:
    first, second = pair.split(",")

    start_first, end_first = map(int, first.split("-"))
    start_second, end_second = map(int, second.split("-"))

    # First overlaps second
    if start_first <= start_second and end_first >= start_second:
        overlap_count += 1
    # Second overlaps first
    elif start_second <= start_first and end_second >= start_first:
        overlap_count += 1

print(overlap_count)
