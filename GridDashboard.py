import streamlit as st
import pandas as pd
import datetime
import random

def grid_filter_dashboard():
    """Fixed grid dashboard with advanced filtering that works properly in Streamlit"""
    
    # Page config
    st.set_page_config(page_title="Grid Dashboard", layout="wide")
    
    # Custom CSS - simplified for better compatibility
    st.markdown("""
    <style>
        .idea-card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        .badge-blue {
            background-color: #e1ebf5;
            color: #4a6fa5;
        }
        .badge-yellow {
            background-color: #fbf3db;
            color: #f9ab00;
        }
        .badge-purple {
            background-color: #e9e1f5;
            color: #7a4af0;
        }
        .status-tag {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }
        .status-review {
            background-color: #fbf3db;
            color: #f9ab00;
        }
        .status-approved {
            background-color: #e1f5e9;
            color: #34a853;
        }
        .status-progress {
            background-color: #e1ebf5;
            color: #4a6fa5;
        }
        .status-completed {
            background-color: #e9e1f5;
            color: #7a4af0;
        }
        .vote-count {
            display: inline-flex;
            align-items: center;
            font-weight: bold;
            color: #4a6fa5;
        }
        .filter-section {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .filter-title {
            font-weight: bold;
            color: #4a6fa5;
            margin-bottom: 10px;
        }
        .sort-option {
            display: inline-block;
            padding: 6px 12px;
            margin-right: 10px;
            border-radius: 4px;
            font-size: 14px;
            cursor: pointer;
        }
        .sort-active {
            background-color: #4a6fa5;
            color: white;
        }
        .sort-inactive {
            background-color: #f2f5f9;
            color: #4a6fa5;
        }
        .page-navigation {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .page-item {
            display: inline-block;
            width: 30px;
            height: 30px;
            text-align: center;
            line-height: 30px;
            margin: 0 5px;
            border-radius: 4px;
            cursor: pointer;
        }
        .page-active {
            background-color: #4a6fa5;
            color: white;
        }
        .page-inactive {
            background-color: #f2f5f9;
            color: #4a6fa5;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("Automation Ideas Hub")
    st.write("Browse and filter automation ideas across the organization")
    
    # Create layout with sidebar for filters
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Submit New Idea", key="submit_button", use_container_width=True):
            st.session_state['view'] = 'form'
            st.experimental_rerun()
    
    # Main layout with sidebar
    sidebar_col, main_col = st.columns([1, 3])
    
    # Sample data for ideas
    sample_ideas = [
        {
            "id": 1,
            "title": "Email Response Classifier",
            "description": "ML system to classify customer emails by urgency and route them to appropriate team members.",
            "department": "Customer Support",
            "timeframe": "Long",
            "tech": ["Machine Learning", "API Integration"],
            "status": "Approved",
            "date": "2024-03-10",
            "votes": 38
        },
        {
            "id": 2,
            "title": "Invoice Processing Bot",
            "description": "RPA bot to extract data from incoming invoices and enter it into our accounting system.",
            "department": "Finance",
            "timeframe": "Short",
            "tech": ["RPA"],
            "status": "In Progress",
            "date": "2024-03-20",
            "votes": 7
        },
        {
            "id": 3,
            "title": "Automated Report Generation",
            "description": "Create a system that automatically generates weekly reports from our CRM data and sends them to stakeholders.",
            "department": "Sales",
            "timeframe": "Medium",
            "tech": ["Data Analysis", "API Integration"],
            "status": "Under Review",
            "date": "2024-03-15",
            "votes": 12
        },
        {
            "id": 4,
            "title": "Meeting Scheduler Assistant",
            "description": "Smart assistant that helps schedule meetings based on participant availability and meeting room resources.",
            "department": "Operations",
            "timeframe": "Medium",
            "tech": ["API Integration", "Custom Software"],
            "status": "Completed",
            "date": "2024-03-05",
            "votes": 15
        },
        {
            "id": 5,
            "title": "Inventory Prediction System",
            "description": "ML-based system that predicts inventory needs based on historical data and seasonal trends.",
            "department": "Logistics",
            "timeframe": "Long",
            "tech": ["Machine Learning", "Data Analysis"],
            "status": "Under Review",
            "date": "2024-03-18",
            "votes": 9
        },
        {
            "id": 6,
            "title": "Employee Leave Management",
            "description": "Automated system for leave requests, approvals, and calendar integration.",
            "department": "HR",
            "timeframe": "Medium",
            "tech": ["Custom Software", "API Integration"],
            "status": "In Progress",
            "date": "2024-02-25",
            "votes": 21
        }
    ]
    
    # Sidebar filters
    with sidebar_col:
        st.subheader("Filters")
        
        # Status filters
        st.markdown("<div class='filter-title'>Status</div>", unsafe_allow_html=True)
        status_under_review = st.checkbox("Under Review", value=True)
        status_approved = st.checkbox("Approved", value=True)
        status_in_progress = st.checkbox("In Progress", value=True)
        status_completed = st.checkbox("Completed", value=True)
        
        # Department filters
        st.markdown("<div class='filter-title'>Department</div>", unsafe_allow_html=True)
        dept_sales = st.checkbox("Sales", value=True)
        dept_marketing = st.checkbox("Marketing", value=True)
        dept_operations = st.checkbox("Operations", value=True)
        dept_finance = st.checkbox("Finance", value=True)
        dept_hr = st.checkbox("HR", value=True)
        dept_it = st.checkbox("IT", value=True)
        dept_support = st.checkbox("Customer Support", value=True)
        dept_logistics = st.checkbox("Logistics", value=True)
        
        # Timeframe filters
        st.markdown("<div class='filter-title'>Implementation Timeframe</div>", unsafe_allow_html=True)
        time_short = st.checkbox("Short", value=True)
        time_medium = st.checkbox("Medium", value=True)
        time_long = st.checkbox("Long", value=True)
        
        # Technologies
        st.markdown("<div class='filter-title'>Technologies</div>", unsafe_allow_html=True)
        tech_api = st.checkbox("API Integration", value=True)
        tech_ml = st.checkbox("Machine Learning", value=True)
        tech_rpa = st.checkbox("RPA", value=True)
        tech_data = st.checkbox("Data Analysis", value=True)
        tech_scraping = st.checkbox("Web Scraping", value=True)
        tech_custom = st.checkbox("Custom Software", value=True)
        
        # Date range
        st.markdown("<div class='filter-title'>Date Submitted</div>", unsafe_allow_html=True)
        date_from = st.date_input("From:", datetime.date(2024, 1, 1))
        date_to = st.date_input("To:", datetime.date(2024, 3, 25))
        
        # Votes range
        st.markdown("<div class='filter-title'>Votes Range</div>", unsafe_allow_html=True)
        min_votes = st.number_input("Min votes:", min_value=0, value=0)
        max_votes = st.number_input("Max votes:", min_value=0, value=100)
        
        # Apply filters button
        if st.button("Apply Filters", use_container_width=True):
            st.success("Filters applied!")
        
        # My activity section
        st.markdown("<div class='filter-title'>My Activity</div>", unsafe_allow_html=True)
        my_ideas = st.checkbox("My Submitted Ideas (5)")
        my_votes = st.checkbox("Ideas I Voted For (12)")
        my_bookmarks = st.checkbox("Bookmarked Ideas (7)")
    
    # Main content area
    with main_col:
        # Sort options
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div style="display: flex; margin-bottom: 20px;">
                <div class="sort-option sort-active">Most Votes</div>
                <div class="sort-option sort-inactive">Newest</div>
                <div class="sort-option sort-inactive">Oldest</div>
                <div class="sort-option sort-inactive">A-Z</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            view_type = st.radio("View:", ["Grid", "List"], horizontal=True)
        
        # Display ideas in a grid
        idea_cols = st.columns(2)
        
        # Sort ideas by votes (descending)
        sorted_ideas = sorted(sample_ideas, key=lambda x: x['votes'], reverse=True)
        
        # Display ideas in columns
        for i, idea in enumerate(sorted_ideas):
            col_idx = i % 2
            with idea_cols[col_idx]:
                # Determine status class
                status_class = ""
                if idea['status'] == 'Under Review':
                    status_class = "status-review"
                elif idea['status'] == 'Approved':
                    status_class = "status-approved"
                elif idea['status'] == 'In Progress':
                    status_class = "status-progress"
                elif idea['status'] == 'Completed':
                    status_class = "status-completed"
                
                # Build card HTML
                card_html = f"""
                <div class="idea-card">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <span class="status-tag {status_class}">{idea['status']}</span>
                        <span style="color: #666; font-size: 0.9rem;">{idea['date']}</span>
                    </div>
                    <h3>{idea['title']}</h3>
                    <p style="margin-bottom: 10px;">{idea['description']}</p>
                    <div style="margin-bottom: 10px;">
                        <span class="badge badge-blue">{idea['department']}</span>
                        <span class="badge badge-yellow">{idea['timeframe']}</span>
                    </div>
                    <div style="margin-bottom: 10px;">
                """
                
                # Add tech badges
                for tech in idea['tech']:
                    card_html += f'<span class="badge badge-purple">{tech}</span>'
                
                # Add footer with vote count and button
                card_html += f"""
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="vote-count">
                            {idea['votes']} votes
                        </span>
                        <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View Details</button>
                    </div>
                </div>
                """
                
                st.markdown(card_html, unsafe_allow_html=True)
        
        # Pagination
        st.markdown("""
        <div class="page-navigation">
            <div class="page-item">Prev</div>
            <div class="page-item page-active">1</div>
            <div class="page-item page-inactive">2</div>
            <div class="page-item page-inactive">3</div>
            <div class="page-item page-inactive">4</div>
            <div class="page-item page-inactive">5</div>
            <div class="page-item">Next</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    grid_filter_dashboard()