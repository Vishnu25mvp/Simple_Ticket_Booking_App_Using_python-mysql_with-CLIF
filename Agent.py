from database import DB_Connection
import mysql.connector


class Agent:
    def __init__(self, agent_id, agent_name, agent_gstin):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.gstin = agent_gstin

    def post_event(self, event_name, date, seat):
        con = DB_Connection()
        cur = con.cursor()
        try:
            cur.execute("""
                INSERT INTO EVENTS(
                EVENT_NAME,EVENT_DATE,AVAILABLE_SEATS) VALUES (
                %s,%s,%s
                )
            """, (event_name,date,seat))
        except mysql.connector.Error as err:
            print("SQL ERROR", err)
        finally:
            cur.close()
            con.commit()
            print("Event Uploaded Sucessfully")

# agent = Agent(123,"vishnu",1234)
