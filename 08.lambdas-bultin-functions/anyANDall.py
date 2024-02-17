number = [1, 20, 20, 10]
ans = [num for num in number if num % 2 == 0]
print(ans)
print(all(ans))

print(any(ans))