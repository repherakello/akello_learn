hello = "hello world".upper()
hello1 = input("Enter your name").strip()
print(hello)
print(hello1.upper())

#working with formated string's'
amount_t = 12456
intrest_rate = 0.013

intrest = amount_t * intrest_rate
print(intrest)
print("The intrest is", round(intrest, 2))
print("The intrst is:", format(intrest, ".2f"))

print(format(56.343433, "10.2f")) # formatting floating-point numbers. 10 = width it takes and 2/3= digits after decimal
print(format(56748.5454, "10.2e")) #formatting scientific notation
print(format(0.0023453, "10.2%")) #formatting as a percentage
print(format(2343.05, "10.2f")) #want to justify the format
print(format(2343.05, "<10.2f")) #justified format
print(format(345432, "10d")) #formatting integer into decimal(d)
print(format(32435, "10x")) #the format is into hexadecimal integer
#formatting string
print(format("hello world!", "20s"))
print(format("hello world!", ">20s"))
print(format("hello world!", "<20s"))