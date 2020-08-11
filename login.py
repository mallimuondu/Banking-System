import sqlite3
conn = sqlite3.connect('main.db') 
cursour = conn.cursor()
    
cursour.execute("CREATE TABLE IF NOT EXISTS login(username VARCHAR, password VARCHAR)")

cursour.execute("INSERT INTO login VALUES('malli', 'Malli2010')")
                
cursour.execute("INSERT INTO login VALUES('nesh', '12')")
conn.commit()