def get_cats_info(path):
    with open(path, encoding="utf-8") as cat_file:
        try:
            cats_lines = cat_file.readlines()
            keys = ["Id", "Name", "Age"]
            cats_list = []
            for line in cats_lines:
                cat_items = line.strip().split(",")
                cat_dict = {keys[0] : cat_items[0],
                            keys[1] : cat_items[1],
                            keys[2] : cat_items[2]
                            }
                cats_list.append(cat_dict)
            return cats_list
        except:
            return ""

a = get_cats_info("cats.txt")
print(a)