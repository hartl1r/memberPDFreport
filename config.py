# congif.py

import os
import pyodbc
import urllib

from dotenv import load_dotenv

# load dotenv in the base directory
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

params = urllib.parse.quote_plus('DRIVER=' + os.getenv('Driver') + ';'
                                 'SERVER=' + os.getenv('Server') + ';'
                                 'DATABASE=' + os.getenv('Database') + ';'
                                 'UID=' + os.getenv('Username') + ';'
                                 'PWD=' + os.getenv('Password') + ';'
                                 )

conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

class Config(object):
    SQLALCHEMY_DATABASE_URI = conn_str
    SQLALCHEMY_TRACK_MODIFICATIONS = False