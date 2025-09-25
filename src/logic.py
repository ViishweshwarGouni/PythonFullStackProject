from src import db

def calculate_emission(value, emission_factor):
    """Calculate emission for a single activity"""
    return value * emission_factor

def log_activity(user_id, category_id, description, value, unit, emission_factor, date=None):
    """Add an activity and update carbon log"""
    emission = calculate_emission(value, emission_factor)

    # Save activity
    db.add_activity(user_id, category_id, description, value, unit, emission_factor, date)

    # Add/update carbon log
    db.add_carbon_log(user_id, emission, date)
    return emission

def get_recommendations(user_id):
    """Generate personalized tips based on user's activities"""
    activities = db.get_user_activities(user_id).data
    recs = []

    for act in activities:
        suggestions = db.get_suggestions_by_category(act["category_id"]).data
        for s in suggestions:
            recs.append({
                "activity": act["description"],
                "tip": s["tip"],
                "potential_reduction": s.get("reduction_estimate", None)
            })
    return recs
