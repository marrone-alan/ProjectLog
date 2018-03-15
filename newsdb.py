# Database code for the log project

import psycopg2

DBNAME = "news"


def getTitles():
    """Return three most popular articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(path) as views from log, (select slug, "
              "title from articles) as art where status like '200 OK' and "
              " replace(path, '/article/', '') = slug"
              " group by path, title order by views DESC limit 3;")
    result = c.fetchall()
    db.close()
    return result


def getAuthors():
    """Return authors of the most popular articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select au.name, count(*) AS views FROM log l INNER JOIN "
              "articles a ON (path = '/article/' || a.slug)"
              " INNER JOIN authors au ON au.id = a.author "
              "GROUP BY au.name ORDER BY views DESC;")
    result = c.fetchall()
    db.close()
    return result


def getPercentage():
    """Return days when more than 1% of requests have errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select tb1.dayTotal as day, concat(round((tb2.error::decimal/"
              "tb1.total::decimal)*100.0, 2), '% errors') as error from "
              "(select to_char(time, 'Month DD, YYYY') as dayTotal, "
              "count(time) as total from log group by dayTotal) as tb1, "
              "(select to_char(time, 'Month DD, YYYY') as dayError, "
              "count(time) as error from log where status like '404 NOT FOUND'"
              " group by dayError) as tb2 where tb1.dayTotal = tb2.dayError "
              "and round((tb2.error::decimal/tb1.total::decimal)*100.0, 2) >"
              " 1.0;")
    result = c.fetchall()
    db.close()
    return result
