# create a dictionary to store the family tree
family = {}

# prompt the user to enter the names of the parents
mother_name = input("Enter the name of the mother: ")
father_name = input("Enter the name of the father: ")

# add the parents to the family tree
family[mother_name] = []
family[father_name] = []

# create a function to add children to a parent
def add_child(parent):
  # prompt the user to enter the name of the child
  child_name = input("Enter the name of the child: ")

  # add the child to the parent's list of children
  family[parent].append(child_name)

# prompt the user to add children to the mother and father
print("Add children to the mother:")
while True:
  add_child(mother_name)
  # prompt the user to continue adding children or to stop
  cont = input("Add another child to the mother? (y/n)")
  if cont != "y":
    break

print("Add children to the father:")
while True:
  add_child(father_name)
  # prompt the user to continue adding children or to stop
  cont = input("Add another child to the father? (y/n)")
  if cont != "y":
    break

# print the family tree
print("\nFamily tree:")
for parent, children in family.items():
  print(parent + ": " + str(children))
