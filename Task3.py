from datetime import datetime

date1 = datetime.strptime("2025-01-01", "%Y-%m-%d")
date2 = datetime.strptime("2025-01-15", "%Y-%m-%d")
difference = (date2 - date1).days
print("Difference:", difference, "days")
