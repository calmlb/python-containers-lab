# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.

##### 

students = ["mark", "hadi", "jasnoor", "jason", "amadou"]
awesome_students = []

for student in (students):
    new_list = [student, "is awesome!"]
    awesome_students.append(new_list)
print(awesome_students)

