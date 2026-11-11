def get_mark(course):
    while True:
        try:
            m = float(input(f"    Mark for {course} (0-100): "))
            if 0 <= m <= 100:
                return m
            print("    Mark must be between 0 and 100.")
        except ValueError:
            print("    Please enter a number.")

def grade_info(mark):
    if mark >= 90: return "A", 4.0
    if mark >= 80: return "B", 3.0
    if mark >= 70: return "C", 2.0
    if mark >= 60: return "D", 1.0
    return "F", 0.0

def main():
    students = []

    while True:
        name = input("Student name (blank to finish): ").strip()
        if not name:
            break

        n = 0
        while n < 1:
            try:
                n = int(input("  Number of courses: "))
            except ValueError:
                print("  Enter a whole number.")

        results = []
        for i in range(n):
            course = input(f"  Course {i+1} name (Enter for default): ").strip() or f"Subject {i+1}"
            mark = get_mark(course)
            letter, points = grade_info(mark)
            results.append((course, mark, letter, points))

        gpa = sum(r[3] for r in results) / len(results)
        students.append((name, results, gpa))

    if not students:
        print("No students entered.")
        return

    print()
    for name, results, gpa in students:
        print(f"Student: {name}")
        print(f"{'Course':<12}{'Mark':>8}{'Grade':>8}")
        for course, mark, letter, _ in results:
            print(f"{course:<12}{mark:>8.1f}{letter:>8}")
        print()

    print("===== GPA SUMMARY =====")
    print(f"{'Student':<12}{'GPA':>6}")
    for name, _, gpa in students:
        print(f"{name:<12}{gpa:>6.2f}")

main()