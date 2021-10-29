import re


def read_html(file_name):

    with open(file_name, 'r', encoding='utf-8') as input:
        html=''
        for line in input:
            html+=line
    return html


def upper_case(match_obj):

    return match_obj.group(0).upper()


def lower_case(match_obj):

    return match_obj.group(0).lower()


def parse_elements(html, option):

    comments = str(re.findall(r'(<!--[\w\d\s.]*-->)', html))
    print(re.sub(r"\['|']", "", re.sub(r"\\n", " ", comments)))

    elements = re.findall(r'</?[^!][\w\W]*?>', html)
    parsed_elements = []

    for element in elements:
        if option == 1:
            parsed_elements.append(re.sub(r'</?[\w]+| [\w-]+?=', upper_case, element))
        elif option == 2:
            parsed_elements.append(re.sub(r'</?[\w]+| [\w-]+?=', lower_case, element))
        else:
            print("Wrong option")
            break

    return parsed_elements


if __name__ == "__main__":
    #INPUT
    file_name = "python.html"

    # SIZE OPTIONS
    # 1 - UPPER
    # 2 - lower
    size = 2

    html = read_html(file_name)

    done_html = parse_elements(html, size)

    for element in done_html:
        print(element)
