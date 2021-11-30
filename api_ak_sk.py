#!/usr/bin/env python3

from typing import TYPE_CHECKING
from apig_sdk import signer

import requests
import warnings
import argparse
import json
import pprint


warnings.filterwarnings('ignore')


def call_wrapper(access_key, secret_key, method, uri, xdomainid, request_content_file):
    """
    Calls SberCloud.Advanced API and signs the request with AK/SK
    Inputs:
        - access_key: Access Key, string
        - secret_key: Secret Key, string
        - method: REST method that will be executed. Most often it will be GET or POST, string
        - uri: request URI is in the following format: {URI-scheme}://{Endpoint}/{resource-path}?{query-string}, string. For example, https://ecs.ru-moscow-1.hc.sbercloud.ru/v1/{project_id}/cloudservers
        - xdomainid: X-Domain-Id of the root account (required for some IAM-related services), string
        - request_content_file: name of the file, which contains request body in JSON format, string
    Outputs:
        - none
    """

    # Initialize HuaweiCloud signer
    sig = signer.Signer()

    # Assign AK and SK
    sig.Key = access_key
    sig.Secret = secret_key

    # Read request from file and prepare the request body
    request_body = ""

    if request_content_file:
        with open(request_content_file) as jsonfile:
            js = json.load(jsonfile)

        request_body = json.dumps(js)

    # Construct request
    if xdomainid:
        r = signer.HttpRequest(method,
                            uri,
                            {"Content-Type": "application/json", "X-Domain-Id": xdomainid},
                            request_body)
    else:
        r = signer.HttpRequest(method,
                            uri,
                            {"Content-Type": "application/json"},
                            request_body)

    # Sign request
    sig.Sign(r)

    # Execute request and print results
    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
    print(resp.status_code)
    pprint.pprint(resp.json())

    return True


if __name__ == "__main__":
    # If executed from CLI, parse arguments    
    parser = argparse.ArgumentParser(description='Makes SberCloud.Advanced API call signed by AK and SK.')
    parser.add_argument("--uri", help="URI for the call. Includes cloud service endpoint and URI. May include Project ID for some calls", required=True)
    parser.add_argument("--method", help="REST method, see API description for your cloud service", required=True)
    #parser.add_argument("--project", help="Project ID, you can find it in the management console", required=True)
    parser.add_argument("--ak", help="Access Key", required=True)
    parser.add_argument("--sk", help="Secret Key", required=True)
    parser.add_argument("--content", help="File with request content in JSON format, optional")
    parser.add_argument("--xdomainid", help="Root account id (X-Domain-Id), optional")
    args = parser.parse_args()

    # Call main function, which does the job
    call_wrapper(args.ak, args.sk, args.method, args.uri, args.xdomainid, args.content)
