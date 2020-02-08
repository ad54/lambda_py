"""This is a aws lambda function, will generate hotel bill amount based 
on multiple parameters.It will display the logs of function."""

import json

def lambda_handler(event, context):
    # Call the event of the bill calculation
    hotel_bill = calculate_bill(event)
    # Call the display logs function
    display_logs(context)
    # Return the hotel bill
    return {
        'message' : hotel_bill
    }


def calculate_bill(event):
    """Calculate bill amount"""
    # number of the day stay
    day_stay = int(event['day_stay'])
    # number of person
    num_person = int(event['num_person'])
    # per day rate of hotel
    per_day_rate = int(event['per_day_rate'])
    # calculating bill amount
    bill_amount = day_stay * num_person * per_day_rate
    # generating hotel bill amount
    hotel_bill = f"The {num_person} person(s) stayed for {day_stay} day(s) so as per perday rate $({per_day_rate}) your total bill amount is : ${bill_amount}"
    # return hotel bill amount
    return hotel_bill


def display_logs(context):
    """give logs of the request"""
    print("request id is : ", context.aws_request_id)
    print("mem. limits(MB):", context.memory_limit_in_mb)
    print("log stream name is : ", context.log_stream_name)
    print("millis is : ",context.get_remaining_time_in_millis())
    print("log group name is : ", context.log_group_name)
    print("name of  function invoked is : ", context.function_name)
