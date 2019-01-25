
def charToAscii():
    c=input("enter a character : ");
    print(ord(c));
    x=-1;
    program();

def asciiToChar():
    c=int(input("enter a number : "));
    print(chr(c));
    x=-1;
    program();
    
def program():
    x=-1
    while(x!=1 and x!=2 and x!=0):
        x=int(input("what to do ? \n 1.Ascii to character \n 2.Character to Ascii \n 0.Nothing \n"))
        if(x==1):
            asciiToChar()
        elif(x==2):
            charToAscii()
        elif(x==0):
            print("Thankyou for visiting");
        else:
            print("enter valid option");
        return 0;

program()
