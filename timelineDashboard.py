import streamlit as st
import pandas as pd
import datetime
import random

def timeline_dashboard():
    """Fixed timeline dashboard that works properly in Streamlit"""
    
    # Page config
    st.set_page_config(page_title="Timeline Dashboard", layout="wide")
    
    # Custom CSS - simplified for better compatibility
    st.markdown("""
    <style>
        .timeline-container {
            margin-bottom: 20px;
            border-left: 4px solid #4a6fa5;
            padding-left: 25px;
            position: relative;
        }
        .timeline-item {
            margin-bottom: 30px;
            position: relative;
        }
        .timeline-item:before {
            content: '';
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 3px solid #4a6fa5;
            background: white;
            position: absolute;
            left: -34px;
            top: 0px;
        }
        .timeline-date {
            background-color: #4a6fa5;
            color: white;
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .timeline-content {
            background-color: #f2f5f9;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .month-divider {
            font-weight: bold;
            color: #4a6fa5;
            margin: 30px 0 15px 0;
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
        .filter-pill {
            display: inline-block;
            padding: 8px 16px;
            margin-right: 10px;
            border-radius: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .filter-active {
            background-color: #4a6fa5;
            color: white;
        }
        .filter-inactive {
            background-color: #f2f5f9;
            color: #4a6fa5;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("Automation Ideas Timeline")
    st.write("Chronological view of all automation ideas")
    
    # Submit button in header
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Submit New Idea", key="submit_header"):
            st.session_state['view'] = 'form'
            st.experimental_rerun()
    
    # Filter pills using st.button
    st.write("Filter by status:")
    filter_cols = st.columns(5)
    with filter_cols[0]:
        st.button("All Ideas", key="all", use_container_width=True)
    with filter_cols[1]:
        st.button("Under Review", key="review", use_container_width=True)
    with filter_cols[2]:
        st.button("Approved", key="approved", use_container_width=True)
    with filter_cols[3]:
        st.button("In Progress", key="progress", use_container_width=True)
    with filter_cols[4]:
        st.button("Completed", key="completed", use_container_width=True)
    
    # March 2024 section
    st.markdown("<h2 class='month-divider'>March 2024</h2>", unsafe_allow_html=True)
    
    # Timeline container for March
    st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
    
    # Timeline items for March
    timeline_item1 = """
    <div class="timeline-item">
        <div class="timeline-date">Mar 20, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-review">Under Review</span>
                <span class="vote-count">7 votes</span>
            </div>
            <h3>Invoice Processing Bot</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Finance</span>
                <span class="badge badge-yellow">Short</span>
                <span class="badge badge-purple">RPA</span>
            </div>
            <p>RPA bot to extract data from incoming invoices and enter it into our accounting system.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item1, unsafe_allow_html=True)
    
    timeline_item2 = """
    <div class="timeline-item">
        <div class="timeline-date">Mar 18, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-review">Under Review</span>
                <span class="vote-count">9 votes</span>
            </div>
            <h3>Inventory Prediction System</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Logistics</span>
                <span class="badge badge-yellow">Long</span>
                <span class="badge badge-purple">ML</span>
                <span class="badge badge-purple">Data Analysis</span>
            </div>
            <p>ML-based system that predicts inventory needs based on historical data and seasonal trends.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item2, unsafe_allow_html=True)
    
    timeline_item3 = """
    <div class="timeline-item">
        <div class="timeline-date">Mar 15, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-review">Under Review</span>
                <span class="vote-count">12 votes</span>
            </div>
            <h3>Automated Report Generation</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Sales</span>
                <span class="badge badge-yellow">Medium</span>
                <span class="badge badge-purple">Data Analysis</span>
                <span class="badge badge-purple">API</span>
            </div>
            <p>Create a system that automatically generates weekly reports from our CRM data and sends them to stakeholders.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item3, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # February 2024 section
    st.markdown("<h2 class='month-divider'>February 2024</h2>", unsafe_allow_html=True)
    
    # Timeline container for February
    st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
    
    # Timeline items for February
    timeline_item4 = """
    <div class="timeline-item">
        <div class="timeline-date">Feb 28, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-approved">Approved</span>
                <span class="vote-count">15 votes</span>
            </div>
            <h3>Customer Feedback Analysis</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Marketing</span>
                <span class="badge badge-yellow">Medium</span>
                <span class="badge badge-purple">ML</span>
                <span class="badge badge-purple">Data Analysis</span>
            </div>
            <p>System to automatically analyze customer feedback from multiple channels and identify key themes and sentiment.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item4, unsafe_allow_html=True)
    
    timeline_item5 = """
    <div class="timeline-item">
        <div class="timeline-date">Feb 15, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-progress">In Progress</span>
                <span class="vote-count">18 votes</span>
            </div>
            <h3>Email Response Classifier</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Customer Support</span>
                <span class="badge badge-yellow">Long</span>
                <span class="badge badge-purple">ML</span>
                <span class="badge badge-purple">API</span>
            </div>
            <p>ML system to classify customer emails by urgency and route them to appropriate team members.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item5, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # January 2024 section
    st.markdown("<h2 class='month-divider'>January 2024</h2>", unsafe_allow_html=True)
    
    # Timeline container for January
    st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
    
    # Timeline items for January
    timeline_item6 = """
    <div class="timeline-item">
        <div class="timeline-date">Jan 20, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-completed">Completed</span>
                <span class="vote-count">22 votes</span>
            </div>
            <h3>Onboarding Process Automation</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">HR</span>
                <span class="badge badge-yellow">Medium</span>
                <span class="badge badge-purple">Workflow</span>
                <span class="badge badge-purple">Custom Software</span>
            </div>
            <p>Automate employee onboarding process with document generation, approval workflows, and IT setup requests.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item6, unsafe_allow_html=True)
    
    timeline_item7 = """
    <div class="timeline-item">
        <div class="timeline-date">Jan 5, 2024</div>
        <div class="timeline-content">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="status-tag status-completed">Completed</span>
                <span class="vote-count">15 votes</span>
            </div>
            <h3>Meeting Scheduler Assistant</h3>
            <div style="margin: 10px 0;">
                <span class="badge badge-blue">Operations</span>
                <span class="badge badge-yellow">Medium</span>
                <span class="badge badge-purple">API</span>
                <span class="badge badge-purple">Custom Software</span>
            </div>
            <p>Smart assistant that helps schedule meetings based on participant availability and meeting room resources.</p>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; margin-top: 10px;">View Details</button>
        </div>
    </div>
    """
    st.markdown(timeline_item7, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Load more button
    if st.button("Load More Ideas", use_container_width=True):
        st.info("Loading more ideas... (This button is just for demonstration)")

if __name__ == "__main__":
    timeline_dashboard()