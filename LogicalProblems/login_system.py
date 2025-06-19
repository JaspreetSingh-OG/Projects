username="jaspreet_542787"
pswd="M1ll!o^@iR#"
def login():
    attempts=3
    
    while attempts>0:
        log=input("Enter Username: ")
        password=input("Enter Password: ")
        if log==username and password==pswd:
            print("Login Successful")
            return True
        else:
            attempts-=1
            print(f"Wrong information! {attempts} attempts left.")
    print("Account Locked! Too many failed attempts")
    return False
login()


