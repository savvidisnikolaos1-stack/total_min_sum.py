total = 0          
count = 0          
minimum = None     
maximum = None     

while True:
    user_input = input("შეიყვანეთ რიცხვი (ან 'stop'): ")

    
    if user_input == "stop":
        break

    
    try:
        number = float(user_input)
    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")
        continue  

    
    total += number
    count += 1

   
    if minimum is None or number < minimum:
        minimum = number
    if maximum is None or number > maximum:
        maximum = number


if count > 0:
    print("ჯამი:", total)
    print("რაოდენობა:", count)
    print("მაქსიმუმი:", maximum)
    print("მინიმუმი:", minimum)
else:
    print("რიცხვები არ შეგიყვანიათ")