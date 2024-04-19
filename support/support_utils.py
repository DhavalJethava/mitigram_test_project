
def parse_str_table(table_with_headers):
    list_table_rows = table_with_headers.split("\n")
    list_headers = str(list_table_rows[0]).strip("|").split("|")
    dict_table = {}
    for header in list_headers:
        header_text = header.strip()
        lst_row = []
        for i in range(1, list_table_rows.__len__()):
            list_temp = list_table_rows[i].strip("|").split("|")
            lst_row.append(list_temp[list_headers.index(header)].strip())

        dict_table[header_text] = lst_row

    return dict_table
