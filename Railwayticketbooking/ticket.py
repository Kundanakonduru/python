def Ticket():
    a = input("From:")
    b = input("To:")

    if not (a.isalpha() and b.isalpha()):
        print("Only letters are allowed")
        return

    c = int(input("No.of Passengers:"))

    x = 0;y=0;z=0

    for i in range(c):
        x = int(input("Old:"))

        if x == c:
            break

        elif x < c:
            y = int(input("Young:"))

            if (x + y) >= c:
                break

            elif (x + y) < c:
                z = int(input("Child:"))

                if (x + y + z) <= c:
                    break

    tick = 1000

    k = x * (80 / 100*tick)
    l = y * tick                
    m = z * (tick / 2)      

    total_price = k + l + m
    
    print("From:", a)
    print("To:", b)
    print("No.of Passengers:", c)

    if x > 0:
        print("No.of Old:", x)

    if y > 0:
        print("No.of Young:", y)

    if z > 0:
        print("No.of Children:", z)

    print("Total Price:", total_price)


Ticket()
