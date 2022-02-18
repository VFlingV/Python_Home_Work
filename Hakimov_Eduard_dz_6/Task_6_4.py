import os
import sys
from itertools import zip_longest


def gen(user, hobby):
    with open(user, "r", encoding="utf-8") as user_f, open(hobby, "r", encoding="utf-8") as hobby_f:
        for user, hobby in zip_longest(user_f, hobby_f):
            yield (user.removesuffix("\n"), hobby.removesuffix("\n") if hobby else None)


def prepare_dataset(output_pth, user, hobby):


    if not (os.path.isfile(user) or
            os.path.isfile(hobby)):
        return -1

    with open(output_pth, "w", encoding="utf-8") as out_file:
        for line in gen(user, hobby):
            print(f"{line[0]}: {line[1]}", file=out_file)

    return 0

if __name__ == "__main__":


    user_name = ""
    hobby_name = ""
    output_name = ""

    if len(sys.argv[1:]) >= 3:
        user_name = sys.argv[1]
        hobby_name = sys.argv[2]
        output_name = sys.argv[3]

    if not user_name:
        user_name = "users.csv"

    if not hobby_name:
        hobby_name = "hobby.csv"

    if not output_name:
        output_name = "users_hobby.txt"

    exit(prepare_dataset(user=user_name, hobby=hobby_name, output_pth=output_name))