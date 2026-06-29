from datetime import datetime


def calculator(expression):

    try:

        result = eval(expression)

        return str(result)

    except:

        return "Calculation Error"


def current_time():

    return str(datetime.now())