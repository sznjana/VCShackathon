# search_feedback.py

from feedback_entry import load_feedback

def search_feedback_by_student(name_query, filename="feedback_data.txt"):
    feedbacks = load_feedback(filename)
    
    if not feedbacks:
        print("No feedback data found.")
        return

    name_query = name_query.lower()
    found = [fb for fb in feedbacks if name_query in fb["student_name"].lower()]

    if not found:
        print(f"No feedback found for '{name_query}'.")
    else:
        print(f"\nFound {len(found)} feedback(s) for '{name_query}':\n")
        for i, fb in enumerate(found, 1):
            print(f"{i}. {fb['student_name']} ({fb['course']})")
            print(f"   Rating: {fb['rating']} / 5")
            print(f"   Comments: {fb['comments']}")
            if "timestamp" in fb:
                print(f"   Submitted: {fb['timestamp']}")
            print()

if __name__ == "__main__":
    student_name = input("Enter the student name to search: ")
    search_feedback_by_student(student_name)
