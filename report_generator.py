# report_generator.py

from datetime import datetime
from collections import defaultdict
from feedback_entry import load_feedback, calculate_average_score

def generate_course_summary(feedbacks):
    course_stats = defaultdict(list)

    for fb in feedbacks:
        course_stats[fb["course"]].append(fb["rating"])

    summary_lines = ["\n--- Course-wise Summary ---"]
    for course, ratings in course_stats.items():
        avg = sum(ratings) / len(ratings)
        summary_lines.append(f"{course}: {avg:.2f} / 5 ({len(ratings)} feedbacks)")
    
    return summary_lines

def generate_feedback_report(filename="feedback_data.txt", report_filename="feedback_report.txt"):
    feedbacks = load_feedback(filename)

    if not feedbacks:
        print("No feedback available to generate a report.")
        return

    # Load version info
    try:
        with open("version.txt") as vf:
            version = vf.read().strip()
    except FileNotFoundError:
        version = "Unknown"

    report_lines = []
    report_lines.append("===== FEEDBACK REPORT =====\n")
    report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"Version: {version}")
    report_lines.append(f"Total Feedback Entries: {len(feedbacks)}")
    report_lines.append(f"Average Rating: {calculate_average_score(feedbacks):.2f} / 5\n")
    report_lines.append("--- Detailed Feedback ---")

    for i, fb in enumerate(feedbacks, 1):
        report_lines.append(f"{i}. {fb['student_name']} ({fb['course']})")
        report_lines.append(f"   Rating: {fb['rating']} / 5")
        report_lines.append(f"   Comments: {fb['comments']}")
        if "timestamp" in fb:
            report_lines.append(f"   Submitted: {fb['timestamp']}")
        report_lines.append("")  # Empty line between entries

    report_lines.extend(generate_course_summary(feedbacks))

    with open(report_filename, "w") as f:
        f.write("\n".join(report_lines))
    
    print(f"✅ Feedback report saved as '{report_filename}'")

if __name__ == "__main__":
    generate_feedback_report()
