def payment(bill, ppl):
    """
    this is the function for determining how much each person pays.
    args: bill(the total bill), ppl(number of people).
    return = the individual payment per person
    """
    try:
        return round((bill/ppl),2)
    except:
        print("an error occured with the payment calculation")

def tip(bill, perc, ppl):
    """
    this is the function for determmining the tip.
    it also splits the tip over a group of ppl
    args: bill(the total of bill), perc(the percentage of the tip to give), ppl(the number of people)
    return = the individual payment per person
    """
    try:
        return round((bill * (perc/100.00)/ppl), 2)
    except:
        print("an error occured with the tip calculation")


def main():
    """this is the main function"""
    print("how much is the bill ?")
    while True:
        try:
            total_bill = float(raw_input(">>$"))
            break
        except:
            print(" ")
            print("must be a number value")
            print(" ")
            print(" ")

    print "how many people ?"
    while True:
        try:
            num_ppl = int(raw_input(">>"))
            break
        except:
            print(" ")
            print("must be a number value")
            print(" ")
            print(" ")

    print "what percentage of tip"
    while True:
        try:
            perc = int(raw_input(">> %"))
            break
        except:
            print(" ")
            print("must be a number value")
            print(" ")
            print(" ")

    print("calculation payment")
    bill_payment = payment(total_bill, num_ppl)
    tip_payment = tip(bill, perc, num_ppl)
    total_payment = float(bill_payment) + float(tip_payment)

    print("each person pays $%s for the bill" % \str(bill_payment))
    print("each person pays $%s for the tip" % \str(tip_payment))
    print("which means each person will pay a total of %s" % \str(total_payment))

if __name__=='__main__':
    main()
    
                 

    
