import sqlite3



def save_result(url, status_code, response_time, error_type=None):
    conn=sqlite3.connect("faultlab.db")
    print("Database connected seccessfully")
    cur=conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS api_checks (
            id INTEGER PRIMARY KEY,
            url TEXT,
            status_code INTEGER,
            response_time_ms REAL,
            error_type TEXT
        )
    ''')

    
    cur.execute("INSERT INTO api_checks (url, status_code, response_time_ms, error_type) VALUES(?,?,?,?)",  (url,status_code, response_time, error_type))
    
    print ("Result saved successfullyt")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    save_result("https://gitlllhub.com", None, 30.19, "NETWORK_ERROR")