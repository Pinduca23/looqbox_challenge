import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

import queries

cnx = mysql.connector.connect(
    host='XXXXXXXXX',
    user='looqbox-challenge',
    password='XXXXXXXXXX',
    database='XXXXXXXXX'
)

cursor = cnx.cursor()

MENU_PROMPT = """
Please choose which graph you wish to view.

1 - Directors x Metascore
2 - Movie Title x (Revenue, Rating, Votes, Metascore)
3 - Movie Genre x Revenue
4 - Actors x Revenue
5 - Exit

Your Selection: """


def menu():
    while True:
        user_input = input(MENU_PROMPT)
        if user_input == '1':
            directors_graph()
        elif user_input == '2':
            title_revenue()
        elif user_input == '3':
            genre_revenue()
        elif user_input == '5':
            cursor.close()
            cnx.close()
            break
        elif user_input == '4':
            actors_revenue()
        else:
            print('\n---Not a valid option---')


def actors_revenue():
    cursor.execute(queries.ACTOR_NUMBER)
    actorsDF = pd.DataFrame(cursor, columns=['Revenue', 'Actors'])
    actorsDF.Revenue = pd.to_numeric(actorsDF.Revenue)
    actorsDF = actorsDF.dropna(subset=['Revenue'], inplace=False)
    revenue_list = list(actorsDF.to_records(index=False))
    dict_actors = {}
    for revenue, name_string in revenue_list:
        lista_actors = name_string.split(',')
        for name in lista_actors:
            name = name.strip()
            if name in dict_actors:
                dict_actors[name]["revenue"] += revenue
                dict_actors[name]["appearances"] += 1
            else:
                dict_actors[name] = {"revenue": revenue, "appearances": 1}
    df = pd.DataFrame.from_dict(dict_actors, orient='index').reset_index()
    df = df.sort_values(['revenue', 'appearances'], ascending=False)
    df = df.head(10)
    df['Average_Revenue_Millions'] = df.apply(
        lambda row: row.revenue / (row.appearances*100), axis=1)
    df.columns = ['Actor', 'Revenue in Millions', 'Appearances', 'Average Revenue Per Movie in 100Million']
    ax = plt.gca()
    df.plot(kind='line', x='Actor', y='Average Revenue Per Movie in 100Million', ax=ax, color='red', rot=30)
    df.plot(kind='bar', x='Actor', y='Appearances', ax=ax, rot=30)
    df.plot(kind='bar', x='Actor', y='Revenue in Millions', color='green', rot=30)
    plt.show()


def directors_graph():
    cursor.execute(queries.DIRECTORS_METASCORE)
    directorsDB = pd.DataFrame(cursor,
                               columns=['director', 'rating', 'metascore'])
    directorsDB['metascore'] = directorsDB['metascore']/10
    directorsDB.rating = pd.to_numeric(directorsDB.rating)
    directorsDB.metascore = pd.to_numeric(directorsDB.metascore)
    ax = plt.gca()
    directorsDB.plot(kind='bar', x='director', y='rating', ax=ax, rot=30)
    directorsDB.plot(kind='line', x='director', y='metascore',
                     color='red', ax=ax, rot=30)
    plt.show()


def title_revenue():
    # Creating and treating data
    cursor.execute(queries.MOVIE_TITLE_REVENUE)
    titleDB = pd.DataFrame(cursor,
                           columns=['Title', 'Revenue',
                                    'Rating', 'Metascore', 'Votes'])
    titleDB.Votes = pd.to_numeric(titleDB.Votes)
    titleDB.Revenue = pd.to_numeric(titleDB.Revenue)
    titleDB.Rating = pd.to_numeric(titleDB.Rating)
    titleDB.Metascore = pd.to_numeric(titleDB.Metascore)
    # Creating Charts
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    titleDB.plot(kind='bar', x='Title', y='Revenue', ax=ax1)
    ax2 = fig.add_subplot(222)
    titleDB.plot(kind='bar', x='Title', y='Rating', ax=ax2)
    ax3 = fig.add_subplot(223)
    titleDB.plot(kind='bar', x='Title', y='Metascore', ax=ax3)
    ax3 = fig.add_subplot(224)
    titleDB.plot(kind='bar', x='Title', y='Votes', ax=ax3)
    plt.show()


def genre_revenue():
    cursor.execute(queries.GENRE_REVENUE)
    genreDB = pd.DataFrame(cursor,
                           columns=['Genre', 'Revenue', 'Rating'])
    genreDB.Revenue = pd.to_numeric(genreDB.Revenue)
    genreDB.Rating = pd.to_numeric(genreDB.Rating)
    # Minha intenção aqui é normalizar os dados pra fazer tudo em um gráfico
    # Já que "Revenue" é na casa dos milhoes preciso normalizar os dados
    # pra que então consigar plotar em um gráfico só


menu()
