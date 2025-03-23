import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random

def analytics_dashboard():
    """Analytics dashboard with metrics and charts"""
    
    # Apply neumorphism styling
    st.markdown("""
    <style>
        /* Neumorphism styles omitted for brevity */
        .metrics-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #e0e5ec;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 8px 8px 16px #bec4ca, -8px -8px 16px #ffffff;
            text-align: center;
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #4a6fa5;
            margin: 0.5rem 0;
        }
        .metric-label {
            color: #666;
            font-size: 1rem;
        }
        .chart-container {
            background-color: #e0e5ec;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 8px 8px 16px #bec4ca, -8px -8px 16px #ffffff;
            margin-bottom: 1.5rem;
        }
        .chart-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #4a6fa5;
            margin-bottom: 1rem;
        }
        .table-compact {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0 6px;
        }
        .table-compact th {
            text-align: left;
            color: #4a6fa5;
            font-weight: 600;
            padding: 0.5rem;
        }
        .table-compact td {
            padding: 0.75rem 0.5rem;
        }
        .table-compact tbody tr {
            background-color: #e0e5ec;
            border-radius: 8px;
            box-shadow: 3px 3px 6px #bec4ca, -3px -3px 6px #ffffff;
        }
        .table-compact td:first-child {
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
        }
        .table-compact td:last-child {
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with navigation
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
        <div>
            <h1 style="margin-bottom: 0.5rem;">Automation Ideas Analytics</h1>
            <p style="color: #666;">Overview of automation ideas and implementation statistics</p>
        </div>
        <div>
            <button class="neuro-button">Submit New Idea</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    st.markdown("""
    <div class="metrics-container">
        <div class="metric-card">
            <div class="metric-value">27</div>
            <div class="metric-label">Total Ideas</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">12</div>
            <div class="metric-label">In Progress</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">8</div>
            <div class="metric-label">Completed</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">78%</div>
            <div class="metric-label">Approval Rate</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Ideas by Department</div>
            <img src="https://via.placeholder.com/450x250?text=Department+Distribution+Chart" width="100%" />
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Ideas by Status</div>
            <img src="https://via.placeholder.com/450x250?text=Status+Distribution+Chart" width="100%" />
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Ideas Submission Trend</div>
            <img src="https://via.placeholder.com/450x250?text=Submission+Trend+Chart" width="100%" />
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Implementation Timeline</div>
            <img src="https://via.placeholder.com/450x250?text=Implementation+Timeline+Chart" width="100%" />
        </div>
        """, unsafe_allow_html=True)
    
    # Top ideas section
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Top-Voted Ideas</div>
        <table class="table-compact">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Department</th>
                    <th>Status</th>
                    <th>Votes</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Automated Report Generation</td>
                    <td>Sales</td>
                    <td><span class="status-tag status-approved">Approved</span></td>
                    <td>42</td>
                    <td><button class="neuro-button" style="padding: 4px 8px; font-size: 0.8rem;">View</button></td>
                </tr>
                <tr>
                    <td>Email Response Classifier</td>
                    <td>Customer Support</td>
                    <td><span class="status-tag status-progress">In Progress</span></td>
                    <td>38</td>
                    <td><button class="neuro-button" style="padding: 4px 8px; font-size: 0.8rem;">View</button></td>
                </tr>
                <tr>
                    <td>Invoice Processing Bot</td>
                    <td>Finance</td>
                    <td><span class="status-tag status-completed">Completed</span></td>
                    <td>35</td>
                    <td><button class="neuro-button" style="padding: 4px 8px; font-size: 0.8rem;">View</button></td>
                </tr>
                <tr>
                    <td>Meeting Scheduler Assistant</td>
                    <td>Operations</td>
                    <td><span class="status-tag status-review">Under Review</span></td>
                    <td>29</td>
                    <td><button class="neuro-button" style="padding: 4px 8px; font-size: 0.8rem;">View</button></td>
                </tr>
                <tr>
                    <td>Inventory Prediction System</td>
                    <td>Logistics</td>
                    <td><span class="status-tag status-progress">In Progress</span></td>
                    <td>24</td>
                    <td><button class="neuro-button" style="padding: 4px 8px; font-size: 0.8rem;">View</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    # Technologies used section
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Popular Technologies</div>
        <img src="https://via.placeholder.com/950x200?text=Technologies+Usage+Chart" width="100%" />
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Analytics Dashboard", layout="wide")
    analytics_dashboard()