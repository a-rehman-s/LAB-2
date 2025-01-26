with open("D://file1.txt", "r") as file1, open("D://file2.txt", "r") as file2:
    combined = file1.read().split(", ") + file2.read().split(", ")
    sorted_combined = sorted(combined)

with open("output.txt", "w") as output:
    output.write(", ".join(sorted_combined))
print("Merged and Sorted Content:", sorted_combined)
