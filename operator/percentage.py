# Calculate the percentage of marks obtained
# Formula: (Marks Obtained / Total Marks) × 100

marks_obtained = int(input("Enter the marks obtained: "))
total_marks = int(input("Enter the total marks: "))

# Divide the obtained marks by total marks
# and multiply by 100 to calculate the percentage
percentage = (marks_obtained / total_marks) * 100

print(f"Percentage: {percentage:.2f}%")