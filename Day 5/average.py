student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
for i in student_heights:
    total_height += i
    print(total_height)


print(
    f"""-------------------------------------------\n{round(total_height/len(student_heights),2)}
"""
)
