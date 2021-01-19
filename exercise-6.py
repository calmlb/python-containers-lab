# - Create an empty list named `cohort`.

# - Using a `for` loop, add one dictionary to the `cohort` list for each student name (using the students and foods containers above). Each dictionary should have this shape:
students = ["mark", "hadi", "jasnoor", "jason", "amadou"]
favfoods = ('apple', 'banana', 'avocado', 'pear', 'peach')
cohort = []

for idx, student in enumerate (students):
    student_food_pair = {
        "student": student,
        "favfood": favfoods[idx]
    }
    cohort.append(student_food_pair)
print(cohort)

    # cohort.append()

        
#   ```python
#   {
#     'student': 'Tina',
#     'fav_food' 'Cheeseburger'
#   }
#   ```

# - Iterate over `cohort` printing out each element.