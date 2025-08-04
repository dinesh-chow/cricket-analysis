# Cricket Players Analysis Configuration

# Data Settings
DATA_PATH = "data/all_players.csv"
CLEANED_DATA_PATH = "data/cleaned_all_players.csv"
OUTPUT_DIR = "visualizations"
REPORTS_DIR = "reports"

# Analysis Settings
TOP_N_COUNTRIES = 10
MIN_AGE = 10
MAX_AGE = 50

# Visualization Settings
FIGURE_SIZE_LARGE = (12, 8)
FIGURE_SIZE_MEDIUM = (10, 6)
FIGURE_SIZE_SMALL = (8, 6)
DPI = 300
COLOR_PALETTE = ['dodgerblue', 'green', 'red', 'orange', 'purple']

# Report Settings
REPORT_TITLE = "Cricket Players Data Analysis Report"
INCLUDE_SAMPLE_PLAYERS = True
MAX_SAMPLE_PLAYERS = 5

# Data Quality Thresholds
MIN_COMPLETENESS_GOOD = 90  # %
MIN_COMPLETENESS_OK = 50    # %
