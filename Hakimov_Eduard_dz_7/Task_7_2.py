def n_project(tab, stryct, root):

    if tab != -1 and not os.path.exists(root):
        os.mkdir(root)
    os.chdir(root)
    n_save = []
    new_dir = None
    for i, (new_name, line_tab, is_dir) in enumerate(stryct):

        if new_dir:
            if new_dir[1] < line_tab:
                n_save.append((new_name, line_tab, is_dir))
                if i == len(stryct) - 1:
                    n_project(new_dir[1], n_save,
                                 os.path.join(root, new_dir[0]))
            elif new_dir[1] == line_tab and is_dir:
                n_project(new_dir[1], n_save,
                             os.path.join(root, new_dir[0]))
                os.chdir(root)
                inside_dir = (new_name, line_tab)
                n_stryct = []
            else:
                if not is_dir:
                    n_save.append((new_name, line_tab, is_dir))

                n_project(new_dir[1], n_save,
                             os.path.join(root, new_dir[0]))
                os.chdir(root)
                inside_dir = (new_name, line_tab) if is_dir else None

        elif is_dir:
            inside_dir = (new_name, line_tab)
        else:
            open(new_name, "a").close()



if __name__ == "__main__":


    import os

    # image if file not big
    with open("./config.yaml", "r", encoding="utf-8") as conf_text:
        conf = map(lambda x: (
            x.strip().replace("\t", "  ").replace(":", ""),
            x.rstrip().count(" "),
            x.find(":") > 0
        ), conf_text.readlines())

    n_project(-1, list(conf), os.getcwd())

    exit(0)