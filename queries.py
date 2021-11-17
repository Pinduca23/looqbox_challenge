'''
FIRST_QUESTION = 'SELECT count(distinct(PRODUCT_NAME)) FROM data_product'

print('The company has: {} products'.format(cursor.fetchall()))

SECOND_QUESTION = """select product_name, product_val from data_product
                order by PRODUCT_VAL desc
                limit 10"""

secondDB = pandas.DataFrame(cursor, columns=(['Product', 'Product Value']))

THIRD_QUESTION = """select distinct(section_name) from data_product
                where DEP_NAME like 'BEBIDAS'
                or DEP_NAME like 'PADARIA'"""

thirdDB = pandas.DataFrame(cursor, columns=['Section'])

FOURTH_QUESTION = """select data_store_sales.STORE_CODE, STORE_NAME, DATE
                from data_store_sales
                JOIN data_store_cad
                ON data_store_cad.STORE_CODE = data_store_sales.STORE_CODE
                order by SALES_VALUE desc
                limit 1"""
fourthDB = pandas.DataFrame(cursor, columns=['Store Code', 'Store Name',
                                             "Date"])

FIFTH_QUESTION = """select
                BUSINESS_NAME,
                sum(SALES_VALUE),
                sum(SALES_QTY)
                from data_product_sales AS DS
                join data_store_cad as DC
                ON DS.STORE_CODE = DC.STORE_CODE
                where DATE between '2019/01/01' AND '2019/03/01'
                group by BUSINESS_NAME
                order by sum(DS.SALES_VALUE) desc
                """
fifthDB = pandas.DataFrame(cursor, columns=['Business Name',
                                            'Total Sales $',
                                            'Total Sales Qty'])
'''
DIRECTORS_METASCORE = """SELECT director,avg(rating), avg(metascore)
                    FROM IMDB_movies
                    where metascore is not NULL
                    group by director
                    order by avg(rating) desc
                    limit 10"""

MOVIE_TITLE_REVENUE = """select title, RevenueMillions, Rating, Metascore, votes
                        from IMDB_movies
                        where RevenueMillions is not NULL
                        order by RevenueMillions desc
                        limit 10"""

GENRE_REVENUE = """select genre, avg(RevenueMillions), avg(Rating)
                    from IMDB_movies
                    group by Genre
                    order by avg(RevenueMillions) desc"""

ACTOR_NUMBER = """select RevenueMillions, actors from IMDB_movies"""
