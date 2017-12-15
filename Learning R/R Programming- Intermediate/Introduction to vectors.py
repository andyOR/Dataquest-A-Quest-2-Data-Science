## Introduction to R -vectors


## Indexing a vector by position

final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
third <- final_scores[3]


## Understanding the numeric data types

final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
print(class(final_scores))


## Understanding the character data types

class_names <- c('math','chemistry','writing','art','history','music','physical_education')
class(class_names)


## Naming values

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)

names(final_scores) <- class_names
named_final_scores <- final_scores


## Indexing vector using names

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
names(final_scores) <- class_names
history <- final_scores["history"]
art <- final_scores["art"]
music <- final_scores["music"]


## Comparing values and logical data types

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
names(final_scores) <- class_names

history_math <- final_scores['history'] > final_scores['math']
writing_art <- final_scores['writing'] <= final_scores['art']
music_chem <- final_scores['music'] == final_scores['chemistry']


## Comparing single value against vectors

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
names(final_scores) <- class_names

lowest_score <- min(final_scores)
lowest_logical <- final_scores == lowest_score


## Indexing using logical data types

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
names(final_scores) <- class_names

lowest_score <- min(final_scores)
lowest_logical <- lowest_score == final_scores
lowest_class <- final_scores[lowest_logical]


## Performing arithmetic with a vector

tests <- c(76, 89, 78, 88, 79, 93, 89)
homework <- c(85, 90, 88, 79, 88, 95, 74)
sum <- tests + homework

projects <- c(77, 93, 87, 90, 77, 82, 80)
johnny_scores <- (projects + sum)/3
johnny_overall <- mean(johnny_scores)


## Vector recycling rule

tests <- c(76, 89, 78)
homework <- c(85, 90, 88, 79, 88, 95, 74)

recycling <- tests + homework
print(recycling)


## Appending data to vector

tests <- c(76, 89, 78)

tests <- c(tests, 88,79,93,89)


## END


























