import sqlite3
import mysql.connector
from prettytable import from_db_cursor

from .functions import *


class BaseDB(object):
    """
    :type _is_select: bool
    """
    _is_select = False

    def execute_sql(self, show=False, named_tuple=False):
        """
        :param named_tuple: bool
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
                self._is_select = get_operation(sql)
                result = self._executor(sql, params, *(show, named_tuple))
                return result
            return main
        return wrapper

    def _check_default_params(self, cursor, *args):
        if args[0]:
            result = from_db_cursor(cursor)
        elif args[1]:
            result = get_namedtuple_from_data(cursor.fetchall(), cursor.description)
        else:
            result = cursor.fetchall()
        return result

    def _executor(self, sql, params, *args):
        pass

    def _connect(self):
        pass


class SqliteDB(BaseDB):

    def __init__(self, **kwargs):
        if "db_name" in kwargs:
            self.db_name = kwargs.get("db_name")

    def _executor(self, sql, params, *args):
        """
        :param sql: str
        :param params: tuple
        :return: list|bool|str
        """
        connection = cursor = None
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute(sql, params)
            if self._is_select:
                result = self._check_default_params(cursor, *args)
        except Exception as e:
            print(e)
            result = False
        else:
            result = result if self._is_select else True
            connection.commit()
        finally:
            # cursor.close()
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

    def _executor(self, sql, params, *args):
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
            if self._is_select:
                result = self._check_default_params(cursor, *args)
        except Exception as e:
            print(e)
            result = False
        else:
            result = result if self._is_select else True
            connection.commit()
        finally:
            # cursor.close()
            connection.close()
        return result
