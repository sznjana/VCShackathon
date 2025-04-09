# This program calculates average scores from feedback

def load_feedback(filename="feedback_data.txt"):
    """Load all the feedback from our file."""
    feedbacks = []
    
    try:
        with open(f"data/{filename}", "r") as file:
            for line in file:
                # Split each line by the | character
                parts = line.strip().split("|")
                
                # Create a feedback dictionary
                if len(parts) == 4:
                    feedback = {
                        "student_name": parts[0],
                        "course": parts[1],
                        "rating": int(parts[2]),
                        "comments": parts[3]
                    }
                    feedbacks.append(feedback)
    except FileNotFoundError:
        print("No feedback found yet. Let's collect some first!")
    
    return feedbacks

def calculate_average_score(feedbacks=None, filename="feedback_data.txt"):
    """Calculate the average score of all feedback."""
    if feedbacks is None:
        feedbacks = load_feedback(filename)
    
    # If we don't have any feedback, return 0
    if not feedbacks:
        return 0
    
    # Add up all the ratings
    total_score = 0
    for feedback in feedbacks:
        total_score += feedback["rating"]
    
    # Calculate the average
    average = total_score / len(feedbacks)
    return average

# When we run this file directly
if __name__ == "__main__":
    avg_score = calculate_average_score()
    print(f"The average score from all feedback is: {avg_score:.1f} out of 5")
