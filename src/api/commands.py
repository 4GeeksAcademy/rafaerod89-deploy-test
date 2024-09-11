
import click
from api.models import db, User

def insert_test_users(count):
    print("Creating test users")
    for x in range(1, int(count) + 1):
        user = User()
        user.email = "test_user" + str(x) + "@test.com"
        user.password = "123456"
        user.is_active = True
        db.session.add(user)
        db.session.commit()
        print("User: ", user.email, " created.")

    print("All test users created")

def insert_test_data():
    insert_test_users(5)
    pass

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    @app.cli.command("insert-test-data")
    def insert_test_data_command():
        insert_test_data()
        pass