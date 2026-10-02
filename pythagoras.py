#1st way

# a,b,c = map(int, input().split())
# if ((a**2)+(b**2))==(c**2) or ((b**2)+(c**2)==(a**2)) or ((a**2)+(c**2)==(b**2)):
#     print(f"{a}, {b}, {c} are pythagorean triplets.")
# else:
#     print(f"{a}, {b}, {c} are not pythagorean triplets.")

#2nd way: by finding max first

a,b,c = map(int, input().split())
list1=[a,b,c]
print(list1)
#....