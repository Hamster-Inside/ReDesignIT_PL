import psycopg2
from psycopg2 import sql
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def create_database(db_name_to_create, username_to_create, password_to_create):
    try:
        # Connect to the default PostgreSQL database (e.g., 'postgres')
        conn = psycopg2.connect(
            dbname="postgres",
            user=getenv('ADMIN_POSTGRESQL'),
            password=getenv('ADMIN_POSTGRESQL_PASSWORD'),
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Create a new database
        cursor.execute(sql.SQL("CREATE DATABASE {} ENCODING 'UTF8'").format(
            sql.Identifier(db_name_to_create)
        ))
        print("Database '{}' created successfully.".format(db_name_to_create))

        # Create a new user and grant privileges
        cursor.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s").format(
            sql.Identifier(username_to_create)
        ), (password_to_create,))
        print("User '{}' created successfully.".format(username_to_create))

        # Set client encoding, default transaction isolation, and timezone for the user
        cursor.execute(sql.SQL("ALTER ROLE {} SET client_encoding TO 'utf8'").format(
            sql.Identifier(username_to_create)
        ))
        cursor.execute(sql.SQL("ALTER ROLE {} SET default_transaction_isolation TO 'read committed'").format(
            sql.Identifier(username_to_create)
        ))
        cursor.execute(sql.SQL("ALTER ROLE {} SET timezone TO 'UTC'").format(
            sql.Identifier(username_to_create)
        ))
        print("Client encoding, default transaction isolation, and timezone set for user '{}'.".format(username_to_create))

        cursor.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
            sql.Identifier(db_name_to_create),
            sql.Identifier(username_to_create)
        ))
        print("Privileges granted to user '{}' on database '{}'.".format(username_to_create, db_name_to_create))

        cursor.execute(sql.SQL("ALTER DATABASE {} OWNER TO {}").format(
            sql.Identifier(db_name_to_create),
            sql.Identifier(username_to_create)
        ))
        print("Ownership to the db '{}' given to '{}'.".format(db_name_to_create, username_to_create))

    except psycopg2.Error as e:
        print("Error: ", e)
    finally:
        # Close communication with the PostgreSQL database server
        if conn is not None:
            cursor.close()
            conn.close()


db_name_prod = getenv('DJANGO_DB')
username_prod = getenv('DJANGO_DB_USER')
password_prod = getenv('DJANGO_DB_PASSWORD')

db_dev_test_name = 'localtestdb_redesignit'
db_dev_test_username = 'testuser_redesignit'
db_dev_test_password = 'TestPassword'

# create_database(db_name_prod, username_prod, password_prod)  # comment out if need just dev db
create_database(db_dev_test_name, db_dev_test_username, db_dev_test_password)  # comment out if need prod db
