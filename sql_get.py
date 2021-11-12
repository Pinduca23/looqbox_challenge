from mysql.connector import connect, Error
import pandas
from datetime import datetime

# How many products does the company have?
# What are the 10 most expensive products in the company?
# What sections do the 'BEBIDAS' and 'PADARIA' departments have?
# Which store sold the most products in one day? Which day?
# Bonus!! What was the total sale of products (in $) of each business area
# in the first quarter of 2019?

try:
    with connect(
        host='xxxx.xx.x.xxx',
        user='xxxxxxxx',
        password='ggggggggg',
        database='aaaaaaaaaa'
    ) as connection:
        first_question = """SELECT COUNT(PRODUCT_COD)
        FROM DATA_PRODUCT
        """
        with connection.cursor() as cursor:
            query_data = cursor.execute(first_question)
except Error as e:
    print(e)

my_db = pandas.DataFrame(query_data)

total_products = my_db.count(axis=1)

# my_db = my_db.append(cursor.execute(first_query))

print('The company has: ', total_products, ' products')

# second_question = """SELECT PRODUCT_VAL
# FROM DATA_PRODUCT
# ORDER BY PRODUCT_VAL DESC limit 5
# """

# third_question = """SELECT SECTION_NAME FROM DATA_PRODUCT
# WHERE SECTION_NAME = BEBIDAS, PADARIA
# """

# Which store sold the most products in one day? Which day?
# fourth_question = """SELECT DATE(DATE), STORE_CODE, STORE_NAME
# FROM DATA_STORE_CAD
# JOIN DATA_STORE_SALES ON STORE_CODE = DATA_STORE_SALES.STORE_CODE
# ORDER BY DATA_STORE_SALES DESC
# LIMIT 1
# """


# Bonus!! What was the total sale of products (in $) of each business area
# in the first quarter of 2019?
