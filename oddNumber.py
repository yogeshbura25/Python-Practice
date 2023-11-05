start = int(input())
end = int(input())
odd = ""
for num in range(start, end + 1):
    result = ( num % 2 == 1)
    if result:
        odd = odd + str(num) + " "
print(odd)