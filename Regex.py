
def exchangecus():
    import re
    import requests
    from bs4 import BeautifulSoup
    url = 'https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019'
    import csv

    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')


    # Find all tables in the HTML
    tables = soup.find_all('table')

    # Iterate through each table
    for table in tables:
        # Find all rows in the table
        rows = table.find_all('tr')
        csv_data = []
        # Loop through each row
        for row in rows:
            # Find all cells in the row
            cells = row.find_all(['th', 'td'])
            csv_row = []
            # Loop through each cell
            for cell in cells:
                # Remove HTML tags from the cell
                cell_data = cell.get_text(strip=True)
                csv_row.append(cell_data)
            csv_data.append(csv_row)
        # Write the data to a CSV file
        with open('table.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
    Exchange2019 = (re.search("15.02.\d\d\d\d.\d\d\d",str(soup))).group()
    Exchange2016 = (re.search("15.01.\d\d\d\d.\d\d\d",str(soup))).group()
    Exchange2013 = (re.search("15.00.\d\d\d\d.\d\d\d",str(soup))).group()

    return  Exchange2013,Exchange2016,Exchange2019
    # print("Latest exchange 2019 is : ", Exchange2019)
    # print("Latest exchange 2016 is : ", Exchange2016)
    # print("Latest "exchange 2013 is : ", Exchange2013)
