import sys
import logging
from db.user_db_operation import UserDbOperations
from db.mysql_connection import MySQLConnector

""" This file / module is for utility function"""
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def print_all_options():
    logging.info("Choose option to do the operation.")
    logging.info("\n 1. Add \n 2. update \n 3. select  \n 4. select by id  \n 5. delete \n 6. exit ")


def take_option():
    user_option = None
    try:
        user_option = int(input("Enter The option: "))
        return user_option
    except Exception as e:
        raise Exception("Option input is not valid")


def user_input():
    print_all_options()
    user_option = take_option()
    logging.info("Selected option is: " + str(user_option))
    do_operation(user_option)

def do_operation(option):
    if option == 1:
        logging.info("Going for add")
        add()
        user_input()
    elif option == 2:
        logging.info("Going for update")
        update()
        user_input()
    elif option == 3:
        logging.info("Going for select")
        selectAll()
        user_input()
    elif option == 4:
        logging.info("Going for select by id")
        selectById()
        user_input()
    elif option == 5:
        logging.info("Going for delete")
        delete()
        user_input()
    elif option == 6:
        logging.info("STOP Request for program")
        sys.exit()
    else:
        logging.info("InValid option chosen..")
        print_all_options()
        take_option()


def add():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    UserDbOperations.insert_student(name, email)
    logging.info("success.")

def update():
    id = input("Enter id: ")
    name = input("Enter Name: ")
    UserDbOperations.update_student(name, id)
    logging.info("success.")

def delete():
    id = input("Enter id: ")
    UserDbOperations.delete_student(id)
    logging.info("success.")

def selectById():
    id = input("Enter id: ")
    UserDbOperations.get_user(id)
    logging.info("success.")

def selectAll():
    UserDbOperations.get_all_student()
    logging.info("success.")
