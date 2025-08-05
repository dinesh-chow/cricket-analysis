import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="🏏 Cricket Players Stats Tool - Live Version",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize theme in session state (Force dark theme)
if 'dark_theme' not in st.session_state:
    st.session_state.dark_theme = True
# Force reset to dark theme on app reload
st.session_state.dark_theme = True

def apply_theme_css(dark_theme=False):
    """Apply theme-specific CSS based on user preference."""
    if dark_theme:
        # Dark theme CSS
        st.markdown("""
        <style>
            /* Global dark theme */
            .stApp {
                background-color: #0e1117 !important;
                color: #fafafa !important;
            }
            
            .main .block-container {
                background-color: #0e1117 !important;
                color: #fafafa !important;
            }
            
            section[data-testid="stSidebar"] {
                background-color: #262730 !important;
                color: #fafafa !important;
            }
            
            /* Headers and titles */
            .main-header {
                font-size: 3rem;
                color: #58a6ff !important;
                text-align: center;
                margin-bottom: 2rem;
                font-weight: bold;
            }
            
            /* Cards and containers */
            .metric-card, .player-card {
                background-color: #21262d !important;
                padding: 1.5rem;
                border-radius: 0.8rem;
                border: 1px solid #30363d;
                color: #fafafa !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                margin-bottom: 1rem;
            }
            
            /* Universal text styling - FORCE ALL TEXT TO BE LIGHT */
            *, *::before, *::after,
            .stMarkdown, .stMarkdown p, .stMarkdown div, .stMarkdown span, 
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
            div[data-testid="stText"], div[data-testid="stText"] p, div[data-testid="stText"] span,
            .stText, .stText p, .stText span, .element-container div, .element-container p, .element-container span,
            [data-testid="stHeading"], [data-testid="stHeading"] h1, [data-testid="stHeading"] h2, [data-testid="stHeading"] h3,
            p, span, div, h1, h2, h3, h4, h5, h6, label, li, td, th, strong, em, a {
                color: #fafafa !important;
            }
            
            /* Container backgrounds */
            .main .block-container *, section[data-testid="stSidebar"] *,
            .stContainer, .stColumn, .stTabs, .stExpander {
                background-color: transparent !important;
                color: #fafafa !important;
            }
            
            /* Form elements - comprehensive dark styling */
            .stSelectbox > div > div > div, .stTextInput > div > div > input,
            .stSelectbox label, .stTextInput label, .stRadio label, .stMultiSelect label, .stSlider label,
            .stNumberInput label, .stDateInput label, .stTimeInput label, .stTextArea label,
            input, select, textarea, option {
                color: #fafafa !important;
                background-color: #21262d !important;
                border-color: #30363d !important;
            }
            
            /* Metric containers - enhanced dark theme */
            [data-testid="metric-container"] {
                background-color: #21262d !important;
                border: 1px solid #30363d !important;
                color: #fafafa !important;
                border-radius: 0.5rem !important;
            }
            
            [data-testid="metric-container"] * {
                color: #fafafa !important;
            }
            
            /* Tables and dataframes - comprehensive dark styling */
            .dataframe, .dataframe th, .dataframe td, .dataframe thead, .dataframe tbody,
            table, table th, table td, thead, tbody, .stTable, .stDataFrame {
                background-color: #21262d !important;
                color: #fafafa !important;
                border-color: #30363d !important;
            }
            
            /* Tabs styling */
            .stTabs [data-baseweb="tab-list"] {
                background-color: #21262d !important;
            }
            
            .stTabs [data-baseweb="tab"] {
                background-color: #21262d !important;
                color: #fafafa !important;
            }
            
            .stTabs [aria-selected="true"] {
                background-color: #238636 !important;
                color: #ffffff !important;
            }
            
            /* Expander styling */
            .streamlit-expanderHeader {
                background-color: #21262d !important;
                color: #fafafa !important;
            }
            
            .streamlit-expanderContent {
                background-color: #0e1117 !important;
                color: #fafafa !important;
            }
            
            /* Buttons - enhanced styling */
            .stButton > button {
                color: #ffffff !important;
                background-color: #238636 !important;
                border: none !important;
                font-weight: bold !important;
                border-radius: 0.5rem !important;
            }
            
            .stButton > button:hover {
                background-color: #2ea043 !important;
            }
            
            /* Chart containers - comprehensive */
            .js-plotly-plot, .plotly-graph-div, .plotly {
                background-color: #0e1117 !important;
            }
            
            /* Force plotly text to be light */
            .plotly .gtitle, .plotly .xtitle, .plotly .ytitle,
            .plotly text, .plotly .legendtext {
                fill: #fafafa !important;
                color: #fafafa !important;
            }
            
            /* Additional comprehensive styling */
            .stSelectbox > div > div, .stMultiSelect > div > div,
            .stRadio > div > div, .stSlider > div > div,
            [data-baseweb="select"] *, [data-baseweb="popover"] *,
            .css-1d391kg, .css-1cpxqw2, .css-1v3fvcr, .css-10trblm, .css-16idsys {
                color: #fafafa !important;
                background-color: #21262d !important;
            }
            
            /* Sidebar elements */
            .css-1d391kg p, .css-1cpxqw2 p, .css-1v3fvcr p {
                color: #fafafa !important;
            }
            
            /* Info boxes and alerts */
            .stInfo, .stSuccess, .stWarning, .stError {
                background-color: #21262d !important;
                color: #fafafa !important;
                border-color: #30363d !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        # Light theme CSS
        st.markdown("""
        <style>
            .stApp {
                background-color: #ffffff !important;
                color: #262730 !important;
            }
            
            .main .block-container {
                background-color: #ffffff !important;
                color: #262730 !important;
            }
            
            section[data-testid="stSidebar"] {
                background-color: #f0f2f6 !important;
                color: #262730 !important;
            }
            
            .main-header {
                font-size: 3rem;
                color: #1f77b4 !important;
                text-align: center;
                margin-bottom: 2rem;
                font-weight: bold;
            }
            
            .metric-card, .player-card {
                background-color: #ffffff !important;
                padding: 1.5rem;
                border-radius: 0.8rem;
                border: 1px solid #e1e5e9;
                color: #262730 !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 1rem;
            }
            
            /* All text elements - dark text on light background */
            .stMarkdown, .stMarkdown p, .stMarkdown div, .stMarkdown span,
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
            div[data-testid="stText"], div[data-testid="stText"] p, div[data-testid="stText"] span,
            .stText, .stText p, .stText span, .element-container div, .element-container p, .element-container span,
            [data-testid="stHeading"], [data-testid="stHeading"] h1, [data-testid="stHeading"] h2, [data-testid="stHeading"] h3 {
                color: #262730 !important;
            }
            
            /* Force text color for all containers */
            .main .block-container *, section[data-testid="stSidebar"] * {
                color: #262730 !important;
            }
            
            /* Override any conflicting styles */
            p, span, div, h1, h2, h3, h4, h5, h6, label {
                color: #262730 !important;
            }
            
            /* Form elements - light theme */
            .stSelectbox > div > div > div, .stTextInput > div > div > input,
            .stSelectbox label, .stTextInput label, .stRadio label, .stMultiSelect label, .stSlider label {
                color: #262730 !important;
                background-color: #ffffff !important;
            }
            
            /* Metric containers - light theme */
            [data-testid="metric-container"] {
                background-color: #f8f9fa !important;
                border: 1px solid #dee2e6 !important;
                color: #262730 !important;
            }
            
            [data-testid="metric-container"] * {
                color: #262730 !important;
            }
            
            /* Dataframes - light theme */
            .dataframe {
                background-color: #ffffff !important;
                color: #262730 !important;
            }
            
            .dataframe th {
                background-color: #f8f9fa !important;
                color: #262730 !important;
            }
            
            .dataframe td {
                color: #262730 !important;
            }
            
            /* Buttons */
            .stButton > button {
                color: #ffffff !important;
                background-color: #1f77b4 !important;
                border: none !important;
                font-weight: bold !important;
            }
            
            /* Chart containers */
            .js-plotly-plot {
                background-color: #ffffff !important;
            }
            
            /* Additional text visibility fixes */
            .stSelectbox > div > div, .stMultiSelect > div > div,
            .stRadio > div > div, .stSlider > div > div,
            [data-baseweb="select"] *, [data-baseweb="popover"] * {
                color: #262730 !important;
            }
            
            /* Force visibility for any remaining text */
            .css-1d391kg, .css-1cpxqw2, .css-1v3fvcr {
                color: #262730 !important;
            }
        </style>
        """, unsafe_allow_html=True)

# Apply theme CSS
apply_theme_css(st.session_state.dark_theme)

def display_chart(fig):
    """Display chart with dark theme applied."""
    if fig is not None:
        fig = apply_dark_theme_to_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

def apply_dark_theme_to_chart(fig):
    """Apply dark theme styling to plotly charts."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        font=dict(color='#fafafa'),
        title_font=dict(color='#fafafa'),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            bordercolor='#30363d',
            font=dict(color='#fafafa')
        ),
        xaxis=dict(
            gridcolor='#30363d',
            zerolinecolor='#30363d',
            color='#fafafa'
        ),
        yaxis=dict(
            gridcolor='#30363d',
            zerolinecolor='#30363d',
            color='#fafafa'
        )
    )
    return fig

@st.cache_data
def load_data():
    """Load and cache the cricket players data."""
    try:
        df = pd.read_csv('data/cleaned_all_players.csv')
        
        # Process date of birth and calculate age
        df['dateofbirth_clean'] = pd.to_datetime(df['dateofbirth'], format='%d-%m-%Y', errors='coerce')
        current_date = datetime.now()
        df['age'] = ((current_date - df['dateofbirth_clean']).dt.days / 365.25).round(1)
        
        # Clean up missing values
        df['battingstyle'] = df['battingstyle'].fillna('Unknown')
        df['bowlingstyle'] = df['bowlingstyle'].fillna('Unknown')
        df['age'] = df['age'].fillna(0)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_chart_styling(fig, title_color=None):
    """Apply theme-aware styling to charts."""
    if title_color is None:
        title_color = '#fafafa' if st.session_state.dark_theme else '#262730'
    
    text_color = '#fafafa' if st.session_state.dark_theme else '#262730'
    bg_color = '#0e1117' if st.session_state.dark_theme else '#ffffff'
    
    fig.update_layout(
        title=dict(font=dict(color=title_color, size=16)),
        xaxis=dict(
            title=dict(font=dict(color=text_color)),
            tickfont=dict(color=text_color)
        ),
        yaxis=dict(
            title=dict(font=dict(color=text_color)),
            tickfont=dict(color=text_color)
        ),
        plot_bgcolor=bg_color,
        paper_bgcolor=bg_color,
        font=dict(color=text_color)
    )
    return fig

def create_overview_stats(df):
    """Create overview statistics."""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Total Players", f"{len(df):,}")
    
    with col2:
        st.metric("🌍 Countries", df['country_name'].nunique())
    
    with col3:
        st.metric("🏏 Continents", df['continent_name'].nunique())
    
    with col4:
        avg_age = df[df['age'] > 0]['age'].mean()
        st.metric("📅 Average Age", f"{avg_age:.1f}" if not pd.isna(avg_age) else "N/A")

def create_country_chart(df):
    """Create interactive country distribution chart."""
    country_counts = df['country_name'].value_counts().head(15)
    
    fig = px.bar(
        x=country_counts.values,
        y=country_counts.index,
        orientation='h',
        title="Top 15 Countries by Player Count",
        labels={'x': 'Number of Players', 'y': 'Country'},
        color=country_counts.values,
        color_continuous_scale='viridis'
    )
    fig.update_layout(height=500, showlegend=False)
    fig = apply_chart_styling(fig)
    return fig

def create_continent_pie_chart(df):
    """Create continent distribution pie chart."""
    continent_counts = df['continent_name'].value_counts()
    
    fig = px.pie(
        values=continent_counts.values,
        names=continent_counts.index,
        title="Player Distribution by Continent",
        color_discrete_sequence=['#238636', '#1f77b4', '#ff7f0e', '#d62728', '#9467bd', '#8c564b']
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig = apply_dark_theme_to_chart(fig)
    return fig

def create_age_distribution(df):
    """Create age distribution histogram."""
    valid_ages = df[(df['age'] > 10) & (df['age'] < 60)]['age']
    
    if len(valid_ages) > 0:
        fig = px.histogram(
            valid_ages,
            nbins=30,
            title="Age Distribution of Players",
            labels={'value': 'Age (years)', 'count': 'Number of Players'},
            color_discrete_sequence=['#238636']
        )
        fig.update_layout(showlegend=False)
        fig = apply_dark_theme_to_chart(fig)
        return fig
    return None

def create_batting_style_chart(df):
    """Create batting style distribution chart."""
    batting_counts = df['battingstyle'].value_counts()
    
    fig = px.bar(
        x=batting_counts.index,
        y=batting_counts.values,
        title="Batting Style Distribution",
        labels={'x': 'Batting Style', 'y': 'Number of Players'},
        color=batting_counts.values,
        color_continuous_scale='blues'
    )
    fig.update_layout(showlegend=False)
    return fig

def generate_synthetic_stats(player_data):
    """Generate synthetic gameplay statistics for demonstration."""
    np.random.seed(int(player_data['id']))  # Use player ID as seed for consistency
    
    position = player_data['position'].lower()
    batting_style = player_data['battingstyle'].lower()
    
    # Base stats depending on position
    if 'batsman' in position or 'allrounder' in position:
        matches = np.random.randint(50, 300)
        runs = np.random.randint(1000, 8000)
        batting_avg = runs / max(matches * 0.8, 1)  # Assuming 80% of matches batted
        strike_rate = np.random.uniform(70, 140)
        centuries = np.random.randint(0, max(1, int(runs/2000)))
        fifties = np.random.randint(centuries, max(centuries + 1, int(runs/800)))
    else:
        matches = np.random.randint(30, 200)
        runs = np.random.randint(100, 2000)
        batting_avg = runs / max(matches * 0.4, 1)
        strike_rate = np.random.uniform(60, 120)
        centuries = 0
        fifties = np.random.randint(0, 3)
    
    if 'bowler' in position or 'allrounder' in position:
        wickets = np.random.randint(20, 400)
        bowling_avg = np.random.uniform(15, 35)
        economy_rate = np.random.uniform(3.5, 6.5)
        five_wickets = np.random.randint(0, max(1, int(wickets/50)))
    else:
        wickets = np.random.randint(0, 20)
        bowling_avg = np.random.uniform(30, 50) if wickets > 0 else 0
        economy_rate = np.random.uniform(4, 8)
        five_wickets = 0
    
    if 'wicketkeeper' in position:
        catches = np.random.randint(max(1, matches//2), matches + 1)
        stumpings = np.random.randint(0, max(1, matches//10) + 1)
    else:
        catches = np.random.randint(0, max(1, matches//3) + 1)
        stumpings = 0
    
    # Generate batting stroke preferences based on batting style
    batting_strokes = {
        'Straight Drive': np.random.randint(15, 25),
        'Cover Drive': np.random.randint(10, 20),
        'Off Drive': np.random.randint(8, 18),
        'On Drive': np.random.randint(8, 18),
        'Pull': np.random.randint(5, 15),
        'Hook': np.random.randint(3, 12),
        'Cut': np.random.randint(8, 18),
        'Square Cut': np.random.randint(5, 15),
        'Late Cut': np.random.randint(3, 12),
        'Leg Glide': np.random.randint(8, 18),
        'Glance': np.random.randint(10, 20),
        'Sweep': np.random.randint(2, 10)
    }
    
    # Adjust stroke preferences based on batting style
    if 'left' in batting_style:
        # Left-handed batsmen might favor certain strokes
        batting_strokes['On Drive'] += 5
        batting_strokes['Leg Glide'] += 5
        batting_strokes['Pull'] += 3
    else:
        # Right-handed batsmen preferences
        batting_strokes['Cover Drive'] += 5
        batting_strokes['Off Drive'] += 3
        batting_strokes['Cut'] += 3
    
    # Aggressive players (based on strike rate) favor power shots
    if strike_rate > 120:
        batting_strokes['Pull'] += 8
        batting_strokes['Hook'] += 5
        batting_strokes['Cut'] += 5
    
    return {
        'matches': matches,
        'runs': runs,
        'batting_avg': round(batting_avg, 2),
        'strike_rate': round(strike_rate, 2),
        'centuries': centuries,
        'fifties': fifties,
        'wickets': wickets,
        'bowling_avg': round(bowling_avg, 2),
        'economy_rate': round(economy_rate, 2),
        'five_wickets': five_wickets,
        'catches': catches,
        'stumpings': stumpings,
        'batting_strokes': batting_strokes
    }

def create_batting_strokes_chart(player_data, stats):
    """Create batting strokes analysis chart similar to cricket field diagram."""
    
    strokes = stats['batting_strokes']
    stroke_names = list(strokes.keys())
    stroke_percentages = list(strokes.values())
    
    # Create a polar bar chart to simulate the cricket field diagram
    fig = go.Figure()
    
    # Calculate angles for each stroke (360 degrees divided by number of strokes)
    angles = np.linspace(0, 2*np.pi, len(stroke_names), endpoint=False)
    
    # Add the polar bar chart
    fig.add_trace(go.Barpolar(
        r=stroke_percentages,
        theta=np.degrees(angles),
        name='Batting Strokes',
        marker_color='rgb(34, 139, 34)',  # Forest green like cricket field
        marker_line_color='white',
        marker_line_width=2,
        opacity=0.8
    ))
    
    # Customize the layout to look like cricket field
    title_color = '#fafafa' if st.session_state.dark_theme else '#262730'
    bg_color = '#0e1117' if st.session_state.dark_theme else '#ffffff'
    
    fig.update_layout(
        title=dict(
            text=f"🏏 Batting Stroke Analysis - {player_data['fullname']}",
            font=dict(size=16, color=title_color, family="Arial Black")
        ),
        font=dict(size=12, color=title_color),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(stroke_percentages) * 1.1],
                ticksuffix='%',
                gridcolor='white',
                gridwidth=2,
                tickfont=dict(color='white', size=10, family="Arial Black")  # White text on dark green
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color='white', family="Arial Black"),  # White text on dark green
                rotation=90,  # Rotate to match cricket field orientation
                direction="clockwise"
            ),
            bgcolor='rgb(34, 139, 34)',  # Dark green background like cricket field
        ),
        showlegend=False,
        height=500,
        plot_bgcolor=bg_color,  # Theme-aware background
        paper_bgcolor=bg_color  # Theme-aware background
    )
    
    # Add text annotations for stroke names
    for i, (stroke, percentage) in enumerate(strokes.items()):
        angle_deg = np.degrees(angles[i])
        fig.add_annotation(
            x=0.5 + 0.35 * np.cos(angles[i]),
            y=0.5 + 0.35 * np.sin(angles[i]),
            text=f"<b>{stroke}</b><br>{percentage}%",
            showarrow=False,
            font=dict(size=10, color='white', family="Arial Black"),  # White text
            bgcolor='rgba(0,0,0,0.9)',  # Very dark background for high contrast
            bordercolor='white',
            borderwidth=2,
            xref="paper",
            yref="paper",
            borderpad=4
        )
    
    return fig

def create_stroke_preference_bar_chart(player_data, stats):
    """Create a horizontal bar chart for stroke preferences."""
    
    strokes = stats['batting_strokes']
    sorted_strokes = dict(sorted(strokes.items(), key=lambda x: x[1], reverse=True))
    
    fig = px.bar(
        x=list(sorted_strokes.values()),
        y=list(sorted_strokes.keys()),
        orientation='h',
        title=f"Favorite Batting Strokes - {player_data['fullname']}",
        labels={'x': 'Usage Percentage (%)', 'y': 'Batting Strokes'},
        color=list(sorted_strokes.values()),
        color_continuous_scale='Greens'
    )
    
    fig.update_layout(
        showlegend=False,
        height=400,
        title=dict(font=dict(size=16, color='#fafafa' if st.session_state.dark_theme else '#262730')),
        xaxis=dict(
            title=dict(font=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')), 
            tickfont=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')
        ),
        yaxis=dict(
            categoryorder='total ascending',
            title=dict(font=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')), 
            tickfont=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')
        ),
        plot_bgcolor='#0e1117' if st.session_state.dark_theme else 'white',
        paper_bgcolor='#0e1117' if st.session_state.dark_theme else 'white'
    )
    
    return fig

def create_player_performance_charts(player_data, stats):
    """Create interactive charts for player performance."""
    
    # Performance radar chart
    categories = ['Batting Avg', 'Strike Rate', 'Bowling Avg', 'Economy Rate', 'Catches']
    
    # Normalize values for radar chart (0-100 scale)
    batting_avg_norm = min(stats['batting_avg'] * 2, 100)
    strike_rate_norm = min(stats['strike_rate'] * 0.8, 100)
    bowling_avg_norm = max(100 - stats['bowling_avg'] * 2, 0)  # Lower is better
    economy_norm = max(100 - stats['economy_rate'] * 10, 0)  # Lower is better
    catches_norm = min(stats['catches'] * 2, 100)
    
    values = [batting_avg_norm, strike_rate_norm, bowling_avg_norm, economy_norm, catches_norm]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=player_data['fullname'],
        line_color='rgb(31, 119, 180)',
        fillcolor='rgba(31, 119, 180, 0.3)'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"Performance Radar - {player_data['fullname']}"
    )
    
    # Career progression chart (synthetic data)
    years = list(range(2015, 2025))
    np.random.seed(int(player_data['id']))
    
    if stats['runs'] > 500:  # Only for players with significant batting
        yearly_runs = []
        base_runs = stats['runs'] // len(years)
        for i, year in enumerate(years):
            variation = np.random.uniform(0.7, 1.3)
            career_progression = 1 + (i * 0.1) if i < 6 else 1.5 - ((i-6) * 0.1)
            runs_year = int(base_runs * variation * career_progression)
            yearly_runs.append(max(runs_year, 0))
        
        fig_progression = px.line(
            x=years,
            y=yearly_runs,
            title=f"Career Runs Progression - {player_data['fullname']}",
            labels={'x': 'Year', 'y': 'Runs Scored'},
            markers=True
        )
        fig_progression.update_traces(line_color='rgb(31, 119, 180)', line_width=3)
        
        return fig_radar, fig_progression
    
    return fig_radar, None

def display_player_details(player_data):
    """Display detailed information for a specific player."""
    
    st.markdown(f"""
    <div class="player-card">
        <h2>🏏 {player_data['fullname']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate synthetic stats for gameplay demonstration
    stats = generate_synthetic_stats(player_data)
    
    # Player basic info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📋 Basic Information")
        st.write(f"**Full Name:** {player_data['fullname']}")
        st.write(f"**First Name:** {player_data['firstname']}")
        st.write(f"**Last Name:** {player_data['lastname']}")
        st.write(f"**Gender:** {'Male' if player_data['gender'] == 'm' else 'Female'}")
    
    with col2:
        st.markdown("### 🌍 Location")
        st.write(f"**Country:** {player_data['country_name']}")
        st.write(f"**Continent:** {player_data['continent_name']}")
        
        st.markdown("### 📅 Age Information")
        st.write(f"**Date of Birth:** {player_data['dateofbirth']}")
        if player_data['age'] > 0:
            st.write(f"**Current Age:** {player_data['age']:.1f} years")
        else:
            st.write("**Current Age:** Not available")
    
    with col3:
        st.markdown("### 🏏 Playing Style")
        st.write(f"**Batting Style:** {player_data['battingstyle']}")
        st.write(f"**Bowling Style:** {player_data['bowlingstyle']}")
        st.write(f"**Position:** {player_data['position']}")
        
        st.markdown("### 🔗 Additional Info")
        st.write(f"**Player ID:** {player_data['id']}")
        if pd.notna(player_data['image_path']) and player_data['image_path']:
            st.write(f"**Image Available:** Yes")
        else:
            st.write(f"**Image Available:** No")
    
    # Career Statistics Section
    st.markdown("---")
    st.markdown("### 📊 Career Statistics")
    st.warning("⚠️ **Important:** All performance statistics shown below are synthetically generated for demonstration purposes only. These are not real player statistics.")
    st.markdown("*Note: These are synthetic statistics for demonstration purposes*")
    
    # Stats metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Matches Played", stats['matches'])
        st.metric("Total Runs", f"{stats['runs']:,}")
    
    with col2:
        st.metric("Batting Average", stats['batting_avg'])
        st.metric("Strike Rate", stats['strike_rate'])
    
    with col3:
        st.metric("Wickets Taken", stats['wickets'])
        st.metric("Bowling Average", stats['bowling_avg'] if stats['wickets'] > 0 else "N/A")
    
    with col4:
        st.metric("Catches", stats['catches'])
        if stats['stumpings'] > 0:
            st.metric("Stumpings", stats['stumpings'])
        else:
            st.metric("Economy Rate", stats['economy_rate'] if stats['wickets'] > 0 else "N/A")
    
    # Additional achievements
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏆 Batting Achievements")
        st.write(f"**Centuries:** {stats['centuries']}")
        st.write(f"**Fifties:** {stats['fifties']}")
        st.write(f"**Best Performance:** {stats['runs']//10} runs")
    
    with col2:
        st.markdown("#### 🎯 Bowling Achievements")
        st.write(f"**Five-wicket hauls:** {stats['five_wickets']}")
        st.write(f"**Best Bowling:** {stats['wickets']//10}-{np.random.randint(10, 50)}")
        st.write(f"**Economy Rate:** {stats['economy_rate']}")
    
    # Performance Charts
    st.markdown("---")
    st.markdown("### 📈 Performance Analysis")
    
    fig_radar, fig_progression = create_player_performance_charts(player_data, stats)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col2:
        if fig_progression:
            st.plotly_chart(fig_progression, use_container_width=True)
        else:
            st.info("Career progression chart not available for this player type.")
    
    # Batting Stroke Analysis
    st.markdown("---")
    st.markdown("### 🏏 Batting Stroke Analysis")
    st.markdown("*Analysis of most frequently played shots by the player*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Cricket field-style polar chart
        fig_strokes_polar = create_batting_strokes_chart(player_data, stats)
        st.plotly_chart(fig_strokes_polar, use_container_width=True)
    
    with col2:
        # Horizontal bar chart for stroke preferences
        fig_strokes_bar = create_stroke_preference_bar_chart(player_data, stats)
        st.plotly_chart(fig_strokes_bar, use_container_width=True)
    
    # Top 3 favorite strokes
    top_strokes = dict(sorted(stats['batting_strokes'].items(), key=lambda x: x[1], reverse=True)[:3])
    
    st.markdown("#### 🎯 Player's Signature Shots")
    cols = st.columns(3)
    
    for i, (stroke, percentage) in enumerate(top_strokes.items()):
        with cols[i]:
            st.metric(
                label=f"#{i+1} Favorite Shot",
                value=stroke,
                delta=f"{percentage}% usage"
            )
    
    # Comparison with similar players
    st.markdown("---")
    st.markdown("### 🔍 Player Comparison")
    
    # Create comparison chart with players from same country and position
    df = load_data()
    similar_players = df[
        (df['country_name'] == player_data['country_name']) & 
        (df['position'] == player_data['position']) &
        (df['fullname'] != player_data['fullname'])
    ].head(5)
    
    if not similar_players.empty:
        comparison_data = []
        comparison_data.append({
            'Player': player_data['fullname'],
            'Batting Avg': stats['batting_avg'],
            'Strike Rate': stats['strike_rate'],
            'Wickets': stats['wickets'],
            'Type': 'Selected Player'
        })
        
        for _, similar_player in similar_players.iterrows():
            similar_stats = generate_synthetic_stats(similar_player)
            comparison_data.append({
                'Player': similar_player['fullname'],
                'Batting Avg': similar_stats['batting_avg'],
                'Strike Rate': similar_stats['strike_rate'],
                'Wickets': similar_stats['wickets'],
                'Type': 'Similar Player'
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        
        fig_comparison = px.scatter(
            comparison_df,
            x='Batting Avg',
            y='Strike Rate',
            size='Wickets',
            color='Type',
            hover_name='Player',
            title=f"Comparison with Similar Players ({player_data['position']} from {player_data['country_name']})",
            color_discrete_map={'Selected Player': 'red', 'Similar Player': 'blue'}
        )
        
        st.plotly_chart(fig_comparison, use_container_width=True)
    else:
        st.info("No similar players found for comparison.")

def create_comparison_chart(df, selected_countries):
    """Create comparison chart for selected countries."""
    if len(selected_countries) < 2:
        return None
    
    country_data = df[df['country_name'].isin(selected_countries)]
    
    # Gender distribution by country
    gender_data = country_data.groupby(['country_name', 'gender']).size().unstack(fill_value=0)
    
    fig = px.bar(
        gender_data,
        title=f"Gender Distribution Comparison: {', '.join(selected_countries)}",
        labels={'value': 'Number of Players', 'index': 'Country'},
        color_discrete_map={'m': '#1f77b4', 'f': '#ff7f0e'}
    )
    
    return fig

def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">🏏 Cricket Players Stats Tool</h1>', unsafe_allow_html=True)
    
    # Data disclaimer
    st.info("📊 **Data Notice:** This application uses sample demonstration data for cricket players. Player statistics and performance metrics are synthetically generated for educational and demonstration purposes only. This is not real player data.")
    
    st.markdown("---")
    
    # Load data
    df = load_data()
    
    if df.empty:
        st.error("Could not load data. Please check if the data file exists.")
        return
    
    # Sidebar
    st.sidebar.markdown("## 🎛️ Navigation")
    
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Overview", "👤 Player Search", "📊 Analytics", "🔍 Country Comparison"]
    )
    
    # Sidebar disclaimer
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About This Data")
    st.sidebar.markdown("""
    **Demo Application:** This tool showcases cricket analytics capabilities using sample data.
    
    **Data Sources:**
    - Player names and basic info: Sample dataset
    - Performance statistics: Synthetically generated
    - Batting stroke analysis: Demonstration purposes
    
    **Purpose:** Educational demonstration of sports analytics dashboard capabilities.
    """)
    st.sidebar.markdown("---")
    
    if page == "🏠 Overview":
        st.markdown("## 📈 Dataset Overview")
        
        # Overview stats
        create_overview_stats(df)
        st.markdown("---")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = create_country_chart(df)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = create_continent_pie_chart(df)
            st.plotly_chart(fig2, use_container_width=True)
        
        # Additional charts
        col3, col4 = st.columns(2)
        
        with col3:
            fig3 = create_age_distribution(df)
            if fig3:
                st.plotly_chart(fig3, use_container_width=True)
        
        with col4:
            fig4 = create_batting_style_chart(df)
            st.plotly_chart(fig4, use_container_width=True)
    
    elif page == "👤 Player Search":
        st.markdown("## 🔍 Player Search & Details")
        
        # Search options
        search_type = st.radio("Search by:", ["Player Name", "Country", "Advanced Filters"])
        
        if search_type == "Player Name":
            # Search by player name
            search_term = st.text_input("🔍 Enter player name:", placeholder="e.g., Virat Kohli")
            
            if search_term:
                # Filter players
                filtered_df = df[df['fullname'].str.contains(search_term, case=False, na=False)]
                
                if not filtered_df.empty:
                    st.write(f"Found {len(filtered_df)} player(s)")
                    
                    # Select player
                    selected_player = st.selectbox(
                        "Select a player:",
                        filtered_df['fullname'].tolist()
                    )
                    
                    if selected_player:
                        player_data = filtered_df[filtered_df['fullname'] == selected_player].iloc[0]
                        display_player_details(player_data)
                else:
                    st.warning("No players found with that name.")
        
        elif search_type == "Country":
            # Search by country
            selected_country = st.selectbox(
                "🌍 Select a country:",
                sorted(df['country_name'].unique())
            )
            
            country_players = df[df['country_name'] == selected_country]
            st.write(f"Players from {selected_country}: {len(country_players)}")
            
            if not country_players.empty:
                # Show top players from country
                selected_player = st.selectbox(
                    "Select a player:",
                    country_players['fullname'].tolist()
                )
                
                if selected_player:
                    player_data = country_players[country_players['fullname'] == selected_player].iloc[0]
                    display_player_details(player_data)
        
        elif search_type == "Advanced Filters":
            st.markdown("### 🎯 Advanced Filters")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                filter_countries = st.multiselect(
                    "Countries:",
                    sorted(df['country_name'].unique())
                )
            
            with col2:
                filter_gender = st.selectbox(
                    "Gender:",
                    ["All", "Male", "Female"]
                )
            
            with col3:
                filter_batting = st.selectbox(
                    "Batting Style:",
                    ["All"] + sorted(df['battingstyle'].unique().tolist())
                )
            
            # Age range filter
            if df['age'].max() > 0:
                age_range = st.slider(
                    "Age Range:",
                    min_value=int(df[df['age'] > 0]['age'].min()),
                    max_value=int(df[df['age'] > 0]['age'].max()),
                    value=(20, 40)
                )
            
            # Apply filters
            filtered_df = df.copy()
            
            if filter_countries:
                filtered_df = filtered_df[filtered_df['country_name'].isin(filter_countries)]
            
            if filter_gender != "All":
                gender_code = 'm' if filter_gender == "Male" else 'f'
                filtered_df = filtered_df[filtered_df['gender'] == gender_code]
            
            if filter_batting != "All":
                filtered_df = filtered_df[filtered_df['battingstyle'] == filter_batting]
            
            if df['age'].max() > 0:
                filtered_df = filtered_df[
                    (filtered_df['age'] >= age_range[0]) & 
                    (filtered_df['age'] <= age_range[1])
                ]
            
            st.write(f"Found {len(filtered_df)} players matching your criteria")
            
            if not filtered_df.empty and len(filtered_df) <= 100:
                selected_player = st.selectbox(
                    "Select a player:",
                    filtered_df['fullname'].tolist()
                )
                
                if selected_player:
                    player_data = filtered_df[filtered_df['fullname'] == selected_player].iloc[0]
                    display_player_details(player_data)
            elif len(filtered_df) > 100:
                st.warning("Too many results. Please narrow down your filters.")
    
    elif page == "📊 Analytics":
        st.markdown("## 📊 Advanced Analytics")
        
        # Analytics options
        analysis_type = st.selectbox(
            "Select Analysis:",
            ["Country Analysis", "Age Analysis", "Playing Style Analysis", "Position Analysis", "Batting Stroke Analysis", "Gameplay Simulation", "Gender Analysis"]
        )
        
        if analysis_type == "Country Analysis":
            st.markdown("### 🌍 Country Analysis")
            
            # Top countries
            top_n = st.slider("Show top N countries:", 5, 20, 10)
            top_countries = df['country_name'].value_counts().head(top_n)
            
            fig = px.bar(
                x=top_countries.index,
                y=top_countries.values,
                title=f"Top {top_n} Countries by Player Count",
                labels={'x': 'Country', 'y': 'Number of Players'}
            )
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
            
            # Country details table
            st.markdown("### 📋 Country Statistics")
            country_stats = df.groupby('country_name').agg({
                'fullname': 'count',
                'age': lambda x: x[x > 0].mean() if len(x[x > 0]) > 0 else np.nan,
                'gender': lambda x: (x == 'f').sum() / len(x) * 100
            }).round(2)
            country_stats.columns = ['Total Players', 'Average Age', 'Female %']
            country_stats = country_stats.sort_values('Total Players', ascending=False)
            
            st.dataframe(country_stats.head(20), use_container_width=True)
        
        elif analysis_type == "Age Analysis":
            st.markdown("### 📅 Age Analysis")
            
            valid_ages = df[df['age'] > 10]
            
            if not valid_ages.empty:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Youngest Player", f"{valid_ages['age'].min():.1f} years")
                    st.metric("Average Age", f"{valid_ages['age'].mean():.1f} years")
                
                with col2:
                    st.metric("Oldest Player", f"{valid_ages['age'].max():.1f} years")
                    st.metric("Median Age", f"{valid_ages['age'].median():.1f} years")
                
                # Age distribution by continent
                fig = px.box(
                    valid_ages,
                    x='continent_name',
                    y='age',
                    title="Age Distribution by Continent"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Playing Style Analysis":
            st.markdown("### 🏏 Playing Style Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Batting style distribution
                batting_counts = df['battingstyle'].value_counts()
                fig1 = px.pie(
                    values=batting_counts.values,
                    names=batting_counts.index,
                    title="Batting Style Distribution"
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Bowling style distribution
                bowling_counts = df['bowlingstyle'].value_counts().head(10)
                fig2 = px.bar(
                    x=bowling_counts.values,
                    y=bowling_counts.index,
                    orientation='h',
                    title="Top 10 Bowling Styles"
                )
                st.plotly_chart(fig2, use_container_width=True)
        
        elif analysis_type == "Position Analysis":
            st.markdown("### 🏏 Position Analysis")
            
            # Position distribution
            position_counts = df['position'].value_counts()
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig1 = px.pie(
                    values=position_counts.values,
                    names=position_counts.index,
                    title="Player Position Distribution"
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Position by continent
                position_continent = pd.crosstab(df['continent_name'], df['position'])
                fig2 = px.bar(
                    position_continent,
                    title="Position Distribution by Continent",
                    labels={'value': 'Number of Players', 'index': 'Continent'}
                )
                st.plotly_chart(fig2, use_container_width=True)
            
            # Detailed position analysis
            st.markdown("### 📋 Position Statistics")
            position_stats = df.groupby('position').agg({
                'fullname': 'count',
                'age': lambda x: x[x > 0].mean() if len(x[x > 0]) > 0 else np.nan,
                'country_name': lambda x: x.nunique()
            }).round(2)
            position_stats.columns = ['Total Players', 'Average Age', 'Countries Represented']
            position_stats = position_stats.sort_values('Total Players', ascending=False)
            
            st.dataframe(position_stats, use_container_width=True)
        
        elif analysis_type == "Batting Stroke Analysis":
            st.markdown("### 🏏 Batting Stroke Analysis")
            st.markdown("*Analysis of preferred batting strokes across different player types*")
            
            # Sample analysis across different batting styles
            batting_styles = df['battingstyle'].value_counts().head(5).index.tolist()
            
            if len(batting_styles) > 0:
                selected_style = st.selectbox(
                    "Select batting style to analyze:",
                    batting_styles
                )
                
                # Get players with selected batting style
                style_players = df[df['battingstyle'] == selected_style].sample(min(10, len(df[df['battingstyle'] == selected_style])))
                
                # Generate stroke analysis data
                all_strokes = {
                    'Straight Drive': [], 'Cover Drive': [], 'Off Drive': [], 'On Drive': [],
                    'Pull': [], 'Hook': [], 'Cut': [], 'Square Cut': [], 'Late Cut': [],
                    'Leg Glide': [], 'Glance': [], 'Sweep': []
                }
                
                for _, player in style_players.iterrows():
                    player_stats = generate_synthetic_stats(player)
                    for stroke, percentage in player_stats['batting_strokes'].items():
                        all_strokes[stroke].append(percentage)
                
                # Calculate average stroke usage for this batting style
                avg_strokes = {stroke: np.mean(percentages) for stroke, percentages in all_strokes.items()}
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Polar chart for batting style average
                    fig_avg = go.Figure()
                    
                    stroke_names = list(avg_strokes.keys())
                    stroke_values = list(avg_strokes.values())
                    angles = np.linspace(0, 2*np.pi, len(stroke_names), endpoint=False)
                    
                    fig_avg.add_trace(go.Barpolar(
                        r=stroke_values,
                        theta=np.degrees(angles),
                        name=f'{selected_style} Strokes',
                        marker_color='rgb(34, 139, 34)',
                        marker_line_color='white',
                        marker_line_width=2,
                        opacity=0.8
                    ))
                    
                    fig_avg.update_layout(
                        title=dict(
                            text=f"Average Stroke Usage - {selected_style}",
                            font=dict(size=16, color='#fafafa' if st.session_state.dark_theme else '#262730')
                        ),
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, max(stroke_values) * 1.1],
                                ticksuffix='%',
                                tickfont=dict(color='white', size=10, family="Arial Black")  # White text on dark green
                            ),
                            angularaxis=dict(
                                tickfont=dict(size=10, color='white', family="Arial Black"),  # White text on dark green
                                rotation=90,
                                direction="clockwise"
                            ),
                            bgcolor='rgb(34, 139, 34)'  # Dark green background
                        ),
                        showlegend=False,
                        height=400,
                        plot_bgcolor='#0e1117' if st.session_state.dark_theme else 'white',
                        paper_bgcolor='#0e1117' if st.session_state.dark_theme else 'white'
                    )
                    
                    st.plotly_chart(fig_avg, use_container_width=True)
                
                with col2:
                    # Bar chart comparison
                    sorted_avg_strokes = dict(sorted(avg_strokes.items(), key=lambda x: x[1], reverse=True))
                    
                    fig_bar = px.bar(
                        x=list(sorted_avg_strokes.values()),
                        y=list(sorted_avg_strokes.keys()),
                        orientation='h',
                        title=f"Stroke Preferences - {selected_style}",
                        labels={'x': 'Average Usage (%)', 'y': 'Batting Strokes'},
                        color=list(sorted_avg_strokes.values()),
                        color_continuous_scale='Greens'
                    )
                    
                    fig_bar.update_layout(
                        showlegend=False,
                        height=400,
                        title=dict(font=dict(size=16, color='#fafafa' if st.session_state.dark_theme else '#262730')),
                        xaxis=dict(
                            title=dict(font=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')), 
                            tickfont=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')
                        ),
                        yaxis=dict(
                            categoryorder='total ascending',
                            title=dict(font=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')), 
                            tickfont=dict(color='#fafafa' if st.session_state.dark_theme else '#262730')
                        ),
                        plot_bgcolor='#0e1117' if st.session_state.dark_theme else 'white',
                        paper_bgcolor='#0e1117' if st.session_state.dark_theme else 'white'
                    )
                    
                    st.plotly_chart(fig_bar, use_container_width=True)
                
                # Stroke usage statistics table
                st.markdown("### 📊 Stroke Usage Statistics")
                
                stroke_stats_df = pd.DataFrame({
                    'Stroke': list(avg_strokes.keys()),
                    'Average Usage (%)': [round(val, 1) for val in avg_strokes.values()],
                    'Min Usage (%)': [round(min(all_strokes[stroke]), 1) for stroke in avg_strokes.keys()],
                    'Max Usage (%)': [round(max(all_strokes[stroke]), 1) for stroke in avg_strokes.keys()]
                })
                
                stroke_stats_df = stroke_stats_df.sort_values('Average Usage (%)', ascending=False)
                st.dataframe(stroke_stats_df, use_container_width=True)
                
                # Top signature shots for this batting style
                top_3_strokes = list(sorted_avg_strokes.keys())[:3]
                
                st.markdown(f"### 🎯 Signature Shots for {selected_style}")
                cols = st.columns(3)
                
                for i, stroke in enumerate(top_3_strokes):
                    with cols[i]:
                        st.metric(
                            label=f"#{i+1} Most Used",
                            value=stroke,
                            delta=f"{sorted_avg_strokes[stroke]:.1f}% avg usage"
                        )
            
            else:
                st.info("No batting style data available for analysis.")
        
        elif analysis_type == "Gameplay Simulation":
            st.markdown("### 🎮 Gameplay Simulation & Performance Analysis")
            st.info("📊 **Demo Feature:** This section demonstrates sports analytics capabilities using synthetically generated performance data for educational purposes.")
            st.markdown("*This section uses synthetic data to demonstrate gameplay analytics*")
            
            # Select a random sample of players for simulation
            sample_size = st.slider("Number of players to simulate:", 5, 50, 20)
            sample_players = df.sample(n=min(sample_size, len(df)))
            
            # Generate performance data for sample
            performance_data = []
            for _, player in sample_players.iterrows():
                stats = generate_synthetic_stats(player)
                performance_data.append({
                    'Player': player['fullname'],
                    'Country': player['country_name'],
                    'Position': player['position'],
                    'Matches': stats['matches'],
                    'Runs': stats['runs'],
                    'Batting_Avg': stats['batting_avg'],
                    'Strike_Rate': stats['strike_rate'],
                    'Wickets': stats['wickets'],
                    'Bowling_Avg': stats['bowling_avg'],
                    'Economy_Rate': stats['economy_rate'],
                    'Catches': stats['catches']
                })
            
            performance_df = pd.DataFrame(performance_data)
            
            # Performance analysis charts
            col1, col2 = st.columns(2)
            
            with col1:
                # Batting performance scatter
                fig1 = px.scatter(
                    performance_df,
                    x='Batting_Avg',
                    y='Strike_Rate',
                    size='Runs',
                    color='Position',
                    hover_name='Player',
                    title="Batting Performance Analysis",
                    labels={'Batting_Avg': 'Batting Average', 'Strike_Rate': 'Strike Rate'}
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Bowling performance scatter
                bowling_players = performance_df[performance_df['Wickets'] > 0]
                if not bowling_players.empty:
                    fig2 = px.scatter(
                        bowling_players,
                        x='Bowling_Avg',
                        y='Economy_Rate',
                        size='Wickets',
                        color='Position',
                        hover_name='Player',
                        title="Bowling Performance Analysis",
                        labels={'Bowling_Avg': 'Bowling Average', 'Economy_Rate': 'Economy Rate'}
                    )
                    st.plotly_chart(fig2, use_container_width=True)
                else:
                    st.info("No bowling data available for selected players")
            
            # Performance leaderboards
            st.markdown("### 🏆 Performance Leaderboards")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("#### Top Batsmen (by Runs)")
                top_batsmen = performance_df.nlargest(5, 'Runs')[['Player', 'Runs', 'Batting_Avg']]
                st.dataframe(top_batsmen, use_container_width=True)
            
            with col2:
                st.markdown("#### Top Bowlers (by Wickets)")
                top_bowlers = performance_df.nlargest(5, 'Wickets')[['Player', 'Wickets', 'Bowling_Avg']]
                st.dataframe(top_bowlers, use_container_width=True)
            
            with col3:
                st.markdown("#### Most Experienced")
                top_experienced = performance_df.nlargest(5, 'Matches')[['Player', 'Matches', 'Position']]
                st.dataframe(top_experienced, use_container_width=True)
            
            # Team formation simulator
            st.markdown("---")
            st.markdown("### 🏏 Dream Team Simulator")
            
            if st.button("Generate Random Dream Team"):
                # Select balanced team
                batsmen = performance_df[performance_df['Position'].str.contains('Batsman', na=False)].nlargest(4, 'Batting_Avg')
                bowlers = performance_df[performance_df['Position'].str.contains('Bowler', na=False)].nlargest(4, 'Wickets')
                allrounders = performance_df[performance_df['Position'].str.contains('Allrounder', na=False)].nlargest(2, 'Runs')
                wicketkeeper = performance_df[performance_df['Position'].str.contains('Wicketkeeper', na=False)].nlargest(1, 'Catches')
                
                dream_team = pd.concat([batsmen, bowlers, allrounders, wicketkeeper]).head(11)
                
                if not dream_team.empty:
                    st.markdown("#### 🌟 Your Dream Team")
                    team_display = dream_team[['Player', 'Country', 'Position', 'Runs', 'Wickets']].reset_index(drop=True)
                    team_display.index = team_display.index + 1
                    st.dataframe(team_display, use_container_width=True)
                    
                    # Team stats
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Team Runs", f"{dream_team['Runs'].sum():,}")
                    with col2:
                        st.metric("Total Team Wickets", f"{dream_team['Wickets'].sum()}")
                    with col3:
                        st.metric("Countries Represented", f"{dream_team['Country'].nunique()}")
        
        elif analysis_type == "Gender Analysis":
            st.markdown("### ⚧ Gender Analysis")
            
            gender_counts = df['gender'].value_counts()
            total_players = len(df)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                male_count = gender_counts.get('m', 0)
                st.metric("Male Players", f"{male_count:,}")
                st.metric("Male %", f"{male_count/total_players*100:.1f}%")
            
            with col2:
                female_count = gender_counts.get('f', 0)
                st.metric("Female Players", f"{female_count:,}")
                st.metric("Female %", f"{female_count/total_players*100:.1f}%")
            
            with col3:
                st.metric("Total Players", f"{total_players:,}")
                ratio = male_count / female_count if female_count > 0 else 0
                st.metric("Male:Female Ratio", f"{ratio:.1f}:1")
            
            # Gender by continent
            gender_continent = pd.crosstab(df['continent_name'], df['gender'])
            gender_continent_pct = gender_continent.div(gender_continent.sum(axis=1), axis=0) * 100
            
            fig = px.bar(
                gender_continent_pct,
                title="Gender Distribution by Continent (%)",
                labels={'value': 'Percentage', 'index': 'Continent'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif page == "🔍 Country Comparison":
        st.markdown("## 🔍 Country Comparison")
        
        # Select countries to compare
        countries_to_compare = st.multiselect(
            "Select countries to compare:",
            sorted(df['country_name'].unique()),
            default=['India', 'England', 'Australia'][:min(3, df['country_name'].nunique())]
        )
        
        if len(countries_to_compare) >= 2:
            comparison_data = df[df['country_name'].isin(countries_to_compare)]
            
            # Summary stats
            st.markdown("### 📊 Comparison Summary")
            summary_stats = comparison_data.groupby('country_name').agg({
                'fullname': 'count',
                'age': lambda x: x[x > 0].mean() if len(x[x > 0]) > 0 else np.nan,
                'gender': lambda x: (x == 'f').sum(),
                'battingstyle': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown'
            }).round(2)
            summary_stats.columns = ['Total Players', 'Average Age', 'Female Players', 'Most Common Batting Style']
            
            st.dataframe(summary_stats, use_container_width=True)
            
            # Comparison charts
            col1, col2 = st.columns(2)
            
            with col1:
                # Player count comparison
                player_counts = comparison_data['country_name'].value_counts()
                fig1 = px.bar(
                    x=player_counts.index,
                    y=player_counts.values,
                    title="Player Count Comparison",
                    labels={'x': 'Country', 'y': 'Number of Players'}
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Gender comparison
                fig2 = create_comparison_chart(df, countries_to_compare)
                if fig2:
                    st.plotly_chart(fig2, use_container_width=True)
        
        else:
            st.info("Please select at least 2 countries to compare.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666;'>🏏 Cricket Players Stats Tool | "
        f"Data contains {len(df):,} players from {df['country_name'].nunique()} countries</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
