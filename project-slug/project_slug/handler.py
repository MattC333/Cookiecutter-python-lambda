import sys


def execute(event, context):
    return "Hello from AWS Lambda using Python" + sys.version + "!"
