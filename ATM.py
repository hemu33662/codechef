X = int(input('How much you want to withdraw :'))
Y = float(input('How much balance is in your account :'))
if (Y > X):
    if (X % 5==0):
        Y = Y - (X + 0.5)
        print("current bank balance is "'%.2f'% Y)
    else:
        print('Invalid \nYour account balance is',Y)                                       
else:
    print("insufficient balance \nYour account balance is :",Y)