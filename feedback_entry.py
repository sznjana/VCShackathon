def collect_feedback():
    print("===== Student Feedback Form =====")

    student_name = input("What is your name? ")
    course = input("What course are you rating? ")
    
    rating = 0
    while rating < 1 or rating > 5:
        try:
            rating = int(input("Rate this course from 1-5: "))
        except ValueError:
            print("Please enter a valid number.")

    comments = input("Any comments? ")

    feedback = {
        "student_name": student_name,
        "course": course,
        "rating": rating,
        "comments": comments,
        "timestamp": datetime.now().isoformat()
    }

    return feedback

def save_feedback(feedback, filename="feedback_data.txt"):
    import os
    os.makedirs("data", exist_ok=True)

    with open(f"data/{filename}", "a") as f:
        line = f"{feedback['student_name']}|{feedback['course']}|{feedback['rating']}|{feedback['comments']}|{feedback['timestamp']}\n"
        f.write(line)

    print("Feedback saved!")
