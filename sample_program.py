
# Classroom Attendance System
# AI assistance: ChatGPT helped draft the sample program.
# I will review and test the code before submitting it.

def display_attendance(records):
    """Display student attendance records and a summary."""
    present_count = 0
    absent_count = 0

    print("=== Classroom Attendance System ===")
    print()

    for student in records:
        name = student["name"]
        status = student["status"]

        print(f"{name}: {status}")

        if status == "Present":
            present_count += 1
        elif status == "Absent":
            absent_count += 1

    print("\n=== Attendance Summary ===")
    print(f"Present: {present_count}")
    print(f"Absent: {absent_count}")
    print(f"Total students: {len(records)}")


# Fictional student records for demonstration.
attendance_records = [
    {"name": "Alex", "status": "Present"},
    {"name": "Jamie", "status": "Absent"},
    {"name": "Taylor", "status": "Present"},
    {"name": "Morgan", "status": "Present"},
    {"name": "Casey", "status": "Absent"}
]

# Display the sample attendance records.
display_attendance(attendance_records)
