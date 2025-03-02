import json

import pytest

from hello_world import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


@pytest.fixture()
def tweet_event():
    """ Generates Tweet Event with HTML content """
    
    return {
        "body": '<blockquote class="twitter-tweet">\n  <p lang="en" dir="ltr">テストツイート本文\n#NEEDY_pic https://t.co/ItIsVAWSlQ</p>\n  &mdash; テストユーザー (@test_user)\n  <a href="https://twitter.com/test_user/status/123456789">Jan 24, 2025</a>\n</blockquote>\n<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n',
        "resource": "/hello",
        "path": "/hello/",
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "headers": {
            "Content-type": "application/json",
            "User-Agent": "Amazon CloudFront",
            "Host": "example.com"
        },
        "requestContext": {
            "resourceId": "shd55o",
            "resourcePath": "/hello",
            "httpMethod": "POST",
            "path": "/Prod/hello/",
            "protocol": "HTTP/1.1",
            "stage": "Prod"
        }
    }


@pytest.fixture()
def array_tweet_event():
    """ Generates Array of Tweet Events """
    
    return [{
        "body": '<blockquote class="twitter-tweet">\n  <p lang="en" dir="ltr">配列形式のテストツイート\n#NEEDY_pic https://t.co/ItIsVAWSlQ</p>\n  &mdash; テストユーザー (@test_user)\n  <a href="https://twitter.com/test_user/status/123456789">Jan 24, 2025</a>\n</blockquote>\n<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n',
        "resource": "/hello",
        "path": "/hello/",
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "headers": {
            "Content-type": "application/json",
            "User-Agent": "Amazon CloudFront",
            "Host": "example.com"
        },
        "requestContext": {
            "resourceId": "shd55o",
            "resourcePath": "/hello",
            "httpMethod": "POST",
            "path": "/Prod/hello/",
            "protocol": "HTTP/1.1",
            "stage": "Prod"
        }
    }]


def test_lambda_handler(apigw_event):
    """ 基本的なレスポンスのテスト """
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"


def test_tweet_text_extraction(tweet_event):
    """ ツイートテキスト抽出機能のテスト """
    ret = app.lambda_handler(tweet_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "tweet_text" in data
    assert data["tweet_text"] == "テストツイート本文\n#NEEDY_pic https://t.co/ItIsVAWSlQ"


def test_array_event_handling(array_tweet_event):
    """ 配列形式のイベント処理のテスト """
    ret = app.lambda_handler(array_tweet_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "tweet_text" in data
    assert data["tweet_text"] == "配列形式のテストツイート\n#NEEDY_pic https://t.co/ItIsVAWSlQ"
