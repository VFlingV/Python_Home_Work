import os
import json

from itertools import zip_longest


def prepare_dataset(user,hobby):


    output_pth = "task_6_3_result.json"
    if not (os.path.isfile(user) or
            os.path.isfile(hobby)):
        return -1

    user_lines = None
    hobby_lines = None

    with open(user, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    with open(hobby, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1

    group = {}

    for name, hobby in zip_longest(user_lines, hobby_lines):
        name = name.replace("\n", "")
        group[name] = hobby.replace("\n", "") if hobby else None

    with open(output_pth, "w+", encoding="utf-8") as out_file:
        json.dump(group, out_file)  # out_file.writelines(json.dumps(group))

    return 0



exit(prepare_dataset("users.csv","hobby.csv"))