from bs4 import BeautifulSoup
import csv
import requests
import time
from utils import (
    get_data,
    full_clean,
    convert_str_to_float,
    get_change,
    curry_function,
    get_nigerian_time,
)

while True:
    file_name = f"myfile{get_nigerian_time()}.csv"
    url = "https://www.coingecko.com/en"
    r = requests.get(url)
    headers = []

    if r.status_code == 200:
        # if status code is okay
        soup = BeautifulSoup(r.text, features="lxml")

        table_container = soup.find("div", class_="gecko-table-container")

        coin_table = table_container.find("div", class_="coingecko-table")
        # move through all the nested divs to actual table.
        coin_table = coin_table.div.div.table

        # table headers
        table_head = coin_table.thead

        table_head_row = table_head.tr
        table_headers = table_head_row.find_all("th")

        for header in table_headers:
            header_text = header.text
            if header_text != "":
                # skip over blank header
                header_text = full_clean(header_text)
                # remove new lines from each string
                headers.append(header_text)

        # print(headers)
        with open(file_name, "w") as crypto_file:
            csv_writer = csv.DictWriter(crypto_file, fieldnames=headers, delimiter="\t")
            # write the heaader
            csv_writer.writeheader()

        # table content
        table_body = coin_table.tbody
        table_body_rows = table_body.find_all("tr")

        for table_body_row in table_body_rows:

            # edit this to get all items
            # getting items on table
            coin_row = table_body_row.find("td", class_="py-0 coin-name")

            # two items match , select the second item
            coin_name_div = coin_row.find_all("div", class_="center")[1]

            full_coin_name = coin_name_div.find_all("a")[0].text
            coin_name_abv = coin_name_div.find_all("a")[1].text

            # strip new lines from data
            full_coin_name = full_coin_name.strip("\n")
            coin_name_abv = coin_name_abv.strip("\n")
            # coin = f"{full_coin_name}({coin_name_abv})"

            percentage_changes = (
                [
                    "change_1hr",
                    "td-change1h change1h stat-percent text-right col-market",
                ],
                [
                    "change_24hr",
                    "td-change24h change24h stat-percent text-right col-market",
                ],
                [
                    "change_7d",
                    "td-change7d change7d stat-percent text-right col-market",
                ],
            )

            percentage_func = curry_function(convert_str_to_float, "%")

            percentage_changes = get_change(
                percentage_changes, percentage_func, table_body_row
            )
            change_1hr = percentage_changes[0][2]
            change_24hr = percentage_changes[1][2]
            change_7d = percentage_changes[2][2]

            dollar_changes = (
                ["price", "td-price price text-right"],
                ["volume_24hr", "td-liquidity_score lit text-right %> col-market"],
                ["mrk_cap", "td-market_cap cap col-market cap-price text-right"],
            )
            dollar_func = curry_function(convert_str_to_float, "$", prefix=True)
            dollar_changes = get_change(dollar_changes, dollar_func, table_body_row)

            price = dollar_changes[0][2]
            volume_24hr = dollar_changes[1][2]
            mrk_cap = dollar_changes[2][2]

            with open(file_name, "a") as crypto_file:

                csv_writer = csv.DictWriter(
                    crypto_file, fieldnames=headers, delimiter="\t"
                )
                # write the heaader

                csv_writer.writerow(
                    {
                        headers[0]: coin_name_abv,
                        headers[1]: full_coin_name,
                        headers[2]: price,
                        headers[3]: change_1hr,
                        headers[4]: change_24hr,
                        headers[5]: change_7d,
                        headers[6]: volume_24hr,
                        headers[7]: mrk_cap,
                    }
                )

    time.sleep(60)

