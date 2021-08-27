import sqlite3


class SqliteDB:
    def __init__(self, db_name):
        """
        :type db_name: str
        """
        self.db_name = db_name

    def select_all(self, get_query):
        """
        :param get_query: function
        :return: function
        """
        def wrapper(*args):
            """
            :return: list
            """
            result = None
            if args:
                sql, params = get_query(*args)
                result = self.__get_all_records(sql, params)
            else:
                sql = get_query()
                result = self.__get_all_records(sql)
            return result

        return wrapper

    def select_one(self, get_query):
        """
        :param get_query: function
        :return: function
        """
        def wrapper(*args):
            """
            :return: list
            """
            result = None
            if args:
                sql, params = get_query(*args)
                result = self.__get_one_record(sql, params)
            else:
                sql = get_query()
                result = self.__get_one_record(sql)
            return result

        return wrapper

    def update_or_delete_or_insert(self, get_query):
        """
        :param get_query: function
        :return: function
        """
        def wrapper(*args):
            """
            :return: bool
            """
            result = False
            if args:
                sql, params = get_query(*args)
                result = self.__get_success_operation(sql, params)
            return result

        return wrapper

    def __get_all_records(self, sql=None, params=None):
        """
        :param sql: str
        :param params: tuple
        :return: list
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            if sql and params:
                result = cursor.execute(sql, params).fetchall()
            else:
                result = cursor.execute(sql).fetchall()
        except Exception as e:
            result = False
            print(e)
        else:
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return result

    def __get_one_record(self, sql=None, params=None):
        """
        :param sql: str
        :param params: tuple
        :return: tuple
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            if sql and params:
                result = cursor.execute(sql, params).fetchone()
            else:
                result = cursor.execute(sql).fetchone()
        except Exception as e:
            result = False
            print(e)
        else:
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return result

    def __get_success_operation(self, sql, params):
        """
        :param sql: str
        :param params: tuple
        :return: bool
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            result = cursor.execute(sql, params)
        except Exception as e:
            result = False
            print(e)
        else:
            result = True
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return result
