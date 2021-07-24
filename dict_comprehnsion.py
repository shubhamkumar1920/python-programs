# dictionary comprehension
# square = {1:1,2:4,3:9}
square = {num:num**2 for num in range(1,11)}
print(square)

# case2:
square = {f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k}:{v}")