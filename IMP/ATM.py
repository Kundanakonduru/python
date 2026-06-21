def ATM_machine():
  balance=50000
  while True:
    print("choice\n1.deposit\n2.withdraw\n3.check balance\n4.exit")
    choice=int(input("Enter choice number:"))

    if choice==1:
      amount=int(input("Enter amount number:"))
      balance+=amount
      print(f'Balance:{balance}')
    elif choice==2:
      amount=int(input("Enter amount number:"))
      if amount>balance:
        print("Insufficient balance")
      else:
        balance-=amount
        print(f'Balance:{balance}')
    elif choice==3:
      print(f"Balance:{balance}")
    elif choice==4:
      print("Thank you")
      break
    else:
      print("Invalid choice")
ATM_machine()
