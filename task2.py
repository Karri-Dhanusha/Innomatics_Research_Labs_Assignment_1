"""
Student Performance Analysis System
Analyzes student marks and categorizes them as pass or fail.
"""

# Define the passing threshold
PASS_MARK = 50


def analyze_marks(marks):
    """
    Analyzes student marks and counts pass/fail statistics.
    
    Args:
        marks (list): List of student marks
        
    Returns:
        tuple: (total_students, pass_count, fail_count)
    """
    pass_count = sum(1 for mark in marks if mark >= PASS_MARK)
    fail_count = len(marks) - pass_count
    
    return len(marks), pass_count, fail_count


def main():
    """Main function to display student performance statistics."""
    student_marks = [45, 78, 90, 33, 60]
    
    total, passed, failed = analyze_marks(student_marks)
    
    print(f"Total Students: {total}")
    print(f"Number of Pass Students: {passed}")
    print(f"Number of Fail Students: {failed}")


if __name__ == "__main__":
    main()