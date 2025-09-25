import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------
# User Management
# ---------------------------
def add_user(name, email, password_hash, age=None, location=None):
    return supabase.table("users").insert({
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "age": age,
        "location": location
    }).execute()

def get_user_by_email(email):
    return supabase.table("users").select("*").eq("email", email).execute()

# ---------------------------
# Activities & Categories
# ---------------------------
def add_activity_category(name, description=None):
    return supabase.table("activity_categories").insert({
        "name": name,
        "description": description
    }).execute()

def get_categories():
    return supabase.table("activity_categories").select("*").execute()

def add_activity(user_id, category_id, description, value, unit, emission_factor, date=None):
    return supabase.table("activities").insert({
        "user_id": user_id,
        "category_id": category_id,
        "description": description,
        "value": value,
        "unit": unit,
        "emission_factor": emission_factor,
        "date": date
    }).execute()

def get_user_activities(user_id):
    return supabase.table("activities").select("*").eq("user_id", user_id).execute()

# ---------------------------
# Carbon Logs
# ---------------------------
def add_carbon_log(user_id, total_emission, log_date=None):
    return supabase.table("carbon_logs").insert({
        "user_id": user_id,
        "total_emission": total_emission,
        "log_date": log_date
    }).execute()

def get_user_logs(user_id):
    return supabase.table("carbon_logs").select("*").eq("user_id", user_id).execute()

# ---------------------------
# Suggestions
# ---------------------------
def get_suggestions_by_category(category_id):
    return supabase.table("suggestions").select("*").eq("category_id", category_id).execute()
