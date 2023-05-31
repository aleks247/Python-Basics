def task1():
    start = int(input("Въведете първото число: "))
    end = int(input("Въведете второто число: "))

    if start > end:
        start, end = end, start
        
    for number in range(start, end+1):
        print(number)
    
        
def task2():
    start = int(input("Въведете първото число: "))
    end = int(input("Въведете второто число: "))

    if start > end:
        start, end = end, start

    for number in range(end, start-1, -1):
        print(number)
        
def task3():
    lenght = int(input("Въведете дължината на списъка: "))
    listOfNumbers = []
    for i in range(lenght):
        number = int(input("Въведи число: "))
        listOfNumbers.append(number)
    for i in listOfNumbers:
        print(i) 
def task4():
    smallest = None
    while True:
        user_input = input("Въведете число (или 'END' за край на въвеждането): ")
        if user_input == 'END':
            break
        number = int(user_input)
        if smallest is None or number < smallest:
            smallest = number

    if smallest is not None:
        print("Най-малкото число, което сте въвели, е:", smallest)
    else:
        print("Не сте въвели нито едно число.")

def task5():
    numbers = []
    while True:
        user_input = input("Въведете число (или 'END' за край на въвеждането): ")
        if user_input == 'END' or user_input == 'end' or user_input == 'End':
            break
        number = int(user_input)
        if number % 2 == 0:
            numbers.append(number)

    print("Четните числа, които сте въвели, са:", end=" ")
    print(*numbers)
            
        
command = int(input("Избери задача(1,2,3,4,5): ")) 
if command == 1:
    task1()
elif command == 2:
    task2()
elif command == 3:
    task3()
elif command == 4:
    task4()
elif command == 5:
    task5()
else:
    print("Няма такава задача")