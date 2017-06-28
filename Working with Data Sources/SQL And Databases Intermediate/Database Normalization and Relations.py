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


## Querying A Many-To-Many Relation

SELECT actors.actor FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie == "The Fighter";

kings_actors = conn.execute('''SELECT actors.actor, movies.movie FROM movies 
INNER JOIN movies_actors 
ON movies.id == movies_actors.movie_id 
INNER JOIN actors ON movies_actors.actor_id == actors.id 
WHERE movies.movie == "The King's Speech";''').fetchall()
print(kings_actors)


## Practice: Querying A Many-To-Many Relation

query = '''
SELECT movies.movie, actors.actor from movies
INNER JOIN movies_actors
ON movies.id == movies_actors.movie_id
INNER JOIN actors
ON movies_actors.actor_id == actors.id
WHERE actors.actor == "Natalie Portman";'''
portman_joins = conn.execute(query).fetchall()
print(portman_joins)


## In this mission, we learned about 2 different kinds of relations,
## how to query tables in a database with these kinds of relations, and the paradigm of database normalization


## END




















