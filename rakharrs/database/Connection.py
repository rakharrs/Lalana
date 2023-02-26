import psycopg2


class Connection:
    __database = "lalana"
    __host = "localhost"
    __user = "rakharrs"
    __password = "pixel"
    __port="5432"

    @staticmethod
    def getPsql():
        return psycopg2.connect(database=Connection.__database,
                                host=Connection.__host,
                                user=Connection.__user,
                                password=Connection.__password,
                                port=Connection.__port)

    @staticmethod
    def close(connection):
        if connection != None: connection.close()

    @staticmethod
    def select(connection, query):
        cursor = None
        array = []
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            for component in cursor.fetchall: array.append(component)
        finally:
            if cursor is not None: cursor.close()
        return array

    @staticmethod
    def select_first(connection, query):
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchone()
        finally:
            if cursor is not None: cursor.close()

