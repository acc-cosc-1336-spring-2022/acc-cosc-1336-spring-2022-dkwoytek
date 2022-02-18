import decisions

total = int(input("What is maximum number of points you could assign to your prefessor? "))
options = int(input("How many points do you want to give to your professor? "))

ratio = decisions.get_options_ratio(options,total)

print("Based on the info you entered, your professor is rated as :", decisions.get_faculty_rating(ratio))
