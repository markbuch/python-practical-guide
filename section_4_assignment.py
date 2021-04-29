# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

persons = [{'name': 'Oscar', 'age': 8, 'hobbies': ['eating', 'sleeping', 'playing']}]
persons.append({'name': 'Herbie', 'age': 12, 'hobbies': ['sleeping', 'eating', 'purring']})
persons.append({'name': 'Benny', 'age': 1, 'hobbies': ['playing', 'eating', 'sleeping']})
#for person in persons:
 #   print(person)

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_names = [person['name'] for person in persons]
print(persons)
print(person_names)


# 3) Use a list comprehension to check whether all persons are older than 20.
is_over_thirty = all([person['age'] > 10 for person in persons])
print(is_over_thirty)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:] (shallow copy.)
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Joe'
print(copied_persons)
print(persons)

# 5) Unpack the persons of the original list into different variables and output these variables.
p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)
