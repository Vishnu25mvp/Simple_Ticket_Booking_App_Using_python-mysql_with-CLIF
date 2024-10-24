import mysql.connector


def DB_Connection():
    try:
        db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database="TICKET_BOOKING")
        return db
    except mysql.connector.Error as err:
        return f"SQL ERR {err}"


def create_table():
    db = DB_Connection()
    cur = db.cursor()
    try:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS EVENTS(
                EVENT_ID INT AUTO_INCREMENT PRIMARY KEY,
                EVENT_NAME VARCHAR(100) NOT NULL,
                EVENT_DATE DATETIME NOT NULL UNIQUE ,
                AVAILABLE_SEATS INT NOT NULL 
                )
                """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS USER(
            USER_ID INT PRIMARY KEY AUTO_INCREMENT,
            USER_NAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL UNIQUE,
            PASSWORD VARCHAR(100) NOT NULL 
            )
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS BOOKING(
            BOOKING_ID  INT AUTO_INCREMENT PRIMARY KEY,
            USER_ID INT ,
            EVENT_ID INT,
            SEATS_BOOKED INT NOT NULL ,
            FOREIGN KEY (USER_ID) REFERENCES USER(USER_ID)
            )
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS AGENT(
            AGENT_ID INT PRIMARY KEY AUTO_INCREMENT,
            AGENT_NAME VARCHAR(50) NOT NULL,
            GSTIN VARCHAR(50) NOT NULL UNIQUE,
            PASSWORD VARCHAR(100) NOT NULL 
            )
            """)

    except mysql.connector.Error as err:
        print(f"SQL ERROR {err}")


create_table()
