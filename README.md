# 🏏 Cricket Players Data Analysis Project

A comprehensive data analysis project for exploring cricket player demographics, statistics, and trends across different countries and continents.

## ⚠️ **Important Data Disclaimer**

**This is a demonstration project using sample data for educational purposes:**

- **Player Data:** Sample dataset with basic player information (names, countries, batting/bowling styles)
- **Performance Statistics:** All career statistics, batting averages, strike rates, and performance metrics are **synthetically generated**
- **Batting Stroke Analysis:** Demonstration feature using simulated data
- **Purpose:** Showcase sports analytics dashboard capabilities and data visualization techniques

**This application does not contain real cricket player statistics or performance data.**

## 📊 Project Overview

This project analyzes a dataset of **17,385 cricket players** from **90 countries** across **6 continents**, providing insights into player demographics, batting/bowling styles, and geographic distribution.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation
```bash
# Clone or download the project
cd players

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install pandas matplotlib seaborn numpy
```

### Run Analysis
```bash
# Run complete pipeline
python run_analysis.py

# Or run individual scripts
python scripts/clean_data.py
python scripts/analysis.py
python scripts/visualization.py
python scripts/advanced_analytics.py
python scripts/generate_report.py
```

## 📁 Project Structure

```
players/
├── data/
│   ├── all_players.csv              # Original dataset
│   └── cleaned_all_players.csv      # Cleaned dataset
├── scripts/
│   ├── clean_data.py               # Data cleaning & preprocessing
│   ├── load_data.py                # Data loading utilities
│   ├── analysis.py                 # Statistical analysis
│   ├── visualization.py            # Basic visualizations
│   ├── advanced_analytics.py       # Advanced analytics & charts
│   └── generate_report.py          # Report generation
├── visualizations/
│   ├── *.png                       # Basic charts
│   └── advanced/                   # Advanced visualizations
├── reports/
│   └── summary_report.md           # Generated analysis report
├── config.py                       # Configuration settings
├── run_analysis.py                 # Main pipeline runner
└── README.md                       # This file
```

## 📈 Analysis Features

### Basic Analytics
- Player count by country and continent
- Gender distribution analysis
- Batting and bowling style breakdowns
- Data quality assessment

### Advanced Analytics
- Age distribution analysis
- Cross-continental gender patterns
- Batting vs bowling style correlation matrix
- Data completeness scoring
- Diversity index calculations

### Visualizations
- **Basic Charts**: Country distribution, gender pie chart, batting styles
- **Advanced Charts**: Age histograms, continent-gender analysis, detailed country rankings

## 📊 Key Insights

### Top Countries by Player Count
1. **India**: 3,179 players (18.3%)
2. **Germany**: 1,040 players (6.0%)
3. **England**: 965 players (5.6%)
4. **Italy**: 936 players (5.4%)
5. **Pakistan**: 808 players (4.6%)

### Demographics
- **Gender Split**: 93.6% Male, 6.4% Female
- **Average Age**: 29.4 years
- **Batting Styles**: 82.7% Right-handed, 17.3% Left-handed
- **Continental Distribution**: Europe (47.6%), Asia (39.9%), Oceania (7.2%)

### Data Quality
- **High Quality Fields**: Player names, countries, demographics (100% complete)
- **Medium Quality**: Batting styles (57.8% complete)
- **Low Quality**: Bowling styles (45.3% complete)

## 🛠️ Technical Details

### Dependencies
- **pandas**: Data manipulation and analysis
- **matplotlib**: Basic plotting and visualization
- **seaborn**: Statistical data visualization
- **numpy**: Numerical computations

### Data Processing Pipeline
1. **Cleaning**: Remove duplicates, standardize formats
2. **Analysis**: Statistical computations and insights
3. **Visualization**: Chart generation
4. **Reporting**: Automated report creation

## 📝 Output Files

### Generated Reports
- `reports/summary_report.md` - Comprehensive analysis summary
- Console output with detailed statistics

### Visualizations
- `visualizations/players_per_country.png` - Top 10 countries bar chart
- `visualizations/batting_styles.png` - Batting style distribution
- `visualizations/gender_distribution.png` - Gender pie chart
- `visualizations/advanced/age_distribution.png` - Age histogram
- `visualizations/advanced/continent_gender_analysis.png` - Cross-continental analysis
- `visualizations/advanced/top_countries_detailed.png` - Detailed country rankings

## 🔧 Configuration

Edit `config.py` to customize:
- File paths and directories
- Chart styling and colors
- Analysis parameters
- Report settings

## 🚀 Future Enhancements

### Potential Improvements
- Interactive dashboard (Streamlit/Dash)
- Performance statistics integration
- Machine learning predictions
- Geographic heat maps
- API integration for live data
- Advanced statistical modeling

### Data Expansion
- Match performance data
- Career progression tracking
- Team affiliations
- Tournament participation

## 📞 Support

For questions or issues:
1. Check the generated reports for analysis details
2. Review console output for any error messages
3. Ensure all dependencies are properly installed
4. Verify data file paths in configuration

## 📜 License

This project is for educational and analysis purposes. Data usage should comply with relevant terms and conditions.

---

**Generated by Cricket Players Analysis System**  
*Last Updated: August 2025*
