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
    except Exeption as error:
        result["error"] = error
        return(result)


# Also can use this alone
if __name__ == "__main__":
    info_str = input("Enter your list carefully: ")
    special_key = input("Enter what key of this list you want categorize (Exp: country): ")
    try:
        info_list = json.loads(info_str)
        result = categorize(info_list=info_list, special_key=special_key)
        print(f"{result=}")
    except Exception as error:
        result = {"error": error}
        print(f"{result=}")
