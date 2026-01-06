balance = 0.0  
kyc_document = {}

print("==========================================================================")
print("Welcome!! to our banking app")
print("(*^_^*)")
print("-------------------------------------------------------------------------------------")


def check_balance():
    print(f" your current balance is: {balance} rupess")
    print("==========================================================================")

def deposite():
    global balance
    dep_amount = float(input("Enter the amount to deposit: "))
    if dep_amount>0:
        balance += dep_amount
    else:
        print("can not deposite a negative or zero amount")

    print(f"YOUR CURRENT BALANCE IS: {balance}")      
    print("==========================================================================")



def withrowal():
     global balance
     wit_amount = float(input("enter amount: "))
     if wit_amount<=0:
            print("can not withrowal a negative or zero amount")
     elif wit_amount > balance:
            print(f" Your acount balance is: {balance}. You cannot withrowal this amount.")
     else:
            balance -= wit_amount

     print("successfully withrowal!!")
     print("==========================================================================")

     print(f"YOUR CURRENT BALANCE IS: {balance}")   
     print("==========================================================================")      
          



 
def update_kyc(docs):
    global kyc_document
    kyc_document.update(docs)

def check_kyc():
    if len(kyc_document) == 0:
        print("KYC not done")
        print("==========================================================================")
    else:    
     for doc in kyc_document:
        print(f"{doc} : {kyc_document[doc]}")  
        print("==========================================================================")   

if __name__ =="__main__":
   print("================================================================")

     

   while True:
    
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check kyc")
    print("5. Update kyc")
    print("6. Exit")
    

    print ("""                                           
                                             
                                              
                                        """)
   
    choice = input("Please select an option (1-6): ")
    print("==========================================================================")
    print("⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓⪓")
    print ("""                                           
                                             
                                              
                                        """)

    if choice == '1':
        check_balance()
        print("==========================================================================")

    elif choice == '2':
        deposite()
        print("Your amount is sussessfully deposite!!!")
        print("==========================================================================")
    elif choice == '3':
        withrowal()
    elif choice == '4':
        check_kyc()
    elif choice == '5': 
        kyc_docs = {}
        n_document = int(input("enter number of document you want to upload:"))
        for i in range(n_document):
         key = input("enter the document type:")
         value = input("enter the document number: ")
         kyc_docs[key] = value
         update_kyc(kyc_docs) 
         print("KYC UPDATED!!!") 
         print("==========================================================================")
         break 
    elif choice == '6':
        print("🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏")
        print("Thank you for using our Banking Application. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")


       
print("""                                         
                                           
                                              
                                             """)
