import os

notepad = {
    "my_project": [
        {
            "settings": [],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project_starter(pth, struct):

    for key, value in struct.items():

        save_notepad = os.path.join(pth, key)

        if not os.path.exists(save_notepad):
            os.mkdir(save_notepad)

        if len(value) > 0:
            for node in value:
                project_starter(save_notepad, node)


if __name__ == "__main__":

    project_starter(os.getcwd(), struct=notepad)