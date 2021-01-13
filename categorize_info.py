#!/usr/bin/env python3


# Include local necessary modules '{json}'
import json


# Include local necessary modules '{get_info, categorize}'
from get_info import get_information
from categorize import categorize

# Default values
DEFAULT_IPS_ADDRESS = "./banned-ips.list"
DEFAULT_FIELDS = ["status", "message", "country", "countryCode", "region",
                "regionName", "city", "isp", "org", "as", "query"]
DEFAULT_SPECIAL_KEY = "country"

# Categorize a list of information of some IP
def categorize_info(ips_addr: str=DEFAULT_IPS_ADDRESS,
                    fields: list=DEFAULT_FIELDS, special_key: str=DEFAULT_SPECIAL_KEY):
    try:
        ips_list = list()
        info_list = list()
        with open(file=ips_addr, mode='r') as f:
            ips_list = f.readlines()
            f.close()
        for ip in ips_list:
            fixed_ip = ip.strip()
            info = get_information(ip=fixed_ip, fields=fields)
            if info["status"] == "success":
                print(f"{fixed_ip} :: SUCCESS *")
                info_list.append(info)
            else:
                print(f"{fixed_ip} :: FAILED ! => {info['message']}")
        with open(file="information-ips.json", mode="w") as f:
            json.dump(fp=f, obj=info_list, indent=4)
            f.close()
        result = categorize(info_list=info_list, special_key=special_key)
        return(result)

    except Exception as error:
        result = {"error": error}
        return(result)


# Also can use this alone
if __name__ == "__main__":
    ips_address = input("Enter address of IP list file (default: './banned-ips.list'): ")
    fields_str = input("Enter fields. cut only with ','. Leave this empty if you want default:\n")
    special_key = input("Enter what key of this list you want categorize (default: 'country'): ")
    fields = list()
    if not ips_address:
        ips_address = DEFAULT_IPS_ADDRESS
    if not fields_str:
        fields = DEFAULT_FIELDS
    else:
        fields = fields_str.split(",")
    if not special_key:
        special_key = DEFAULT_SPECIAL_KEY
    try:
        result = categorize_info(ips_addr=ips_address, fields=fields, special_key=special_key)
        print(f"{result=}")
    except Exception as error:
        result = {"error": error}
        print(f"{result=}")
