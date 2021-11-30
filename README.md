# sbercloud-api-aksk
Signs API calls to SberCloud.Advanced with AK/SK  

This script is a courtesy of @sadpdtchr

## Description

Sometimes there is a need to manuall call SberCloud.Advanced API of a certain cloud service.  
According to the [documentation](https://support.hc.sbercloud.ru/api/ecs/en-us_topic_0124306062.html), a request can be authenticated either by a temporary security token or by Access Key and Secret Key (AK/SK).  
This script implements the second option: it signs the request with AK/SK.
It uses the standard Python SDK for that available [here](https://support.hc.sbercloud.ru/devg/apisign/api-sign-sdk-python.html).  

## Usage 

$ python3 api_ak_sk.py -h  
usage: api_ak_sk.py [-h] --uri URI --method METHOD --ak AK --sk SK [--content CONTENT] [--xdomainid XDOMAINID]  
  
Makes SberCloud.Advanced API call signed by AK and SK.  
  
Arguments:  
&emsp;-h, --help              &emsp;&emsp;show this help message and exit  
&emsp;--uri URI               &emsp;&emsp;URI for the call. Includes cloud service endpoint and URI. May include Project ID for some calls  
&emsp;--method METHOD         &emsp;&emsp;REST method, see API description for your cloud service  
&emsp;--ak AK                 &emsp;&emsp;Access Key  
&emsp;--sk SK                 &emsp;&emsp;Secret Key  
&emsp;--content CONTENT       &emsp;&emsp;File with request content in JSON format, optional  
&emsp;--xdomainid XDOMAINID   &emsp;&emsp;Root account id (X-Domain-Id), optional  

## Examples

### Example 1: GET call to get list of ELB (Elastic Load Balancer)

You don't need any request body for this GET request, so you can omit the content parameter. You don't need the xdomainid parameter as well.  

$ python3 api_ak_sk.py --ak **Your_AK_here** --sk **Your_SK_here** --method GET --uri https://elb.ru-moscow-1.hc.sbercloud.ru/v2/<b>Your_Project_ID_here</b>/elb/loadbalancers  

This is how your request should look like:  

$ python3 api_ak_sk.py --ak A5...CL --sk mn...gj --method GET --uri https://elb.ru-moscow-1.hc.sbercloud.ru/v2/07...ef/elb/loadbalancers

### Example 2: POST call to create new ECS

Here you need to provide the request body, which will describe your ECS:

$ python3 api_ak_sk.py --ak **Your_AK_here** --sk **Your_SK_here** --method POST --uri https://ecs.ru-moscow-1.hc.sbercloud.ru/v1/<b>Your_Project_ID_here</b>/cloudservers --content ecs.json

### Example 3: POST call to create new custom IAM policy

This very call (as well as some other IAM-related calls) requires you to provide the domain id of your root account, even if you execute this call from under the root account itself. Thus you must add the xdomainid parameter:

$ python3 api_ak_sk.py --ak **Your_AK_here** --sk **Your_SK_here** --method POST --uri https://iam.ru-moscow-1.hc.sbercloud.ru/v3.0/OS-ROLE/roles --content policy.json --xdomainid **Your_Domain_ID_here**

## Dependencies

The script requires python3 with the following modules:

- typing
- requests
- argparse
- json
- pprint
- apig_sdk (you get this one from [here](https://support.hc.sbercloud.ru/devg/apisign/api-sign-sdk-python.html))

## Installation

Just clone the repo. Install [apig_sdk](https://support.hc.sbercloud.ru/devg/apisign/api-sign-sdk-python.html). Then execute the script as shown earlier:

$ python3 api_ak_sk.py -h

Or, you could make it executable:

$ chmod u+x api_ak_sk.py  
$ ./api_ak_sk.py -h
