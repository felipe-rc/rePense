from dataclasses import dataclass
import datetime
import sqlite3


@dataclass
class Model:
    sqliteConnection = sqlite3.connect('src/model/database.db')
    cursor = sqliteConnection.cursor()

    def savePoints(self, score: int):
        query = f"INSERT INTO scores (score, date) VALUES ({score}, '{datetime.datetime.now()}');"
        self.cursor.execute(query)
        self.sqliteConnection.commit()

    def getPoints(self):
        query = 'SELECT score, date FROM scores ORDER BY date'
        result = self.cursor.execute(query)
        return result
