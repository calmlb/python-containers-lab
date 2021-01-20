# Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.
foods = ('apple', 'banana', 'avocado', 'pear', 'peach')

for food in foods:
    if "a" in food:
        print(food)