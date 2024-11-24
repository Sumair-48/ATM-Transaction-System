import mysql.connector

atm_database = mysql.connector.connect(
    host="127.0.0.1",
    username="root",
    password="118162",
    database="ATM_SYS"
)

mycursor = atm_database.cursor()


def create_acc():

    acc_owner_name = input("Enter Your Full Name: ")
    cnic_id_num = int(input("Enter Your CNIC No: "))
    owner_occupation = input("Enter Your Occupation: ")
    owner_age = int(input("Enter Your Age: "))
    owner_city = input("Enter Your City you Currently Live In: ")

    acc_owner_id = int(input("According To You Enter 13 Digit Account Number: "))
    acc_owner_pass = int(input("Set Your Account Pin (4 digit): "))

    acc_details_insert = "INSERT INTO ATM_ACC_DETAIL(Acc_num,Acc_owner,Acc_pass,Acc_Owner_Occ,CNIC_Num,Age,City) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data_1 = (acc_owner_id,acc_owner_name,acc_owner_pass,owner_occupation,cnic_id_num,owner_age,owner_city)
    mycursor.execute(acc_details_insert,data_1)
    atm_database.commit()

def account_access_main_menu():

    print("""
                                            Menu
    
    To Withdraw Cash Press          : 1             To Deposit Cash Press           : 2
    To Check Balance Press          : 3             To Check Account Details Press  : 4
    To Check Transaction Press      : 5             To Log out From Account         : 6
    """)
    
    account_operation = int(input('Operation Want To Perform: '))

    if account_operation == 1:
        withdraw_def()
        print("\n Ammount Has Successfully Withdraw!! ")
    
    elif account_operation == 2:
        deposit_def()
        print("\n Ammount Has Successfully Deposited!! ")

    elif account_operation == 3:
        balance()

    elif account_operation == 4:
        acc_details()

    elif account_operation == 5:
        transactions()

    elif account_operation == 6:
        begin()

    else:
        print("Invalid")

def withdraw_def():

    print("""
                    Withdraw Cash 

    $1000 Press  : 1                $2000 Press        : 2  
    $5000 Press  : 3                $10000 Press       : 4
    $15000 Press : 5                Other Amount Press : 6        
    """)
    
    withdraw_operation = int(input("Operation Want To Perform: "))

    if withdraw_operation == 6:

        withdraw_cash = int(input("Enter Amount Want To Withdraw: "))
        withdraw_operation_id = Acc_Id_access
        withdraw_sql_query_1 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,%s,NOW())"
        data_3_1 = (withdraw_operation_id,withdraw_cash)

        mycursor.execute(withdraw_sql_query_1,data_3_1)
        atm_database.commit()

    elif withdraw_operation == 1:

        withdraw_operation_id_1 = Acc_Id_access
        withdraw_sql_query_2 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,1000,NOW())"
        data_3_2 = (withdraw_operation_id_1,)

        mycursor.execute(withdraw_sql_query_2,data_3_2)
        atm_database.commit()
    
    elif withdraw_operation == 2:

        withdraw_operation_id_2 = Acc_Id_access
        withdraw_sql_query_3 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,2000,NOW())"
        data_3_3 = (withdraw_operation_id_2,)

        mycursor.execute(withdraw_sql_query_3,data_3_3)
        atm_database.commit()
    
    elif withdraw_operation == 3:

        withdraw_operation_id_3 = Acc_Id_access
        withdraw_sql_query_4 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,5000,NOW())"
        data_3_4 = (withdraw_operation_id_3,)

        mycursor.execute(withdraw_sql_query_4,data_3_4)
        atm_database.commit()
  
    elif withdraw_operation == 4:

        withdraw_operation_id_4 = Acc_Id_access
        withdraw_sql_query_5 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,10000,NOW())"
        data_3_5 = (withdraw_operation_id_4,)

        mycursor.execute(withdraw_sql_query_5,data_3_5)
        atm_database.commit()
   
    elif withdraw_operation == 5:
        withdraw_operation_id_5 = Acc_Id_access
        withdraw_sql_query_6 = "INSERT INTO ATM(Acc_Id,Withdraw,date_time) VALUES (%s,15000,NOW())"
        data_3_6 = (withdraw_operation_id_5,)
        
        mycursor.execute(withdraw_sql_query_6,data_3_6)
        atm_database.commit()

    else:
        print("Invalid Error")

    print("\n Ammount Has Successfully Withdraw!! ")

    next_op = int(input("For Main Menu (1) else For Log out: "))
    if next_op == 1:
        account_access_main_menu()
    else:
        begin()

def deposit_def():

    print("""
                    Deposit Cash
    """)

    deposit_operation = int(input("Ammount Want To Deposit: "))
    deposit_operation_id = Acc_Id_access
    deposit_sql_query = "INSERT INTO ATM (Acc_Id,Deposit,date_time) VALUES (%s,%s,NOW())"
    data_2 = (deposit_operation_id,deposit_operation)

    mycursor.execute(deposit_sql_query,data_2)
    atm_database.commit()

    print("\n Ammount Has Successfully Deposited!! ")

    next_op = int(input("For Main Menu (1) else For Log out: "))
    if next_op == 1:
        account_access_main_menu()
    else:
        begin()


def balance():
    print("""
                    Balance       
    """)

    balance_operator_id = Acc_Id_access
    print(f"Account ID: {balance_operator_id}")
    sql_balance_query = "SELECT SUM(Deposit) - SUM(Withdraw) AS Difference FROM ATM WHERE Acc_Id = %s"
    data_8 = (balance_operator_id,)

    mycursor.execute(sql_balance_query, data_8)
    balance_result = mycursor.fetchone()

    if balance_result and balance_result[0] is not None:
        print(f"Your balance is: {balance_result[0]}")
    else:
        print("No transactions found or balance is zero.")

    next_op = int(input("For Main Menu (1) else For Log out: "))
    if next_op == 1:
        account_access_main_menu()
    else:
        begin()

def transactions():
    print("""
                            Transactions
    
    To Check Withdraw Statement : 1
    To Check Deposit Statement  : 2     
          
    """)

    operation_trans = int(input("Operation Want To Perform: "))

    if operation_trans == 1:

        transactions_id = Acc_Id_access
        print(f"Account ID: {transactions_id}\n")
        transactions_sql_query = "Select Withdraw,date_time from ATM WHERE Acc_Id = %s AND Withdraw is NOT NULL"
        data_trans = (transactions_id,)
        mycursor.execute(transactions_sql_query,data_trans)
        result_1 = mycursor.fetchall()

        for x in result_1:
            print(f"Deposit: {x[0]},                         Date and Time: {x[1]}")

    elif operation_trans == 2:

        transactions_id = Acc_Id_access
        print(f"Account ID: {transactions_id}\n")
        transactions_sql_query_2 = "Select Deposit,date_time from ATM WHERE Acc_Id = %s AND Deposit is NOT NULL "
        data_trans_2 = (transactions_id,)
        mycursor.execute(transactions_sql_query_2,data_trans_2)
        result_2 = mycursor.fetchall()

        for y in result_2:
            print(f"Deposit: {y[0]},                         Date and Time: {y[1]}")

    else: 
        print("Invalid Error")

    next_op = int(input("For Main Menu (1) else For Log out: "))
    if next_op == 1:
        account_access_main_menu()
    else:
        begin()

def acc_details():

    print("""
                    Account Details
    """)

    acc_operation_id = Acc_Id_access
    table = "Select Acc_num, Acc_owner, Acc_Owner_Occ, CNIC_Num, Age, City from ATM_ACC_DETAIL Where Acc_num = %s"
    data_acc = (acc_operation_id,)
    mycursor.execute(table,data_acc)
    my_acc_result = mycursor.fetchall()
    for x in my_acc_result:
        print("Employee Id:", x[0])
        print("Employee Name:", x[1])
        print("Employee Occupation:", x[2])
        print("Employee CNIC Num:", x[3])
        print("Employee Age:", x[4])
        print("Employee City:", x[5])
        print("/---------------------------------/")

    next_op = int(input("For Main Menu (1) else For Log out: "))
    if next_op == 1:
        account_access_main_menu()
    else:
        begin()
    

def login():
    Acc_pass_access = Acc_Id_access
    Acc_pass_query = "Select Acc_pass From ATM_ACC_DETAIL Where Acc_num = %s"
    data_acc = (Acc_pass_access,)
    mycursor.execute(Acc_pass_query, data_acc)
    Acc_result = mycursor.fetchone()

    if Acc_result and Acc_result[0] == int(input("Enter Your 4-digit PIN: ")):
        print("Access Granted!!")
        account_access_main_menu()
    else:
        print("Wrong input!!")


def close_acc():

    pass


def begin():
    print("""
                    WELCOME TO BCCI
        BANK OF CREDIT AND COMMERCE INTERNATIONAL

        To Create Account Press : 1
        To Login Account Press  : 2    
        """)
    
    operation= int(input("Operation Want To Perform: " ))

    if operation == 1:
        create_acc()
        print("\nYOUR ACCOUNT HAS BEEN CREATED!!")
    
    elif operation == 2:
        global Acc_Id_access
        Acc_Id_access = int(input("Enter Your Account ID: "))
        login()
    
    else:
        print("Invalid Error!!")


def main():
        
     begin()

main()