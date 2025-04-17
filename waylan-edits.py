# Aaron McCoy, Anders Houghton, Caydn Baldwin, George Martinez, Ryan Bartholomew, Waylan Abbott
# Project 4 - Retail Sales: Pandas and PostgreSQL
# Transfer data into a postgres database and read data programmatically back from the database using Pandas to display a summary of different product categories.

import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

# these ones are optional
import openpyxl
from sqlalchemy.sql import text
import psycopg2

# TODO 1: The excel file is mostly in good shape, except the Name column needs to be separated into first name and last name, and the Category column has the incorrect categories listed. You'll need to fix the categories based on the product names

while True:
    selection = input("If you want to import data, enter 1.\nIf you want to see summaries of stored data, enter 2.\nEnter any other value to exit the program: ")
    
    if selection == "1":
        df = pd.read_excel("Retail_Sales_Data.xlsx")  # Read spreadsheet into a DataFrame

        name_column_index = 1
        split_names = df['name'].str.split('_', expand=True)
        df.drop(columns=['name'], inplace=True)
        df.insert(loc=name_column_index, column='first_name', value=split_names[0])
        df.insert(loc=name_column_index + 1, column='last_name', value=split_names[1])

        product_categories_dict = {
            'Camera': 'Technology',
            'Laptop': 'Technology',
            'Gloves': 'Apparel',
            'Smartphone': 'Technology',
            'Watch': 'Accessories',
            'Backpack': 'Accessories',
            'Water Bottle': 'Household Items',
            'T-shirt': 'Apparel',
            'Notebook': 'Stationery',
            'Sneakers': 'Apparel',
            'Dress': 'Apparel',
        }

        df['category'] = df['product'].map(product_categories_dict)

        print("\nDataFrame after processing (first 5 rows):")
        print(df.head())
        print("---------------------------------\n")

        username = "georgemartinez"
        password = "admin"
        host = "localhost"
        port = "5432"
        database = "project"
        engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
        df.to_sql('sale', engine, if_exists='replace', index=False)

        print("You've imported the excel file into your postgres database.")

    elif selection == "2":
        print("The following are all the categories that have been sold:")

        username = 'georgemartinez'
        password = 'admin'
        host = 'localhost'
        port = '5432'
        database = 'project'

        engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
        conn = engine.connect()

        query = "SELECT DISTINCT category FROM sale ORDER BY category;"
        categories_df = pd.read_sql(text(query), conn)

        for iCount, stuff in enumerate(categories_df['category'], start=1):
            print(f"{iCount}: {stuff}")

        userSelection = int(input("Please enter the number of the category you want to see summarized: "))
        selection_dict = {1: 'Accessories', 2: 'Apparel', 3: 'Household Items', 4: 'Stationery', 5: 'Technology'}
        selection = selection_dict[userSelection]
        print(selection)

        query = """
                SELECT product, SUM(total_price) AS total_sales, AVG(total_price) AS average_sales, SUM(quantity_sold) AS total_quantity_sold
                FROM sale
                WHERE category = :category
                GROUP BY product
                ORDER BY total_sales DESC"""
        df = pd.read_sql(text(query), conn, params={"category": selection})
        iColumnSum = df['total_sales'].sum()
        iColumnAve = df['average_sales'].median()
        iColumnQuantity = df['total_quantity_sold'].sum()

        print(f"Total sales for {selection}: ${iColumnSum:.2f}")
        print(f"Average sale amount for {selection}: ${iColumnAve:.2f}")
        print(f"Total units sold for {selection}: {iColumnQuantity:.0f}")

        plot.bar(df['product'], df['total_sales'])
        plot.title(f"Total Sales in {selection}")
        plot.xlabel("Product")
        plot.ylabel("Total Sales")
        plot.show()

    else:
        print("Closing the program.")
        break