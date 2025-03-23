import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Automation Ideas Heatmap", layout="wide")

# Title and description
st.title("Automation Ideas Heatmap")
st.write("Visualize idea distribution across departments and statuses")

# Add a submit button at the top right
col1, col2 = st.columns([5, 1])
with col2:
    st.button("Submit New Idea", use_container_width=True)

# Key metrics section with native st.metric
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Ideas", value="27", delta="12%")

with col2:
    st.metric(label="Implementation Rate", value="68%", delta="5%")

with col3:
    st.metric(label="Avg Approval Time", value="7.3", delta="-0.8 days")

with col4:
    st.metric(label="Active Contributors", value="42", delta="7")

# Heatmap data
st.subheader("Idea Distribution Heatmap")

# Create the basic data
data = {
    'Department': ['Sales', 'Marketing', 'Finance', 'Operations', 'HR', 'IT', 'Customer Support', 'Total'],
    'Under Review': [2, 1, 1, 1, 0, 1, 0, 6],
    'Approved': [1, 1, 1, 2, 1, 1, 1, 8],
    'In Progress': [1, 0, 1, 2, 1, 1, 1, 7],
    'Completed': [1, 1, 1, 1, 1, 1, 0, 6],
    'Total': [5, 3, 4, 6, 3, 4, 2, 27]
}

# Create DataFrame
df = pd.DataFrame(data)

# Use a custom formatting function to add "idea" or "ideas" labels
def format_values(val):
    if val == 1:
        return f"{val}\nidea"
    else:
        return f"{val}\nideas"

# Apply the formatting to all columns except Department
formatted_df = df.copy()
for col in formatted_df.columns:
    if col != 'Department':
        formatted_df[col] = formatted_df[col].apply(format_values)

# Function to color cells based on value
def color_cells(val):
    if isinstance(val, str):
        # Extract the number from the formatted string
        try:
            num = int(val.split('\n')[0])
        except:
            return ''
    else:
        num = val

    # Color coding based on value ranges
    if num == 0:
        return 'background-color: #f0f0f5; color: #999999;'
    elif num == 1:
        return 'background-color: #e3f2fd; color: #1976d2;'
    elif num <= 3:
        return 'background-color: #bbdefb; color: #1976d2;'
    elif num <= 5:
        return 'background-color: #90caf9; color: #0d47a1;'
    elif num <= 8:
        return 'background-color: #64b5f6; color: white;'
    else:
        return 'background-color: #42a5f5; color: white;'

# Apply styling
try:
    # For newer pandas versions
    styled_df = formatted_df.style.applymap(
        color_cells, 
        subset=pd.IndexSlice[:, [col for col in formatted_df.columns if col != 'Department']]
    ).set_properties(**{
        'text-align': 'center',
        'font-size': '16px',
        'padding': '12px',
        'white-space': 'pre-wrap'  # This preserves line breaks in cells
    }).set_properties(
        subset=['Department'],
        **{'text-align': 'left', 'font-weight': 'bold', 'color': '#4a6fa5'}
    ).hide_index()
except:
    # For older pandas versions
    styled_df = formatted_df.style.applymap(
        color_cells, 
        subset=[col for col in formatted_df.columns if col != 'Department']
    ).set_properties(**{
        'text-align': 'center',
        'font-size': '16px',
        'padding': '12px',
        'white-space': 'pre-wrap'
    }).set_properties(
        subset=['Department'],
        **{'text-align': 'left', 'font-weight': 'bold', 'color': '#4a6fa5'}
    )
    # Older pandas versions might not have hide_index

# Display the heatmap
st.dataframe(styled_df, height=400, use_container_width=True)

# Color legend explanation
st.caption("Color Legend: Darker blue indicates higher number of ideas")
legend_cols = st.columns(6)

with legend_cols[0]:
    st.markdown('<div style="background-color: #f0f0f5; color: #999999; text-align: center; padding: 5px; border-radius: 4px;">0</div>', unsafe_allow_html=True)
with legend_cols[1]:
    st.markdown('<div style="background-color: #e3f2fd; color: #1976d2; text-align: center; padding: 5px; border-radius: 4px;">1</div>', unsafe_allow_html=True)
with legend_cols[2]:
    st.markdown('<div style="background-color: #bbdefb; color: #1976d2; text-align: center; padding: 5px; border-radius: 4px;">2-3</div>', unsafe_allow_html=True)
with legend_cols[3]:
    st.markdown('<div style="background-color: #90caf9; color: #0d47a1; text-align: center; padding: 5px; border-radius: 4px;">4-5</div>', unsafe_allow_html=True)
with legend_cols[4]:
    st.markdown('<div style="background-color: #64b5f6; color: white; text-align: center; padding: 5px; border-radius: 4px;">6-8</div>', unsafe_allow_html=True)
with legend_cols[5]:
    st.markdown('<div style="background-color: #42a5f5; color: white; text-align: center; padding: 5px; border-radius: 4px;">9+</div>', unsafe_allow_html=True)

# Selected idea details section
st.subheader("Operations - Approved Ideas (2)")
export_col1, export_col2 = st.columns([6, 1])
with export_col2:
    st.download_button(
        label="Export as CSV",
        data="Resource Allocation Optimizer,Operations,Approved,Medium,Custom Software;Data Analysis,18,2024-02-22\nAutomated Document Workflow,Operations,Approved,Medium,Workflow;API Integration,14,2024-01-15",
        file_name="operations_approved_ideas.csv",
        mime="text/csv"
    )

# Display idea details
idea_cols = st.columns(2)

with idea_cols[0]:
    st.markdown("""
    <style>
    .idea-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .status-tag {
        background-color: #e1f5e9;
        color: #34a853;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
        display: inline-block;
    }
    .idea-tag {
        background-color: #e9e1f5;
        color: #7a4af0;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
        font-size: 14px;
    }
    .time-tag {
        background-color: #fbf3db;
        color: #f9ab00;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
        font-size: 14px;
    }
    </style>
    
    <div class="idea-card">
        <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
            <span class="status-tag">Approved</span>
            <span style="color: #666; font-size: 14px;">2024-02-22</span>
        </div>
        <h3 style="margin-top: 0; margin-bottom: 12px;">Resource Allocation Optimizer</h3>
        <p>System to intelligently allocate resources based on project priorities and team availability.</p>
        <div style="margin: 12px 0;">
            <span class="time-tag">Medium</span>
            <span class="idea-tag">Custom Software</span>
            <span class="idea-tag">Data Analysis</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: bold; color: #4a6fa5;">↑ 18 votes</span>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">View Details</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with idea_cols[1]:
    st.markdown("""
    <div class="idea-card">
        <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
            <span class="status-tag">Approved</span>
            <span style="color: #666; font-size: 14px;">2024-01-15</span>
        </div>
        <h3 style="margin-top: 0; margin-bottom: 12px;">Automated Document Workflow</h3>
        <p>System to route documents through approval processes with notifications and tracking.</p>
        <div style="margin: 12px 0;">
            <span class="time-tag">Medium</span>
            <span class="idea-tag">Workflow</span>
            <span class="idea-tag">API Integration</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: bold; color: #4a6fa5;">↑ 14 votes</span>
            <button style="background-color: #4a6fa5; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">View Details</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Technology usage section
st.subheader("Technologies Used Across Departments")

# Create the technology data
tech_data = {
    'Department': ['Sales', 'Marketing', 'Finance', 'Operations', 'HR', 'IT', 'Customer Support'],
    'API Integration': [5, 4, 3, 4, 2, 5, 3],
    'Machine Learning': [2, 1, 1, 2, 0, 3, 2],
    'RPA': [1, 0, 3, 2, 1, 1, 0],
    'Data Analysis': [4, 3, 2, 3, 1, 2, 1],
    'Web Scraping': [2, 1, 0, 1, 0, 3, 1],
    'Custom Software': [3, 2, 1, 4, 2, 4, 2]
}

# Create DataFrame for tech data
tech_df = pd.DataFrame(tech_data)

# Apply the same styling
try:
    # For newer pandas versions
    tech_styled_df = tech_df.style.applymap(
        color_cells, 
        subset=pd.IndexSlice[:, [col for col in tech_df.columns if col != 'Department']]
    ).set_properties(**{
        'text-align': 'center',
        'font-size': '16px',
        'padding': '12px'
    }).set_properties(
        subset=['Department'],
        **{'text-align': 'left', 'font-weight': 'bold', 'color': '#4a6fa5'}
    ).hide_index()
except:
    # For older pandas versions
    tech_styled_df = tech_df.style.applymap(
        color_cells, 
        subset=[col for col in tech_df.columns if col != 'Department']
    ).set_properties(**{
        'text-align': 'center',
        'font-size': '16px',
        'padding': '12px'
    }).set_properties(
        subset=['Department'],
        **{'text-align': 'left', 'font-weight': 'bold', 'color': '#4a6fa5'}
    )

# Display the tech heatmap
st.dataframe(tech_styled_df, height=300, use_container_width=True)