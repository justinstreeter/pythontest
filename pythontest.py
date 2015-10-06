restart = 'y'
while restart != 'n': 
        print ("enter total amount")
        total = int(input())
        print ("enter number of people")
        numPeople = int(input())
        print ("enter tip percent")
        tipPerc = int(input())

        tip = total * (tipPerc/100) / numPeople
        tipPlus = (total * (tipPerc/100) + total) / numPeople
        if numPeople < 2:
            print ("your tip ammount is $",tip)
            print ("your tip plus total is $",tipPlus)
            print ("enter another tip? if not enter n ")
            restart = input()
        else:
            print ("your tip amount each is $",tip)
            print ("your tip plus total each is $",tipPlus)
            print ("enter another tip if? if not enter n")
            restart = input()
