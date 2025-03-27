from decouple import config
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=config('HOST_PGSQL'),
        database=config('NAME_PGSQL'),
        user=config('USER_PGSQL'),
        password=config('PASS_PGSQL')
    )
    return conn