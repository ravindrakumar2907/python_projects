from flask import Flask, redirect, url_for, jsonify, request
import json
"""
https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module
"""
import logging
from emp_service import *

from app_msg import *

app = Flask(__name__)

log_file_name = "emp_app.log"
logging.basicConfig(filename=log_file_name,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('RestAPP')


@app.route('/')
def server_check():
    logger.info("Server status check")
    return create_response(SUCCESS, SERVER_HEALTH_STATUS)


# https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
@app.route('/getAllEmployee', methods=['GET'])
def get_all_employee():
    if request:
        args = request.args
        if args and is_valid_user(args):
            logger.info("get all employee")
            return jsonify(get_all_employee_data())  # josn.dump(get_all_employee_data())
            # return json.dumps(get_all_employee_data())
        else:
            return create_response(FAILED, INVALID_USER)
    else:
        return create_response(FAILED, MISSING_DATA)


@app.route('/registerEmployee', methods=['POST'])
def register_employee():
    logger.info("register_employee method")
    if request:
        args = request.args
        if args and is_valid_user(args):
            print("processing input" + str(request.json))
            status = register_employee_data(request.json)
            if status:
                logger.debug("employee has been registered successfully.")
                return create_response(SUCCESS, REGISTERED)
            else:
                logger.debug("employee failed to register")
                return create_response(FAILED, REGISTERED_FAILED)
        else:
            return create_response(FAILED, INVALID_USER)

    logger.debug(MISSING_DATA)
    return create_response(FAILED, MISSING_DATA)



@app.route('/updateEmployee/<email>', methods=['PUT'])
def update_employee(email):
    logger.info("update_employee method")
    if request:
        args = request.args
        if args and is_valid_user(args):
            print("processing input" + str(request.json))
            status = update_employee_data(request.json, email)
            if status:
                logger.debug("employee has been updated successfully.")
                return create_response(SUCCESS, UPDATED)
            else:
                logger.debug("employee failed to update")
                return create_response(FAILED, UPDATED_FAILED)
        else:
            return create_response(FAILED, INVALID_USER)

    logger.debug(MISSING_DATA)
    return create_response(FAILED, MISSING_DATA)


@app.route('/deleteEmployee/<email>', methods=['DELETE'])
def delete_employee(email):
    logger.info("delete_employee method")
    if request:
        args = request.args
        if args and is_valid_user(args):
            if email:
                status = delete_employee_data(email)
                if status:
                    logger.debug("employee has been deleted successfully.")
                    return create_response(SUCCESS, DELETED)
                else:
                    logger.debug("employee failed to delete")
                    return create_response(FAILED, DELETED_FAILED)
            logger.debug(MISSING_DATA_EMAIL)
            return create_response(FAILED, MISSING_DATA_EMAIL)
        else:
            return create_response(FAILED, INVALID_USER)


@app.route('/getEmployee/<email>', methods=['GET'])
def get_employee(email):
    if request:
        args = request.args
        if args and is_valid_user(args):
            logger.info("get_employee method")
            if email:
                emp_data = get_employee_data(email)
                if emp_data:
                    logger.debug("employee found")
                    return emp_data
                else:
                    logger.debug("employee not found")
                    return create_response(FAILED, EMAIL_NOT_VALID)

            logger.debug(MISSING_DATA_EMAIL)
            return create_response(FAILED, MISSING_DATA_EMAIL)
        else:
            return create_response(FAILED, INVALID_USER)



if __name__ == '__main__':
    #app.run()
    logging.info("Starting app")
    app.run(host="localhost", port="5000", debug=True)
    logging.info("Started app")
    """app.run(host="0.0.0.0", port="5001", debug=True)"""
    """##app.add_url_rule(‘/’, ‘hello’, hello_world)"""

"""
GET http://localhost:5000/getAllEmployee
POST http://localhost:5000/registerEmployee
PUT http://localhost:5000/updateEmployee
DELETE http://localhost:5000/deleteEmployee
GET http://localhost:5000/getEmployee
"""
