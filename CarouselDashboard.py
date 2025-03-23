import streamlit as st
import pandas as pd
import datetime
import random

def carousel_dashboard():
    """Fixed featured ideas carousel dashboard that works properly in Streamlit"""
    
    # Page config
    st.set_page_config(page_title="Featured Ideas Dashboard", layout="wide")
    
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
        .featured-card {
            background-color: #fff8e6;
            border-left: 4px solid #f9ab00;
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
        .featured-badge {
            display: inline-block;
            padding: 4px 8px;
            background-color: #fef3c7;
            color: #d97706;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 5px;
        }
        .vote-count {
            display: inline-flex;
            align-items: center;
            font-weight: bold;
            color: #4a6fa5;
        }
        .section-title {
            font-size: 20px;
            font-weight: bold;
            color: #4a6fa5;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #e1ebf5;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .section-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #4a6fa5;
            color: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            font-size: 14px;
            margin-left: 8px;
        }
        .view-all {
            font-size: 14px;
            color: #4a6fa5;
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("Automation Ideas Hub")
    st.write("Discover and collaborate on automation ideas")
    
    # Header buttons
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        st.button("My Ideas", use_container_width=True)
    with col3:
        st.button("Submit New Idea", use_container_width=True)
    
    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Home", "Trending", "Categories", "My Watchlist"])
    
    with tab1:  # Home tab
        # Featured Ideas section
        st.markdown("<h2 style='text-align: center; color: #4a6fa5; margin: 20px 0;'>Featured Ideas</h2>", unsafe_allow_html=True)
        
        # Carousel implementation using columns instead of HTML carousel
        carousel_items = st.columns(3)
        
        # Featured idea 1
        with carousel_items[0]:
            st.markdown("""
            <div class="featured-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <div>
                        <span class="featured-badge">Featured</span>
                        <span class="status-tag status-progress">In Progress</span>
                    </div>
                    <span style="color: #666; font-size: 0.9rem;">Feb 15, 2024</span>
                </div>
                <h3>Email Response Classifier</h3>
                <p>ML system to classify customer emails by urgency and route them to appropriate team members, saving support team hours each day.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Customer Support</span>
                    <span class="badge badge-yellow">Long</span>
                </div>
                <div style="margin: 10px 0;">
                    <span class="badge badge-purple">Machine Learning</span>
                    <span class="badge badge-purple">API Integration</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">38 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View Details</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Featured idea 2
        with carousel_items[1]:
            st.markdown("""
            <div class="featured-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <div>
                        <span class="featured-badge">Featured</span>
                        <span class="status-tag status-approved">Approved</span>
                    </div>
                    <span style="color: #666; font-size: 0.9rem;">Jan 20, 2024</span>
                </div>
                <h3>Onboarding Process Automation</h3>
                <p>Automate employee onboarding process with document generation, approval workflows, and IT setup requests.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">HR</span>
                    <span class="badge badge-yellow">Medium</span>
                </div>
                <div style="margin: 10px 0;">
                    <span class="badge badge-purple">Workflow</span>
                    <span class="badge badge-purple">Custom Software</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">22 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View Details</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Featured idea 3
        with carousel_items[2]:
            st.markdown("""
            <div class="featured-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <div>
                        <span class="featured-badge">Featured</span>
                        <span class="status-tag status-progress">In Progress</span>
                    </div>
                    <span style="color: #666; font-size: 0.9rem;">Feb 25, 2024</span>
                </div>
                <h3>Employee Leave Management</h3>
                <p>Automated system for leave requests, approvals, and calendar integration to streamline PTO management.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">HR</span>
                    <span class="badge badge-yellow">Medium</span>
                </div>
                <div style="margin: 10px 0;">
                    <span class="badge badge-purple">Custom Software</span>
                    <span class="badge badge-purple">API Integration</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">21 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View Details</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Carousel navigation (just for show - non-functional in this simplified version)
        col1, col2, col3 = st.columns([5, 1, 5])
        with col2:
            st.markdown("""
            <div style="display: flex; justify-content: center; margin: 10px 0 30px 0;">
                <div style="width: 10px; height: 10px; background-color: #4a6fa5; border-radius: 50%; margin: 0 5px;"></div>
                <div style="width: 10px; height: 10px; background-color: #ccc; border-radius: 50%; margin: 0 5px;"></div>
                <div style="width: 10px; height: 10px; background-color: #ccc; border-radius: 50%; margin: 0 5px;"></div>
            </div>
            """, unsafe_allow_html=True)
        
        # Recent Ideas section
        st.markdown("""
        <div class="section-title">
            Recently Added
            <span class="section-badge">7</span>
            <span style="flex-grow: 1;"></span>
            <a href="#" class="view-all">View All</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Display recent ideas in 2 columns
        recent_cols = st.columns(2)
        
        # Recent idea 1
        with recent_cols[0]:
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-review">Under Review</span>
                    <span style="color: #666; font-size: 0.9rem;">Mar 20, 2024</span>
                </div>
                <h3>Invoice Processing Bot</h3>
                <p>RPA bot to extract data from incoming invoices and enter it into our accounting system.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Finance</span>
                    <span class="badge badge-yellow">Short</span>
                    <span class="badge badge-purple">RPA</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">7 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Recent idea 2
        with recent_cols[1]:
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-review">Under Review</span>
                    <span style="color: #666; font-size: 0.9rem;">Mar 18, 2024</span>
                </div>
                <h3>Inventory Prediction System</h3>
                <p>ML-based system that predicts inventory needs based on historical data and seasonal trends.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Logistics</span>
                    <span class="badge badge-yellow">Long</span>
                    <span class="badge badge-purple">ML</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">9 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Top Voted Ideas section
        st.markdown("""
        <div class="section-title">
            Top Voted Ideas
            <span class="section-badge">5</span>
            <span style="flex-grow: 1;"></span>
            <a href="#" class="view-all">View All</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Display top ideas in 2 columns
        top_cols = st.columns(2)
        
        # Top idea 1
        with top_cols[0]:
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-approved">Approved</span>
                    <span style="color: #666; font-size: 0.9rem;">Feb 15, 2024</span>
                </div>
                <h3>Email Response Classifier</h3>
                <p>ML system to classify customer emails by urgency and route them to appropriate team members.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Customer Support</span>
                    <span class="badge badge-yellow">Long</span>
                    <span class="badge badge-purple">ML</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">38 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Top idea 2
        with top_cols[1]:
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-completed">Completed</span>
                    <span style="color: #666; font-size: 0.9rem;">Jan 20, 2024</span>
                </div>
                <h3>Onboarding Process Automation</h3>
                <p>Automate employee onboarding process with document generation and workflows.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">HR</span>
                    <span class="badge badge-yellow">Medium</span>
                    <span class="badge badge-purple">Workflow</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">22 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Ideas by Department section
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="section-title">
                Sales & Marketing
                <span class="section-badge">8</span>
                <span style="flex-grow: 1;"></span>
                <a href="#" class="view-all">View All</a>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-review">Under Review</span>
                    <span style="color: #666; font-size: 0.9rem;">Mar 15, 2024</span>
                </div>
                <h3>Automated Report Generation</h3>
                <p>Create a system that automatically generates weekly reports from our CRM data.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Sales</span>
                    <span class="badge badge-yellow">Medium</span>
                    <span class="badge badge-purple">Data Analysis</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">12 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="section-title">
                Finance & Operations
                <span class="section-badge">10</span>
                <span style="flex-grow: 1;"></span>
                <a href="#" class="view-all">View All</a>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="idea-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span class="status-tag status-review">Under Review</span>
                    <span style="color: #666; font-size: 0.9rem;">Mar 20, 2024</span>
                </div>
                <h3>Invoice Processing Bot</h3>
                <p>RPA bot to extract data from incoming invoices and enter it into our accounting system.</p>
                <div style="margin: 10px 0;">
                    <span class="badge badge-blue">Finance</span>
                    <span class="badge badge-yellow">Short</span>
                    <span class="badge badge-purple">RPA</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span class="vote-count">7 votes</span>
                    <button style="background-color: #4a6fa5; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;">View</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    carousel_dashboard()