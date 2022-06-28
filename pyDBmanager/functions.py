from collections import namedtuple


def get_namedtuple_from_data(data_fetch, data_description):
    _namedtuple = namedtuple("data", [data_description[i][0] for i in range(len(data_description))])
    if len(data_fetch) == 1:
        result = _namedtuple(*data_fetch[0])
    else:
        result = [_namedtuple(*item) for item in data_fetch]
    return result


def get_operation(sql):
    """
    :param sql: str
    :return: bool
    """
    if sql.startswith("SELECT"):
        return True
    return False
