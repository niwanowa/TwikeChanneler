import json
import logging
import os
import sys

# import requests

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add stdout handler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    logger.info("## EVENT")
    logger.info(event)

    # Log request URI
    if "requestContext" in event and "http" in event["requestContext"]:
        request_uri = event["requestContext"]["http"].get("path", "N/A")
        logger.info(f"Request URI: {request_uri}")
    else:
        logger.info("Request URI: N/A")

    # Log query parameters
    if "queryStringParameters" in event and event["queryStringParameters"]:
        query_params = event["queryStringParameters"]
        logger.info(f"Query Parameters: {query_params}")
    else:
        logger.info("Query Parameters: N/A")

    # Log request body
    if "body" in event and event["body"]:
        try:
            request_body = json.loads(event["body"])
            logger.info(f"Request Body: {request_body}")
        except json.JSONDecodeError:
            logger.info(f"Request Body: {event['body']}")
    else:
        logger.info("Request Body: N/A")

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
