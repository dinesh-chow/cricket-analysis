import pandas as pd
import matplotlib.pyplot as plt
import os

# Configure matplotlib to use non-interactive backend to avoid warnings
import matplotlib
matplotlib.use('Agg')

def load_and_analyze_data():
    """Load data and perform analysis to get required variables."""
    # Load your data into a DataFrame
    df = pd.read_csv('data/all_players.csv')
    
    # Since the actual CSV doesn't have ODI stats, we'll analyze what we have
    # Country-wise player distribution
    player_counts = df['country_name'].value_counts().head(10)  # Top 10 countries
    
    # Get batting style data if available
    batting_styles = df['battingstyle'].dropna().value_counts() if 'battingstyle' in df.columns else pd.Series()
    
    # Get gender distribution if available
    gender_dist = df['gender'].value_counts() if 'gender' in df.columns else pd.Series()
    
    return player_counts, batting_styles, gender_dist

def create_visualizations():
    """Create and save visualizations."""
    # Ensure visualizations directory exists
    os.makedirs('visualizations', exist_ok=True)
    
    # Load data
    player_counts, batting_styles, gender_dist = load_and_analyze_data()
    
    # Players per country (bar chart)
    if not player_counts.empty:
        plt.figure(figsize=(12, 6))
        player_counts.plot(kind='bar', color='dodgerblue')
        plt.title('Number of Players Per Country (Top 10)', fontsize=14)
        plt.ylabel('Player Count', fontsize=12)
        plt.xlabel('Country', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('visualizations/players_per_country.png', dpi=300, bbox_inches='tight')
        plt.close()  # Close figure to free memory and avoid warnings
        print("Saved: visualizations/players_per_country.png")
    else:
        print("No country data available to visualize")
    
    # Batting style distribution if available
    if not batting_styles.empty:
        plt.figure(figsize=(10, 6))
        batting_styles.plot(kind='bar', color='green')
        plt.title('Distribution of Batting Styles', fontsize=14)
        plt.ylabel('Number of Players', fontsize=12)
        plt.xlabel('Batting Style', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('visualizations/batting_styles.png', dpi=300, bbox_inches='tight')
        plt.close()  # Close figure to free memory and avoid warnings
        print("Saved: visualizations/batting_styles.png")
    else:
        print("No batting style data available to visualize")
    
    # Gender distribution if available
    if not gender_dist.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(gender_dist.values, labels=gender_dist.index, autopct='%1.1f%%', startangle=90)
        plt.title('Gender Distribution of Players', fontsize=14)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.tight_layout()
        plt.savefig('visualizations/gender_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()  # Close figure to free memory and avoid warnings
        print("Saved: visualizations/gender_distribution.png")
    else:
        print("No gender data available to visualize")

if __name__ == "__main__":
    create_visualizations()
    print("Visualization generation completed!")
