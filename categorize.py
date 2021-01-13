#!/usr/bin/env python3


# Include necessary modules: {json}
import json


# Categorize a given list of some information with a special key like "country"
def categorize(info_list: list, special_key: str):
    result = dict()
    try:
        for info in info_list:
            value = info[special_key]
            if value in result:
                result[value] += 1
            else:
                result[value] = 1
        return(result)
    except Exception as error:
        result["error"] = error
        return(result)


# Also can use this alone
if __name__ == "__main__":
    info_file_addr = input("Enter your information file list address (exp: './information-ips.json'): ")
    special_key = input("Enter what key of this list you want categorize (Exp: country): ")
    try:
        with open(file=info_file_addr, mode='r') as f:
            info_list = json.load(fp=f)
            f.close()
            result = categorize(info_list=info_list, special_key=special_key)
            print(f"{result=}")
    except Exception as error:
        result = {"error": error}
        print(f"{result=}")
