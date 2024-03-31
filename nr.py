print("NOISE RESTRICTION")
zone=input("Enter the zone:")
db=int(input("Enter the noise level in decibals:"))
ch='y'
while ch=='y':
    if zone=="silence":
        if db>=40:
            print("ALERT: NOISE LEVEL EXCEEDED")
        else:
            print("NOISE LEVEL MAINTAINED")
    elif zone=="industrial":
        if db>=75:
            print("ALERT: NOISE LEVEL EXCEEDED")
        else:
            print("NOISE LEVEL MAINTAINED")
    elif zone=="commertial":
        if db>=65:
            print("ALERT: NOISE LEVEL EXCEEDED")
        else:
            print("NOISE LEVEL MAINTAINED")
    elif zone=="residential":
        if db>=65:
            print("ALERT: NOISE LEVEL EXCEEDED")
        else:
            print("NOISE LEVEL MAINTAINED")
    else:
        print("INVALID ZONE")
    ch=input("Would you like you continue(y/n):")
    if ch!='y':
        print("TERMINATED")
        break


