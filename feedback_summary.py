def summarize_feedback(feedbacks=None, filename="feedback_data.txt"):
    """Print a summary of all feedback entries."""
    if feedbacks is None:
        feedbacks = load_feedback(filename)
    
    if not feedbacks:
        print("No feedback to summarize.")
        return
    
    print("\n===== Feedback Summary =====")
    for i, fb in enumerate(feedbacks, 1):
        print(f"\nFeedback #{i}")
        print(f"Student: {fb['student_name']}")
        print(f"Course: {fb['course']}")
        print(f"Rating: {fb['rating']} / 5")
        print(f"Comments: {fb['comments']}")
    
    average = calculate_average_score(feedbacks)
    print(f"\n---\nAverage Rating: {average:.2f} / 5 based on {len(feedbacks)} feedback(s)")
