def get_mark(name):
    while True:
        try:
            m = float(input(f"  {name} mark (0-100): "))
            if 0 <= m <= 100:
                return m
            print("  Mark must be between 0 and 100.")
        except ValueError:
            print("  Please enter a number.")

def letter_grade(avg):
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

def main():
    students = []
    while True:
        name = input("Student name (blank to finish): ").strip()
        if not name:
            break
        n = 0
        while n < 1:
            try:
                n = int(input("  Number of subjects: "))
            except ValueError:
                print("  Enter a whole number.")
        marks = [get_mark(f"Subject {i+1}") for i in range(n)]
        avg = sum(marks) / n
        students.append((name, avg, letter_grade(avg)))

    print(f"\n{'Name':<20}{'Average':>10}{'Grade':>8}")
    for name, avg, g in students:
        print(f"{name:<20}{avg:>10.2f}{g:>8}")

main()