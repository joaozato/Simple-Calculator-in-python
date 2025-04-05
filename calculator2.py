firstnumber = int(input('say a number'))
secondnumber = int(input('say another number'))
operation = input('what operation you want do? You can select + , -, / or *')
if operation == '+':
    print(firstnumber + secondnumber)
else:
    if operation == '-':
        print(firstnumber - secondnumber)
    else:
        if operation == '/':
            print(firstnumber / secondnumber)
        else:
            if operation == '*':
                print(firstnumber * secondnumber)
            else:
                print('invalid number or operation')
                

