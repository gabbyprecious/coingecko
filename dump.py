# price_row = table_body_row.find("td", class_="td-price price text-right")
#     price = price_row.span.text
#     # strip all new lines
#     price = price.strip("\n")


# one_hr_change_row = table_body_row.find(
#     "td", class_="td-change1h change1h stat-percent text-right col-market"
# )
# one_hr_change = one_hr_change_row.span.text
# one_hr_change = one_hr_change.price.strip("\n")


# for change in percentage_changes:
#     class_name = change[1]
#     data = get_data(class_name, table_body_row)
#     data = func()
#     change.append(data)
# print(percentage_changes)

# change_1hr = get_data(
#     table_body_row, "td", "td-change1h change1h stat-percent text-right col-market"
# )
# change_1hr = convert_str_to_float(change_1hr, "%")

# change_24hr = get_data(
#     table_body_row,
#     "td",
#     "td-change24h change24h stat-percent text-right col-market",
# )
# change_24hr = convert_str_to_float(change_24hr, "%")

# change_7d = get_data(
#     table_body_row, "td", "td-change7d change7d stat-percent text-right col-market"
# )

# change_7d = convert_str_to_float(change_7d, "%")


# changes = {
#     "change_1hr": "td-change1h change1h stat-percent text-right col-market",
#     "change_24hr": "td-change1h change1h stat-percent text-right col-market",
#     "change_7d": "td-change7d change7d stat-percent text-right col-market",
# }

# price = get_data(table_body_row, "td", "td-price price text-right")

# price = convert_str_to_float(price, "$", True)


# with open("myfile.txt", "w") as write:
    #     write.writelines(str(full_coin_name))

    # with open("myfile.txt", "w") as crypto_file:
    #     filed_names = headers
    #     csv_writer = csv.DictWriter(crypto_file, fieldnames=headers, delimeter="\t")

    # writer.writelines(str(table_headers))