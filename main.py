import sqlite3
import time
import random   
conn = sqlite3.connect('main.db')
c = conn.cursor()
def table():
    c.execute("CREATE TABLE IF NOT EXISTS username(username VARCHAR, password VARCHAR)")
table()
def login():
    for i in range(3):
        username = input("pls enter your username: ")
        password = input("pls enter pass: ")
        with sqlite3.connect('main.db') as db:
            cursour = db.cursor()
        find_user = ('SELECT * FROM login WHERE username = ? AND password = ?')
        cursour.execute(find_user,[(username), (password)])
        results = cursour.fetchall()
        if results:
            for bla in results:
                malli = str(bla)
                print("Welcome ")
            break
        else:
            print("Username and passwored not recognised")
            again = input("Do u want to try again?(y/n): ")
            if again.lower() == "n":
                print("Good Bye")
                time.sleep(1)
                break
login()
def main():
    print("this are the categorys we have")
    print('''
    a.new acount
    b.veiw account 
    c.add money
    d.sending money
    ''')
    a = input("wich category do you want: ")
    def logic_statment():
        if a == 'a':
            print("you are creating a new account")
            c.execute("CREATE TABLE IF NOT EXISTS names(username,passwored)")
            while True:
                username  = input("enter your name: ")
                if not username.isalpha():
                        continue
                else:
                    try:
                        passwored = int(input("enter passwored: "))
                        bankAccountNumber = random.randint(1000,100000)
                        print(bankAccountNumber)
                        print("THIS IS YOUR BANK ACCOUNT NUBER")
                    except ValueError:
                        print("sorry i did'nt understand that")
                c.execute("INSERT INTO names(username,passwored) VALUES(?,?)",(username,passwored))
                conn.commit()
                print("SUCCESSFULLY ADDED")

                break
            c.execute("SELECT * FROM  names")
            for b in c.fetchall():
                print(b)
        elif a == 'b':
            c.execute("CREATE TABLE IF NOT EXISTS names(username,passwored)")
    logic_statment()
main()