list = []
biggest = 0
smallest = 0
for c in range(0,5):
    list.append(int(input(f"Write the valeu for position {c} = ")))
    if c == 0:
        smallest = biggest = list[c]
    else:
        if list[c] > biggest:
            biggest = list[c]
        if list[c] < smallest:
            smallest = list[c]

print(list)
print(f'The biggest Value is {biggest} at position {list.index(biggest)}.')
for i, v in enumerate(list):
    if v == biggest:
        print(f'Showing all position the biggest appear {i}...')
print(f'-=-'*20)
print(f'The smallest value is {smallest} in the position {list.index(smallest)}.')
for i, v in enumerate(list):
    if v == smallest:
        print(f'Showing all positions the smallest appear {i}...',)