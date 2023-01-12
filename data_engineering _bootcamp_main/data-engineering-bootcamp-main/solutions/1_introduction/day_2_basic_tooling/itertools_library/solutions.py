import itertools

# Use itertools to infinitely iterate over the [“a”, “b”, “c”] list.
for i, item in enumerate(itertools.cycle(["a", "b", "c"])):
    print(i, item)
    if i > 10:
        break

# Use itertools to show all permutations of the [“a”, “b”, “c”] list.
print(list(itertools.permutations(["a", "b", "c"])))

# Let’s assume that meat_types contains types of meat and salad_types contains types of salad. What would you do
# to get a list of all possible combinations: one meat type + one type of salad?
print(list(itertools.product(["beef", "chicken"], ["tomato salad", "potato salad"])))
