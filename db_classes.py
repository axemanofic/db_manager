import sqlite3
import mysql.connector
from prettytable import from_db_cursor


class BaseDB(object):
    """
    :type _isSelect: bool
    """
    _isSelect = False

    def execute_sql(self, show=False):
        """
        :param show: bool
        :return: void
        """
        def wrapper(get_query):
            """
            :param get_query: function
            :return: function
            """
            def main(*args):
                """
                :param args: tuple
                :return: list|bool|str
                """
                params = ()
                try:
                    sql, params = get_query(*args)
                except ValueError:
                    sql = get_query()
                self._isSelect = self.__get_operation(sql)
                result = self._executor(sql, params, show)
                return result
            return main
        return wrapper

    def __get_operation(self, sql):
        """
        :param sql: str
        :return: bool
        """
        if sql.startswith("SELECT"):
            return True
        return False

    def _executor(self, sql, params, show):
        pass

    def _connect(self):
        pass


class SqliteDB(BaseDB):

    def __init__(self, **kwargs):
        if "db_name" in kwargs:
            self.db_name = kwargs.get("db_name")

    def _executor(self, sql, params, show):
        """
        :param sql: str
        :param params: tuple
        :param show: bool
        :return: list|bool|str
        """
        connection = cursor = None
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute(sql, params)
            if self._isSelect:
                if show:
                    result = from_db_cursor(cursor)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            print(e)
            result = False
        else:
            result = result if self._isSelect else True
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return result


class MysqlDB(BaseDB):

    def __init__(self, **kwargs):
        if "db_name" in kwargs:
            self.db_name = kwargs.get("db_name")
        if "username" in kwargs:
            self.username = kwargs.get("username")
        if "password" in kwargs:
            self.password = kwargs.get("password")
        if "host" in kwargs:
            self.host = kwargs.get("host")
        else:
            self.host = '127.0.0.1'
        if "port" in kwargs:
            self.port = kwargs.get("port")
        else:
            self.port = 3306

    def _executor(self, sql, params, show):
        """
        :param sql: str
        :param params: tuple
        :param show: bool
        :return: list|bool|str
        """
        connection = cursor = None
        try:
            connection = mysql.connector.connect(database=self.db_name, user=self.username, password=self.password,
                                                 port=self.port, host=self.host)
            cursor = connection.cursor()
            cursor.execute(sql, params)
            if self._isSelect:
                if show:
                    result = from_db_cursor(cursor)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            result = False
            print(e)
        else:
            result = result if self._isSelect else True
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return result
