import sys

Stop = (str())

while Stop !="n" or "N" or "no" or "No" or "NO" or "false" or "False" or "end" or "End" or "stop" or "Stop":
    
    Invoice_Date = (str(input("Enter Invoice Date / Bill Date ")))
    Program_Code = (str(input("Enter Program Code ")))
    Recipient_ID = (str(input("Enter Four Digit Recipient ID ")))
    Activity_Code = (str(input("Enter Activity Code ")))
    FPN = (str(input("Federal Project Number ")))
    Object_Class = (str(input("Enter Project Class ")))
    Demo_ID = (str(input("Enter Demo ID ")))
    Transaction_Type = (str(input("Enter Transaction Type ")))
    Amount = (str(input("Enter Amount ")))
    RPD = (str(input("Enter Requested Payment Date ")))


    print(Invoice_Date,"|",Program_Code,"|",Recipient_ID,"|",Activity_Code,"|",FPN,"|",Object_Class,"|",Demo_ID,"|",Transaction_Type,"|",Amount,"|",RPD,sep='',end ='\n')



 
    # Saving the reference of the standard output
    original_stdout = sys.stdout    
 
    with open('FHWA_Bill.txt', 'a+') as f:
        sys.stdout = f 
        print(Invoice_Date,"|",Program_Code,"|",Recipient_ID,"|",Activity_Code,"|",FPN,"|",Object_Class,"|",Demo_ID,"|",Transaction_Type,"|",Amount,"|",RPD,sep='',end ='\n')
        # Reset the standard output
        sys.stdout = original_stdout 
 
    #print(Invoice_Date,"|",Program_Code,"|",Recipient_ID,"|",Activity_Code,"|",FPN,"|",Object_Class,"|",Demo_ID,"|",Transaction_Type,"|",Amount,"|",RPD,sep='',end ='\n')
    
    Stop = (str(input("would you like to enter another FHWA Bill? Y/N ")))