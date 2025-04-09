def search_feedback_by_student(students, search_name):
    """
    Search and display feedback for a student by name (case-insensitive, partial match allowed).
    """
    found = False
    for student, subjects in students.items():
        if search_name.lower() in student.lower():
            found = True
            print(f"\nFeedback for {student}:")
            for subject, feedbacks in subjects.items():
                print(f"  Subject: {subject}")
                for i, feedback in enumerate(feedbacks, start=1):
                    print(f"    {i}. {feedback}")
            print("-" * 40)
    
    if not found:
        print(f"No student found matching '{search_name}'.")
