## In this script, we'll dive more deeply into relations between tables, learn about data normalization, and how we can take advantage of them to perform more complex joins

## In this script, we'll work with data on Academy Award nominations from 2001 to 2010 for just the lead and supporting acting roles.


## Database Normalization - It involves separating data into smaller tables with less redundant information and creating relations between the appropriate tables

## Types Of Relations

# 2 most common relations: one-to-many and many-to-many.


## Querying A Normalized Database

query = 'select ceremonies.year, nominations.movie from nominations INNER JOIN ceremonies ON nominations.ceremony_id == ceremonies.id where nominations.nominee == "Natalie Portman";'
portman_movies = conn.execute(query).fetchall()
print(portman_movies)


## Many-To-Many Relation

# The right way to model actors and movies is to use a many-to-many relation. A many-to-many relation allows us to flexibly represent both:

# the actors in a movie and
# the movies an actor has starred in


## Join Table

CREATE table movies_actors (
id INTEGER PRIMARY KEY,
movie_id INTEGER REFERENCES movies(id),# two foreign columns
actor_id INTEGER REFERENCES actors(id) 
);

five_movies = conn.execute("select * from movies limit 5;").fetchall()

five_actors = conn.execute("select * from actors limit 5;").fetchall()
five_join_table = conn.execute("select * from movies_actors limit 5;").fetchall()

print(five_movies)
print(five_actors)
print(five_join_table)


## 
