def calculate_cgpa(semesters_data):
    """Calculates CGPA based on accumulated credit hours and grade points."""
    total_credits = 0
    total_points = 0
    
    for sem, courses in semesters_data.items():
        for course in courses:
            credits = course['credits']
            grade_point = course['grade_point']
            total_credits += credits
            total_points += (credits * grade_point)
            
    if total_credits == 0:
        return 0.0, 0
    return round(total_points / total_credits, 2), total_credits

def predict_target(current_cgpa, current_credits, target_cgpa, remaining_credits):
    """Calculates the exact GPA needed in remaining semesters to hit a target."""
    if remaining_credits <= 0:
        return None
        
    total_needed_credits = current_credits + remaining_credits
    total_needed_points = target_cgpa * total_needed_credits
    current_points = current_cgpa * current_credits
    
    required_points = total_needed_points - current_points
    required_gpa = required_points / remaining_credits
    
    return round(required_gpa, 2)
