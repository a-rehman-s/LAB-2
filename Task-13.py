import json

data = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 90},
    {"name": "Charlie", "marks": 78}
]
average_marks = sum(student["marks"] for student in data) / len(data)
print("Average Marks:", round(average_marks, 2))
