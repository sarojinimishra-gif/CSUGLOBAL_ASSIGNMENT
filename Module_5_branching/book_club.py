num_of_books = int(input("Enter number of books you purchased this month : "))
points_earned = 0
if num_of_books == 0:
    points_earned = 0
elif num_of_books == 2:
    points_earned = 5
elif num_of_books == 4:
    points_earned = 15
elif num_of_books == 6:
    points_earned = 30
elif num_of_books >= 8:
    points_earned = 60

print(f"Number of books purchased in this month are {num_of_books}.")
print(f"Number of points earned are {points_earned}")

