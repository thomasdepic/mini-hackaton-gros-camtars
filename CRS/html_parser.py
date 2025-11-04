

from bs4 import BeautifulSoup
import os




def extract_all_fields(html_content):
    if hasattr(html_content, 'read'):
        html_content = html_content.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    result = []

    for row in soup.find_all('tr'):
        td = row.find('td', class_='l m linecontent')
        if td:
            text = td.get_text(separator='|', strip=True)
            fields = {}
            parts = text.split('|')
            for part in parts:
                if ':' in part:
                    key, value = part.split(':', 1)
                    value = value.replace("\xa0", " ")
                    key = key.replace("\xa0", " ")
                    fields[key.strip()] = value.strip()
            if fields:
                result.append(fields)

    return result

# Parse file, extract relevant field, and return a list and a dictionnary{column_names : column_content}
def parse_html(filename="./mini-hackaton-gros-camtars/USCODE22_LLCP_102523.HTML"):
    cwd = os.getcwd()
    print("\n\n working directory")
    print(cwd)
    print("\n\n")
    print("opening file ...")
    with open(filename, "r", encoding = "ISO-8859-1") as file :
        html_content = file.read()
    print("File read\n")
    parsed = extract_all_fields(html_content)
    print("File parsed\n")
    # print(parsed[0])

    keys = []
    values = []
    datas = []

    for p in parsed :
        keys.append(p["SAS Variable Name"])
        values.append(p["Label"])
        #datas.append(p[""])

    parsed_dict = dict(zip(keys, values))
    #print(parsed_dict)
    return parsed, parsed_dict
