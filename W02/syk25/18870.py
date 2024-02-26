N = int(input())
numbers = list(map(int, input().split()))
compare = sorted(list(set(numbers)))
compare_dict = {val: i for i, val in enumerate(compare)}
answer = [compare_dict[number] for number in numbers]
print(' '.join(map(str, answer)))