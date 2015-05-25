__author__ = 'PaulFranken'
import sqlite3

import os



class DatabaseFunctions():
    #used once to create sqlite database, left for reference
    def create_db(self):
        self.c.execute('''CREATE TABLE tickets(name text,
                                        nr1 integer,
                                        nr2 integer,
                                        nr3 integer,
                                        nr4 integer,
                                        nr5 integer,
                                        redball integer)''')

    def save_to_db(self, name, ticket_list):
        if self.check_name(name) == True:
            for entry in ticket_list:
                self.c.execute('INSERT INTO tickets VALUES (?,?,?,?,?,?,?)', (name,
                                                                         entry[0],
                                                                         entry[1],
                                                                         entry[2],
                                                                         entry[3],
                                                                         entry[4],
                                                                         entry[5],))
            self.conn.commit()
        else:
            self.c.execute("DELETE FROM tickets WHERE name=?", (name,))

            for entry in ticket_list:
                self.c.execute('INSERT INTO tickets VALUES (?,?,?,?,?,?,?)', (name,
                                                                         entry[0],
                                                                         entry[1],
                                                                         entry[2],
                                                                         entry[3],
                                                                         entry[4],
                                                                         entry[5],))
            self.conn.commit()
            pass
    # function used to validate the name entry
    def check_name(self, name):
        self.c.execute('SELECT 1 FROM tickets WHERE name = ?', (name,))

        if self.c.fetchone():
            return False
        else:
            return True

    # function used to populate the optionmenu
    def get_players(self):

        query = self.c.execute('SELECT name FROM tickets GROUP BY name')
        playerList = [query.fetchall()]
        playerList = playerList.pop(0)

        return playerList

    def get_numbers(self, name):
        query = self.c.execute('SELECT nr1, nr2, nr3, nr4, nr5, redball FROM tickets WHERE name = ?', (name,))
        numberList = query.fetchall()
        return numberList

    def __init__(self):
        self.here = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(self.here, 'tickets.db')
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()


