student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(sum(student_scores))
# total_sum = 0
#
# for score in student_scores :
#     total_sum += score
# print(total_sum)
#print(range(1, 10))

# print (max(student_scores))

max_of_scores = None

for score in student_scores :
    if (max_of_scores == None) or (score > max_of_scores) :
        max_of_scores = score
print(max_of_scores)