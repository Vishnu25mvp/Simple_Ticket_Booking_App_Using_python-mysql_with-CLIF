from database import DB_Connection
import mysql.connector
import hashlib

def passwd_enc(passsword):
    slat = "HWX@#$@"
    passsword = passsword+slat
    passsword = passsword.encode("utf-8")
    passwd = hashlib.sha256(passsword)
    return passwd.hexdigest()

def login(user,passwd):
    global data
    try:
        con = DB_Connection()
        cur = con.cursor()
        passwd = passwd_enc(passwd)
        cur.execute("""SELECT USER_ID, USER_NAME, EMAIL 
                        FROM USER
                        WHERE USER_NAME = %s AND PASSWORD= %s""", (user, passwd))
        data = cur.fetchall()
    except mysql.connector.Error as Err:
        print("SQL Error", Err)
    finally:
        return data


def Singup(user_name,email,password):
    con = DB_Connection()
    cur = con.cursor()
    try:
        password = passwd_enc(password)
        cur.execute("""
                        INSERT INTO USER(
                        USER_NAME,EMAIL,PASSWORD
                        ) VALUES (
                        %s, %s, %s
                        )
                    """, (user_name, email, password))
    except mysql.connector.Error as err:
        print("SQL ERROR",err)
    else:
        print("user Register Sucessfully")
    finally:
        con.commit()

def Agent_Singup(agent_name, gstin, password):
    con = DB_Connection()
    cur = con.cursor()
    try:
        password = passwd_enc(password)
        cur.execute("""
                        INSERT INTO AGENT(
                        AGENT_NAME,GSTIN,PASSWORD
                        ) VALUES (
                        %s, %s, %s
                        )
                    """, (agent_name, gstin, password))
    except mysql.connector.Error as err:
        print("SQL ERROR",err)
    else:
        print("Agent Register Sucessfully")
    finally:
        con.commit()


def Agent_login(user,passwd):
    con = DB_Connection()
    cur = con.cursor()
    global data
    try:
        passwd = passwd_enc(passwd)
        cur.execute("""SELECT AGENT_ID, AGENT_NAME, GSTIN 
                        FROM AGENT
                        WHERE AGENT_NAME = %s AND PASSWORD= %s""", (user, passwd))
        data = cur.fetchall()
    except mysql.connector.Error as Err:
        print("INVAILD PASSWORD AND USER NAME", Err)
    finally:
        return data


