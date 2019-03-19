import re


def load_file(file_name):
    """
    Takes a text file in utf8 encoding and returns a string list having new lines
    :param file_name: File Directory loaded from whatsapp
    :return: List of strings
    """
    f = open(file_name, encoding='utf8')
    split_lst = f.readlines()
    return split_lst


def parse_dataset(split_lst):
    """
    Takes a list of string and returns list of lists where each sub list has 4 objects of interest
    :param split_lst: List of string
    :return:list of lists having grouped strings
    """
    working_statements = 0
    not_working_statements = 0
    data_list = []

    for i in range(len(split_lst)):
        x = re.search(r"^(\d{2}\/\d{2}\/\d{2}), (\d+:\d{2} (am|pm)) - (.+): (.+)?(\n.*)*$", split_lst[i])

        if x is None and len(data_list) != 0:
            not_working_statements += 1
            data_list[-1][3] += "\n" + split_lst[i]

        if x is not None:
            working_statements += 1
            lst2 = [x.group(1), x.group(2), x.group(4), x.group(5), i]
            data_list.append(lst2)

    return data_list


def count_yo(data_list):
    """
    Takes a list of lists of string and returns the desired count of word of interest
    :param data_list: List of lists having grouped string
    :return: count of word of interest
    """
    count = 0
    for i in data_list:
        x = re.findall(r"(?=((\n|^|(\ ))yo+((\ )|$|\n)))", i[3], re.IGNORECASE)
        if len(x) is 0:
            print(i)

        if len(x) is not 0:
            matchCount = len(x)
            count += matchCount

    return count


if __name__ == "__main__":
    split_list = load_file("wchatad.txt")
    data_list = parse_dataset(split_list)
    count = count_yo(data_list)
    print(count)










