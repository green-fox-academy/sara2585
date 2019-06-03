students = [{'name': 'John', 'age': 16, 'gender': 'male', 'grades': [5, 5, 4, 2]},
            {'name': 'Jane', 'age': 15, 'gender': 'female', 'grades': [4, 3, 4, 4, 5]},
            {'name': 'Bob', 'age': 17, 'gender': 'male', 'grades': [2, 2, 3, 1]}]

# Create a new list that only includes the boys
boys = list(filter(lambda student: student['gender'] == 'male', students))


# Create a new list that only includes who's name starts with the letter J
name_start_with_J = list(filter(lambda student: 'J' in student['name'], students))


# Create a new list that only includes the girls
girls = list(filter(lambda student: student['gender'] == 'female', students))

# Create a new list that only includes who's grade average is above 4
grade_average_above_4 = list(filter(lambda student: sum(student['grades'])/len(student['grades']) > 4, students))


# Create a new list that only includes the boys who's name starts with the letter J
boys_name_with_J = list(filter(lambda student: 'J' in student['name'], boys))



# Create a new list that only includes the girls who's grade average is above 4
girls_grade_avg_above_4 = list(filter(lambda student: sum(student['grades'])/len(student['grades']) > 4, girls))

# Create a new list that only includes who's at least two 5s
at_least_two_5s = list(filter(lambda student: student['grades'].count(5)>= 2, students))


# Create a new list that only includes who's grade average is above 4 and at at least got two 5s
avg_above_4_and_at_least_2_5s = list(filter(lambda student: sum(student['grades'])/len(student['grades']) > 4 and student['grades'].count(5)>= 2, students))
# print(avg_above_4_and_at_least_2_5s)