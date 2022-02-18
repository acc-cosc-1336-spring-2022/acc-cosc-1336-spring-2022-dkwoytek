def get_options_ratio(options, total):
    return options / total

def get_faculty_rating(ratio):
    if 0.9 <= ratio and ratio < 1 :
        return "Excellent"     

    elif 0.8 < ratio and ratio < 0.9:
        return "Very Good"
    
    elif 0.7 < ratio and ratio < 0.8:
        return "Good"  
    
    elif 0.6 < ratio and ratio < 0.9:
        return "Needs Improvement"

    elif 0 <= ratio and ratio <= 0.59:
        return "Unacceptable"

    else :
        return "Invalid input."
        
