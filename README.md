# sbercloud-api-aksk
Signs API calls to SberCloud.Advanced with AK/SK  

This script is a courtesy of @sadpdtchr

### Description

Sometimes there is a need to manuall call SberCloud.Advanced API of a certain cloud service.  
According to the [documentation](https://support.hc.sbercloud.ru/api/ecs/en-us_topic_0124306062.html), a request can be authenticated either by a temporary security token or by Access Key and Secret Key (AK/SK).  
This script implements the second option: it signs the request with AK/SK.
It uses the standard Python SDK for that available [here](https://support.huaweicloud.com/intl/en-us/devg-apig/apig-dev-180307016.html).  

### Usage 

$ python3 api_ak_sk.py -h
usage: api_ak_sk.py [-h] --uri URI --method METHOD --ak AK --sk SK [--content CONTENT] [--xdomainid XDOMAINID]

Makes SberCloud.Advanced API call signed by AK and SK.

Arguments:
  -h, --help              show this help message and exit
  --uri URI               URI for the call. Includes cloud service endpoint and URI. May include Project ID for some calls
  --method METHOD         REST method, see API description for your cloud service
  --ak AK                 Access Key
  --sk SK                 Secret Key
  --content CONTENT       File with request content in JSON format, optional
  --xdomainid XDOMAINID   Root account id (X-Domain-Id), optional

### Dependencies

### Installation

