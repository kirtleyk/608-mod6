
import sqlite3
import pandas as pd

conn = sqlite3.connect("./books.db")

pd.options.display.max_columns = 10

#print(pd.read_sql('Select * from sqlite_master where type="table"', conn), '\n')
print('Table: Authors', '\n', pd.read_sql('Select * from authors', conn), '\n')
print('Table: Titles', '\n', pd.read_sql('Select * from titles', conn), '\n')
print('Table: Author_ISBN', '\n', pd.read_sql('Select * from author_ISBN', conn), '\n')
#print(pd.read_sql('Select a.first, a.last, t.isbn, t.title, t.copyright, t.edition from titles t, authors a, author_ISBN ai where a.id = ai.id and t.isbn = ai.isbn ', conn), '\n')

print('Titles Where copyright > 2016', '\n', 
      pd.read_sql("""Select title, edition, copyright from titles
                  WHERE copyright > '2016' """, conn), '\n')

print('Authors where last name starts with "D"', '\n', 
      pd.read_sql("""Select id, first, last from authors
                  WHERE last LIKE 'D%'""", conn), '\n')

print('Authors where second letter of first name is "b"', '\n',
      pd.read_sql("""Select id, first, last from authors
                  WHERE first LIKE '_b%'""", conn), '\n')

print('Titles in ascending order', '\n', 
      pd.read_sql('Select * from titles ORDER BY title ASC', conn), '\n')

print('Authors Order By last name, first name', '\n',
      pd.read_sql("""Select id, first, last from authors
                  ORDER BY last, first""", conn, index_col=['id']), '\n')

print('Authors Order By last name DESC, first name ASC', '\n',
      pd.read_sql("""Select id, first, last from authors
                  ORDER BY last desc, first""", conn, index_col=['id']), '\n')

print('Titles where title ends with "How to Program" ordered by title', '\n',
      pd.read_sql("""Select title, edition, copyright from titles
                  WHERE title like '%How to Program'
                  ORDER BY title""", conn), '\n')

conn.close()



