from datetime import datetime

def export_feedback_report(students, filename="feedback_report.txt"):
    try:
        with open(filename, "w") as f:
            f.write(f"Student Feedback Report\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")

            if not students:
                f.write("No feedback data available.\n")
                return

            for student, subjects in students.items():
                f.write(f"Student: {student}\n")
                for subject, feedbacks in subjects.items():
                    f.write(f"  Subject: {subject}\n")
                    for i, feedback in enumerate(feedbacks, start=1):
                        f.write(f"    {i}. {feedback}\n")
                f.write("\n")
        
        print(f"Feedback successfully exported to '{filename}'")

    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
