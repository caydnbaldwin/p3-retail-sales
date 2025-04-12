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

def main():
    while True:
        selection = input("If you want to import data, enter 1.\nIf you want to see summaries of stored data, enter 2.\nEnter any other value to exit the program: ")
        if selection == "1":
            pass
            # TODO 2: Read Retail_Sales_Data.xlsx into python using pandas

            # TODO 3: Separate the "name" column into a "first_name" and "last_name" column
                # TODO: Delete or overwrite the original "name" column
            
            # TODO 4: Fix the category column so that the categories actually match the product that was sold

            # TODO 5: Save the results as a table called "sale" in your is303 postgres database

            # TODO 6: Print out the message: "You've imported the excel file into your postgres database."

        elif selection == "2":
            pass
            # TODO 7: Print out: "The following are all the categories that have been sold:"

            # TODO 8: Print out: each of the categories stored in your database from the "sale" table with a number preceding it. You can't just hardcode the categories in, your program must read them from the database. 
                # It should look like this:
                    # 1: Technology
                    # 2: Apparel
                    # 3: Accessories
                    # 4: Household Items
                    # 5: Stationary
            
            # TODO 9: Print out: "Please enter the number of the category you want to see summarized: "

            # TODO 10: Then, for the entered category, calculate and display the sum of total sales, the average sale amount, and the total units sold

            # TODO 11: Then, display a bar chart ith the x axis as the products in that category and the y axis as the sum of the total sales of that product
                # TODO: The title of the chart should be "Total Sales by Product in Category (but put the actual category name)"
                # TODO: The x label should be "Product", the y label should be "Total Sales"
        else:
            print("Closing the program.")
            break

if __name__ == "__main__":
    main()