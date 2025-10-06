import streamlit as st
import datetime 
import sys
import os

# --- CRITICAL FIX: Standard Python Import using sys.path for module visibility ---
# The correct path to add is the project root, which contains BOTH 'FrontEnd' and 'source'.
# Since we are running from 'FrontEnd', we need to add the parent directory ('..') to the path.
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(project_root)
# ---------------------------------------------------------------------------------

# 1. TEST PATHING
try:
    # We import directly from the 'source' package since the root is now in sys.path.
    import source.db as db_module
    
    # If the import succeeds, the connection test inside db.py will run and print
    # its success or failure to the terminal.
    
except ImportError as e:
    st.error(f"🔴 FAILED TO LOCATE MODULE. PATHING ERROR: {e}")
    st.info(f"The system searched in these directories: {sys.path}")
    st.stop()
except Exception as e:
    st.error(f"🔴 FAILED DURING DB INITIALIZATION. Connection or package error: {e}")
    st.stop()
    
# Import the logic functions, which rely on the connection setup in db_module
from source.logic import (
    log_activity, 
    get_user_dashboard_data, 
    get_all_categories, 
    get_recommendations
)


# --- Streamlit App Configuration and UI Logic (REMAINS THE SAME) ---

# 1. Page Config
st.set_page_config(
    page_title="Echo Footprint Tracker",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. State Initialization (Example User ID - Replace with actual auth in the final version)
if 'user_id' not in st.session_state:
    # Placeholder User ID until proper authentication is implemented
    st.session_state.user_id = 1 

# 3. Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Log Activity", "Recommendations"])
st.sidebar.markdown("---")
st.sidebar.caption(f"Current User ID: {st.session_state.user_id}")


# --- Helper Function to Render Dashboard ---

def render_dashboard(user_id):
    st.title("🌱 Carbon Footprint Dashboard")
    st.markdown("Monitor your environmental impact and track your progress towards a sustainable lifestyle.")
    
    data = get_user_dashboard_data(user_id)

    if data.get("error"):
        st.error(f"Error loading dashboard data: {data['error']}")
        return

    activities = data.get("activities", [])
    logs = data.get("logs", [])

    col1, col2 = st.columns(2)
    
    # 3.1 Total Emission Log
    total_log = sum(log['total_emission'] for log in logs) if logs else 0
    with col1:
        st.metric(
            label="Total Emissions (Last 30 days)", 
            value=f"{total_log:,.2f} kg CO2e",
            delta="Analyze Trends" # Placeholder for future trend data
        )
        st.markdown("### Recent Activities")
        if activities:
            st.dataframe(
                data=[
                    {
                        "Date": a.get("date", "N/A"), 
                        "Description": a.get("description", "N/A"),
                        "Emission (kg CO2e)": f"{a.get('total_emission', 0):.2f}"
                    } 
                    for a in activities[:5]
                ],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No activities logged yet. Head over to the 'Log Activity' page!")

    # 3.2 Visualization Placeholder
    with col2:
        st.markdown("### Emission Trend Over Time")
        # Placeholder for a chart (requires pandas/altair data manipulation)
        if logs:
            st.line_chart(
                data=[
                    {"date": log['log_date'], "emissions": log['total_emission']}
                    for log in logs
                ],
                x="date",
                y="emissions"
            )
        else:
            st.info("Data logging will populate this chart.")

def render_log_activity(user_id):
    st.title("✏️ Log New Activity")
    st.markdown("Enter details about an activity to calculate and track your carbon footprint.")

    categories_data = get_all_categories()
    
    if categories_data.get("error"):
        st.error(f"Could not load activity categories: {categories_data['error']}")
        return

    categories = categories_data.get("data", [])
    category_map = {c['name']: c['id'] for c in categories}
    category_names = list(category_map.keys())

    with st.form("activity_form"):
        # Input Fields
        col_cat, col_val = st.columns([2, 1])
        with col_cat:
            selected_category_name = st.selectbox("Category", category_names)
        
        selected_category_id = category_map.get(selected_category_name)
        
        with col_val:
            value = st.number_input("Value", min_value=0.01, step=0.1)

        description = st.text_input("Description (e.g., '10-mile drive home', 'Weekly grocery shopping')")
        unit = st.selectbox("Unit (e.g., miles, kWh, currency)", ["mile", "km", "kWh", "USD", "count"]) # Example units
        date_input = st.date_input("Date", datetime.date.today())

        submitted = st.form_submit_button("Calculate & Log Footprint")

        if submitted:
            if not selected_category_id or not value or not description:
                st.error("Please fill in all required fields.")
            else:
                try:
                    date_str = date_input.isoformat()
                    result = log_activity(
                        user_id=user_id,
                        category_id=selected_category_id,
                        description=description,
                        value=float(value),
                        unit=unit,
                        date=date_str
                    )

                    if result.get("success"):
                        st.success(f"Activity logged successfully! Estimated Footprint: **{result['emission']:.2f} kg CO2e**")
                    else:
                        st.error(f"Failed to log activity: {result['error']}")

                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

def render_recommendations(user_id):
    st.title("💡 Personalized Sustainability Tips")
    st.markdown("Based on your logged activities, here are some actionable steps you can take to reduce your carbon footprint.")
    
    recommendation_data = get_recommendations(user_id)
    
    if recommendation_data.get("error"):
        st.error(f"Could not load recommendations: {recommendation_data['error']}")
        return

    suggestions = recommendation_data.get("suggestions", [])
    
    if suggestions:
        st.subheader("Your Top Reduction Opportunities:")
        for i, suggestion in enumerate(suggestions):
            st.info(f"**Tip {i+1}:** {suggestion}")
            
        st.markdown("---")
        st.caption("These suggestions are based on your highest-emitting categories.")
    else:
        st.info("Log some activities first to receive personalized recommendations!")


# --- Main App Router ---

if page == "Dashboard":
    render_dashboard(st.session_state.user_id)
elif page == "Log Activity":
    render_log_activity(st.session_state.user_id)
elif page == "Recommendations":
    render_recommendations(st.session_state.user_id)
