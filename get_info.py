#!/usr/bin/env python3

# Include necessary modules '{requests, json}'
import requests, json

# Get information from given IP 
def get_information(ip: str, fields: list):
    base_url = "http://ip-api.com/json"
    url = f"{base_url}/{ip}"
    list_fields = (',').join(fields)
    params = {"fields": list_fields}
    try:
        response = requests.get(url=url, params=params)
        return(response.json())
    except Exception as error:
        result = {"status": "fail", "message": error}
        return result

# Also can use this alone
if __name__ == "__main__":
    ip = input("Enter the IP (Exp: 123.45.67.89): ")
    fields_str = input("Enter fields. cut only with ','. Leave this empty if you want default:\n")
    if not fields_str:
        fields_str = "status,message,country,countryCode,region,regionName,city,isp,org,as,query"
    fields = fields_str.split(',')
    result = get_information(ip=ip, fields=fields)
    print(f"{result=}")
