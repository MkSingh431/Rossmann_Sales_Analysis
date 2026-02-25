import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


st.set_page_config(page_title='SuperStore!!!',page_icon=':bar_chart',layout='wide')
st.title('Rossmann Analysis Dashboard')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# Load the data
data=pd.read_csv("C:\\Programmings\\Projects\\Store\\rossman.csv",encoding='ISO-8859-1')

# If using a Streamlit file uploader
uploaded_file = st.file_uploader("Choose an Excel file")
if uploaded_file:
    data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data = data.dropna(subset=['Date']).copy()
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.strftime('%B')
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Initial Sidebar setup
with st.sidebar:
    # Using st.image for precise 100px width as we discussed
    st.image("logo.png", width=100) 
    st.title('Choose your Filters')
    
    st.subheader('Select Year')
    years = sorted(data['Year'].dropna().astype(int).unique().tolist())
    selected_years = st.multiselect("Pick your Year(s)", years, default=years)

    st.subheader('Select Store Type')
    store_types = sorted(data['StoreType'].dropna().unique().tolist())
    selected_store_types = st.multiselect("Pick Store Type(s)", store_types, default=store_types)
    
    st.subheader("Select Store ID")
    store_ids = sorted(data['Store'].dropna().unique().tolist())
    selected_store_ids = st.multiselect("Pick Store ID(s)", store_ids, default=store_ids)
    
    st.subheader("Follow Mk Singh")
    st.markdown("[LinkedIn](http://www.linkedin.com/in/motilal-das-42b4a9254)")
    st.markdown("[GitHub](https://github.com/MkSingh431)")
    
    
filtered_data = data.copy()
if selected_years:
    filtered_data = filtered_data[filtered_data['Year'].isin(selected_years)]
if selected_store_types:
    filtered_data = filtered_data[filtered_data['StoreType'].isin(selected_store_types)]

if filtered_data.empty:
    st.warning("No data for the selected sidebar filters. Please adjust your selections.")
    st.stop()
        
      

col1, col2,col3,col4,col5 = st.columns(5)

with col1:
    with st.container(border=True):
        total_sales=filtered_data['Sales'].sum()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color: {label_color}; font-size: 20px; margin: 0;">Total Sales</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">${total_sales:,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        total_store=filtered_data['Store'].nunique()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color: {label_color}; font-size: 20px; margin: 0;">Total Store</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{total_store}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        
with col3:
    with st.container(border=True):
        total_customer=filtered_data['Customers'].sum()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color: {label_color}; font-size: 20px; margin: 0;">Total Customers</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{total_customer}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        

with col4:
    with st.container(border=True):
        total_open=filtered_data['Open'].sum()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color: {label_color}; font-size: 20px; margin: 0;">Total Open</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{total_open}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)

with col5:
    total_storetype=filtered_data['StoreType'].unique()
    with st.container(border=True):
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color: {label_color}; font-size: 20px; margin: 0;">Total Store Type</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{len(total_storetype)}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        
st.divider()
        
chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("### Sales by Store Type")
    
    # 1. Aggregate Sales
    sales_by_storetype = filtered_data.groupby('StoreType')['Sales'].sum().sort_values(ascending=True)
    
    # 2. Creating the figure
    fig, ax = plt.subplots(figsize=(6, 4)) # Adjusted size for a 2-column layout
    
    bars = ax.bar(
        sales_by_storetype.index,
        sales_by_storetype.values,
        color=['#F18C10', '#0047AB', '#FF5733', '#33FF57'],
        width=0.6
    )
    
    # 3. Data Labels (Uncommented and correctly indented)
    ax.bar_label(bars, fmt='%.0f', padding=3, fontweight='bold')

    # 4. Styling (Must be indented inside 'with chart1')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_visible(False)

    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    st.pyplot(fig)
        
with chart2:
    st.markdown("### Sales by Month")
    
    # 1. Aggregate Sales
    # Reindexing ensures months are ordered chronologically
    sales_by_month = filtered_data.groupby('Month')['Sales'].sum().reindex(month_order, fill_value=0)
    
    # 2. Creating the figure
    fig, ax = plt.subplots(figsize=(6, 4))
    
    bars = ax.bar(
        sales_by_month.index,
        sales_by_month.values,
        color=['#0047AB','#F18C10','#FF5733','#33FF57','#8A2BE2','#FFD700','#00FFFF','#FF69B4','#A52A2A','#5F9EA0','#D2691E','#FF7F50'],
        width=0.6
    )

    # 3. Styling (Must be indented inside 'with chart2')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_tick_params(labelsize=8)
    
    # Rotation is necessary for long month names
    plt.xticks(rotation=45, ha='right', fontsize=9)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    st.pyplot(fig)        
    
    
view1, view2 = st.columns(2)

with view1:
    with st.expander("Sales by Store Type"):
        # 1. Prepare the data
        st_data = filtered_data.groupby('StoreType')['Sales'].sum().reset_index()
        
        # 2. Apply the color styling
        # 'cmap' can be 'YlOrRd', 'Blues', 'Greens', or 'magma'
        styled_df = st_data.style.background_gradient(cmap='YlOrRd', subset=['Sales']).format({'Sales': '${:,.2f}'})
        
        # 3. Display in Streamlit
        st.dataframe(styled_df, width='stretch')
        
with view2:
    
    
    with st.expander("Sales by Month"):
        # 1. Prepare the data
        sm_data = filtered_data.groupby('Month')['Sales'].sum().reindex(month_order, fill_value=0)
        
        # 2. Apply the color styling
        styled_df = sm_data.to_frame().style.background_gradient(cmap='Blues', subset=['Sales']).format({'Sales': '${:,.2f}'})
        
        # 3. Display in Streamlit
        st.dataframe(styled_df, width='stretch')
        
st.divider()

chart3, chart4 = st.columns(2)

with chart3:
    st.markdown("### Sales by Year")
    sales_by_year = filtered_data.groupby('Year')['Sales'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(
        sales_by_year.index.astype(str),
        sales_by_year.values,
        color=['#F18C10', '#0047AB', '#FF5733', '#33FF57'],
        width=0.6
    )
    ax.bar_label(bars, fmt='%.0f', padding=3, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_visible(False)
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    st.pyplot(fig)        
    
# sales_by_competition = data.groupby("CompetitionDistance")["Sales"].mean()
# plt.plot(sales_by_competition)
# plt.xlabel("Competition Distance")
# plt.ylabel("Sales")
# plt.title("Sales by Competiotion Distance")
# plt.show()

with chart4:
    st.markdown("### Sales by Competition Distance")
    
    # 1. Grouping and calculating mean (as per your request)
    sales_by_competition = data.groupby("CompetitionDistance")["Sales"].mean()
    
    # 2. Creating the Figure and Axes objects
    # This is required in Streamlit to avoid "Global State" plotting errors
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # 3. Plotting on the 'ax' object
    ax.plot(sales_by_competition.index, sales_by_competition.values, color='#0047AB')
    
    # Dashboard Styling: removing borders and matching background
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.patch.set_alpha(0) # Transparent background
    
    plt.tight_layout()
    
    # 5. Display the figure in the Streamlit column
    st.pyplot(fig) 
    
    
view1, view2 = st.columns(2)
with view1:
    with st.expander("Sales by Year"):
        sales_by_year = filtered_data.groupby('Year')['Sales'].sum().reset_index()
        styled_df = sales_by_year.style.background_gradient(cmap='Greens', subset=['Sales']).format({'Sales': '${:,.2f}'})
        st.dataframe(styled_df, width='stretch')
        
with view2:
    with st.expander("Sales by Competition Distance"):
        sales_by_competition = data.groupby("CompetitionDistance")["Sales"].mean().reset_index()
        styled_df = sales_by_competition.style.background_gradient(cmap='magma', subset=['Sales']).format({'Sales': '${:,.2f}'})
        st.dataframe(styled_df, width='stretch')
            
st.divider()            
            
chart5,chart6=st.columns(2)

with chart5:
    st.markdown("### Total Sales by State Holiday")
    
    # 1. Define labels and mapping
    labels = ['No Holiday', 'Public Holiday', 'Easter Holiday', 'Christmas Holiday']
    holiday_map = {'0': 'No Holiday', 'a': 'Public Holiday', 'b': 'Easter Holiday', 'c': 'Christmas Holiday'}
    
    # 2. Calculation: Grouping and reindexing to ensure consistent order
    # We use .sum() as per your initial logic
    holiday_data = data.groupby('StateHoliday')['Sales'].sum().reindex(['0', 'a', 'b', 'c']).fillna(0)
    
    # 3. Plotting
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        labels, 
        holiday_data.values, 
        color=['#2E8B57', '#CD5C5C', '#9370DB', '#00CED1'], 
        width=0.6
    )
    
    # 4. Adding Value Labels (Truth-telling: showing the scale clearly)
    ax.bar_label(bars, fmt='%.0f', padding=3, fontweight='bold', fontsize=9)
    
    # 5. Styling for the Dashboard
    ax.set_ylabel('Total Sales')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_visible(False) # Hide Y-axis since we have bar labels
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig)   
    
with chart6:
    st.markdown("### School Holiday Sales Impact")
    
    # 1. Calculation: Grouping by SchoolHoliday (0 or 1)
    # We calculate both to give you the option, but we'll plot the Mean for 'truth'
    school_holiday_stats = data.groupby('SchoolHoliday')['Sales'].agg(['sum', 'mean'])
    
    # 2. Prepare labels
    labels = ['Not School Holiday', 'School Holiday']
    
    # 3. Create the figure
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Using the Mean to show the real performance comparison
    bars = ax.bar(
        labels, 
        school_holiday_stats['sum'], 
        color=['#0047AB', '#F18C10'], # Blue and Orange as requested
        width=0.5
    )
    
    # 4. Adding Data Labels (Average Sales per Day)
    ax.bar_label(bars, fmt='%.0f', padding=3, fontweight='bold')
    
    # 5. Styling to match your clean dashboard look
    ax.set_ylabel('Average Sales per Day')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_visible(False)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig) 
    
view1, view2 = st.columns(2)

with view1:
    with st.expander("Sales by State Holiday"):
        labels = ['No Holiday', 'Public Holiday', 'Easter Holiday', 'Christmas Holiday']
        holiday_map = {'0': 'No Holiday', 'a': 'Public Holiday', 'b': 'Easter Holiday', 'c': 'Christmas Holiday'}
        holiday_data = data.groupby('StateHoliday')['Sales'].sum().reindex(['0', 'a', 'b', 'c']).fillna(0).reset_index()
        holiday_data['StateHoliday'] = holiday_data['StateHoliday'].map(holiday_map)
        styled_df = holiday_data.style.background_gradient(cmap='YlOrRd', subset=['Sales']).format({'Sales': '${:,.2f}'})
        st.dataframe(styled_df, width='stretch')

with view2:
    with st.expander("School Holiday Sales Impact"):
        school_holiday_stats = data.groupby('SchoolHoliday')['Sales'].agg(['sum', 'mean']).reset_index()
        school_holiday_stats['SchoolHoliday'] = school_holiday_stats['SchoolHoliday'].map({0: 'Not School Holiday', 1: 'School Holiday'})
        styled_df = school_holiday_stats.style.background_gradient(cmap='Blues', subset=['sum']).format({'sum   ': '${:,.2f}', 'mean': '${:,.2f}'})
        st.dataframe(styled_df, width='stretch') 
    

    
    
    
    
    
    
    