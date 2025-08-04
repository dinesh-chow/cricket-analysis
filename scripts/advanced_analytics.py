import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os

# Configure matplotlib
import matplotlib
matplotlib.use('Agg')

def advanced_analytics():
    """Perform advanced analytics on the cricket players dataset."""
    
    df = pd.read_csv('data/cleaned_all_players.csv')
    os.makedirs('visualizations/advanced', exist_ok=True)
    
    print("=== ADVANCED ANALYTICS ===")
    
    # 1. Age Analysis (if birth dates are valid)
    try:
        # Clean date format and calculate ages
        df['dateofbirth_clean'] = pd.to_datetime(df['dateofbirth'], format='%d-%m-%Y', errors='coerce')
        current_date = datetime.now()
        df['age'] = (current_date - df['dateofbirth_clean']).dt.days / 365.25
        
        # Filter reasonable ages (10-50 years)
        valid_ages = df[(df['age'] >= 10) & (df['age'] <= 50)]['age']
        
        if len(valid_ages) > 0:
            plt.figure(figsize=(12, 6))
            plt.hist(valid_ages, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
            plt.title('Age Distribution of Cricket Players', fontsize=14)
            plt.xlabel('Age (years)')
            plt.ylabel('Number of Players')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('visualizations/advanced/age_distribution.png', dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Age analysis: Mean age = {valid_ages.mean():.1f} years")
            print("Saved: visualizations/advanced/age_distribution.png")
    except Exception as e:
        print(f"Age analysis skipped: {e}")
    
    # 2. Continent vs Gender Analysis
    plt.figure(figsize=(12, 8))
    continent_gender = pd.crosstab(df['continent_name'], df['gender'])
    continent_gender.plot(kind='bar', stacked=True, color=['lightcoral', 'lightblue'])
    plt.title('Player Distribution by Continent and Gender', fontsize=14)
    plt.xlabel('Continent')
    plt.ylabel('Number of Players')
    plt.legend(['Female', 'Male'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('visualizations/advanced/continent_gender_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: visualizations/advanced/continent_gender_analysis.png")
    
    # 3. Top Countries Detailed Analysis
    top_10_countries = df['country_name'].value_counts().head(10)
    
    plt.figure(figsize=(14, 8))
    colors = plt.cm.Set3(np.linspace(0, 1, len(top_10_countries)))
    bars = plt.bar(range(len(top_10_countries)), top_10_countries.values, color=colors)
    plt.title('Top 10 Countries by Player Count (Detailed)', fontsize=16)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Number of Players', fontsize=12)
    plt.xticks(range(len(top_10_countries)), top_10_countries.index, rotation=45, ha='right')
    
    # Add value labels on bars
    for bar, value in zip(bars, top_10_countries.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, 
                str(value), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('visualizations/advanced/top_countries_detailed.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: visualizations/advanced/top_countries_detailed.png")
    
    # 4. Batting vs Bowling Style Matrix
    style_matrix = pd.crosstab(df['battingstyle'].fillna('Unknown'), 
                              df['bowlingstyle'].fillna('Unknown'), 
                              margins=True)
    
    print("\n=== BATTING vs BOWLING STYLE MATRIX ===")
    print(style_matrix)
    
    # 5. Country Diversity Index
    print(f"\n=== DIVERSITY METRICS ===")
    total_players = len(df)
    country_diversity = 1 - sum((df['country_name'].value_counts() / total_players) ** 2)
    print(f"Country Diversity Index: {country_diversity:.3f} (0=no diversity, 1=max diversity)")
    
    # 6. Data Completeness Analysis
    print(f"\n=== DATA COMPLETENESS ===")
    completeness = (df.notna().sum() / len(df) * 100).round(1)
    for col, pct in completeness.items():
        if pct > 90:
            status = "GOOD"
        elif pct > 50:
            status = "OK"
        else:
            status = "POOR"
        print(f"{col}: {pct}% ({status})")
    
    print("\n=== ADVANCED ANALYTICS COMPLETE ===")

if __name__ == "__main__":
    advanced_analytics()
