from database import DB_Connection
import mysql.connector
import pandas as pd


class User:
    def __init__(self, id: int, name: str, mail: str):
        self.user_id = id
        self.user_name = name
        self.mail = mail

    def display_event(self):
        try:
            con = DB_Connection()
            cur = con.cursor()
            cur.execute("""SELECT * FROM EVENTS
                            WHERE CURRENT_TIME()<EVENT_DATE""")
            data = cur.fetchall()
            df = pd.DataFrame(columns=["Event_ID","EVENT_NAME","EVENT_DATE","NO OF SEAT"],data=data)
        except mysql.connector.Error as Err:
            print("SQL ERROR", Err)

        finally:
            if bool(data):
                print(df)
            else:
                print("No Data Found")

    def display(self):
        print(f"User_id : {self.user_id}")

    def Book_Ticket(self,event_id):
        global df, con, cur
        try:
            con = DB_Connection()
            cur = con.cursor()
            cur.execute("""
                SELECT * FROM EVENTS WHERE CURRENT_TIME()<EVENT_DATE AND EVENT_ID =%s
                """,(event_id,))
            data = cur.fetchall()
            df = pd.DataFrame(columns=["Event_ID","EVENT_NAME","EVENT_DATE","NO OF SEAT"],data=data)
            print(df)
        except mysql.connector.Error as Err:
            print("SQL ERROR",Err)
        finally:
            cur.close()
            con.commit()

        try:
            seat = int(input("Enter the no of seat to be book : "))
            event_id = int(df["Event_ID"].iloc[0])
            con = DB_Connection()
            cur = con.cursor()
            print(event_id)
            cur.execute("""INSERT INTO BOOKING(USER_ID,EVENT_ID,SEATS_BOOKED)
                            VALUES(%s, %s, %s)""",(self.user_id,event_id,seat))
            cur.execute("""UPDATE EVENTS SET AVAILABLE_SEATS = AVAILABLE_SEATS-%s WHERE EVENT_ID =%s;""",(seat,event_id))

        except mysql.connector.Error as Err:
            print("SQL ERROR", Err)
        finally:
            cur.close()
            con.commit()
            print("Ticket Bokk SucessFully")

    def Booking_history(self):
        try:
            con = DB_Connection()
            cur = con.cursor()
            cur.execute("""
                SELECT BOOKING_ID,EVENT_ID,SEATS_BOOKED FROM BOOKING WHERE USER_ID = %s
            """,(self.user_id,))
            df = pd.DataFrame(columns=["Booking_id","Event_id","Seats_Booked"],data=cur.fetchall())
            print(df)
        except mysql.connector.Error as Err:
            print("SQL Error",Err)
    def Cancel_Ticker(self,Booking_id):
        global cur, con
        try:
            con = DB_Connection()
            cur = con.cursor()
            cur.execute("""
                SELECT SEATS_BOOKED FROM BOOKING WHERE BOOKING_ID = %s
            """,(Booking_id,))
            seat = cur.fetchall()[0][0]
            cur.execute("""
                UPDATE EVENTS SET AVAILABLE_SEATS = AVAILABLE_SEATS + %s
            """,(seat,))
            cur.execute("""
                DELETE FROM BOOKING WHERE BOOKING_ID = %s
            """,(Booking_id,))

        except mysql.connector.Error as Err:
            print("SQL Error",Err)
        finally:
            cur.close()
            con.commit()

