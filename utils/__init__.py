from decimal import Decimal
import datetime
import collections
import json
from operator import itemgetter
from django.http import HttpResponse
from django.db import connection


def json_custom_parser(obj):
    """
        A custom json parser to handle json.dumps calls properly for Decimal and Datetime data types.
    """
    if isinstance(obj, Decimal):
        return float(obj)
    elif not isinstance(obj, basestring) and isinstance(obj, collections.Iterable):
        return list(obj)
    elif isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19 # 'YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM'.find('.')
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)


def json_response(data, status=200):
    return HttpResponse(
        json.dumps(data, default=json_custom_parser),
        content_type='application/json',
        status=status)


def fetchall(query, params=None):
    "Returns all rows from a cursor"
    if params is None:
        params = ()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cursor.close()


def execute(query, params=None, conn=connection):
    "Executes a query"
    if params is None:
        params = ()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
    finally:
        cursor.close()


def dictfetchall(query, params=None, conn=connection):
    """Returns all rows from a cursor as a dict"""
    if params is None:
        params = ()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        keys = [col[0] for col in cursor.description]
        x = [
            dict(zip(keys, row))
            for row in cursor.fetchall()
        ]
        return x
    finally:
        cursor.close()


def pluck(lst, *keys):
    return map(itemgetter(*keys), lst)


def find_where(lst, **kwargs):
    for val in lst:
        for k, v in kwargs.items():
            if val.get(k) != v:
                break # not a match
        else: # Every k,v matches.
            return val
    return None
