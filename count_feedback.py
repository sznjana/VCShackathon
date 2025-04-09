def count_total_feedback_entries(students):
    """
    Count and print total feedback entries per student, per subject, and overall.
    """
    total_count = 0
    print("\nFeedback Entry Counts:")

    for student, subjects in students.items():
        student_count = 0
        print(f"\nStudent: {student}")
        for subject, feedbacks in subjects.items():
            count = len(feedbacks)
            student_count += count
            print(f"  {subject}: {count} feedback entries")
        print(f"  ➤ Total for {student}: {student_count} entries")
        total_count += student_count

    print(f"\n✅ Overall Total Feedback Entries: {total_count}")
