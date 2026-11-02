sun = "No HW"
mon="School HW & Coding HW"
tue="School HW"
wen="School HW & Coding HW"
thu="School HW"
fri="Maybe School HW"
sat="No HW"

with open("homework_schedule.txt", "w") as f:

    f.write("=== Weekly HW Schedule ===")
    f.write(f"Sunday:   {sun}\n")
    f.write(f"Monday:   {mon}\n")
    f.write(f"Tuesday:  {tue}\n")
    f.write(f"Wensenday:{wen}\n")
    f.write(f"Thursday: {thu}\n")
    f.write(f"Friday:   {fri}\n")
    f.write(f"Saturday: {sat}\n")

print("Homework schedule saved successfully!")