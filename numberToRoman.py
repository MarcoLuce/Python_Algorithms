roman = {
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'C',
    900:'CM',
    1000:'M'
}

number = int(input("Enter a number: "))

romanOrder = [1000, 900, 500, 400, 100, 90, 60, 50, 40, 10, 9, 5, 4, 1]

print("The Roman number is: ")
for i in romanOrder:
    if number > 0:
        div = number //i
        if div > 0:
            number = number%i
            for a in range(div):
                print(roman[i], end=" ")

print(end='\n')
               
