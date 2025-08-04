import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('data/all_players.csv')

print("=== PLAYER DATA ANALYSIS ===")
print(f"Total players in dataset: {len(df):,}")
print(f"Total countries represented: {df['country_name'].nunique()}")
print(f"Date range: {df['dateofbirth'].min()} to {df['dateofbirth'].max()}")

print("\n=== TOP 10 COUNTRIES BY PLAYER COUNT ===")
country_counts = df['country_name'].value_counts().head(10)
print(country_counts)

print("\n=== GENDER DISTRIBUTION ===")
gender_dist = df['gender'].value_counts()
print(gender_dist)
print(f"Percentage female players: {(gender_dist.get('f', 0) / len(df) * 100):.1f}%")

print("\n=== BATTING STYLES DISTRIBUTION ===")
batting_styles = df['battingstyle'].value_counts()
print(batting_styles)

print("\n=== BOWLING STYLES DISTRIBUTION ===")
bowling_styles = df['bowlingstyle'].value_counts()
print(bowling_styles)

print("\n=== PLAYERS BY CONTINENT ===")
continent_counts = df['continent_name'].value_counts()
print(continent_counts)

print("\n=== SAMPLE PLAYERS FROM TOP COUNTRIES ===")
top_5_countries = country_counts.head(5).index.tolist()
for country in top_5_countries:
    sample_players = df[df['country_name'] == country]['fullname'].head(3).tolist()
    print(f"{country}: {', '.join(sample_players)}")

print("\n=== ANALYSIS COMPLETE ===")
print("Note: This dataset contains player profile information.")
print("Performance statistics (runs, wickets) are not available in this dataset.")
