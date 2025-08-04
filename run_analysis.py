"""
Cricket Players Data Analysis - Main Runner
Executes the complete analysis pipeline
"""

import os
import sys
import time
from datetime import datetime

def run_script(script_name, description):
    """Run a Python script and handle errors."""
    print(f"\n{'='*50}")
    print(f"🏏 {description}")
    print(f"{'='*50}")
    
    start_time = time.time()
    
    try:
        # Run script using subprocess to avoid import issues
        import subprocess
        result = subprocess.run([sys.executable, f"scripts/{script_name}.py"], 
                              capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            if result.stdout:
                print(result.stdout)
        else:
            print(f"Error output: {result.stderr}")
            raise Exception(f"Script failed with return code {result.returncode}")
        
        end_time = time.time()
        print(f"\n✅ Completed in {end_time - start_time:.2f} seconds")
        return True
        
    except Exception as e:
        print(f"\n❌ Error in {script_name}: {str(e)}")
        return False

def main():
    """Run the complete cricket players analysis pipeline."""
    
    print(f"""
🏏 CRICKET PLAYERS DATA ANALYSIS PIPELINE
==========================================
Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
==========================================
    """)
    
    # Pipeline steps
    pipeline_steps = [
        ("clean_data", "Data Cleaning & Preprocessing"),
        ("analysis", "Statistical Analysis"),
        ("visualization", "Basic Visualizations"),
        ("advanced_analytics", "Advanced Analytics"),
        ("generate_report", "Report Generation")
    ]
    
    success_count = 0
    total_steps = len(pipeline_steps)
    
    for script_name, description in pipeline_steps:
        success = run_script(script_name, description)
        if success:
            success_count += 1
        else:
            print(f"\n⚠️ Pipeline stopped due to error in {script_name}")
            break
    
    # Final summary
    print(f"\n{'='*60}")
    print(f"🏆 PIPELINE SUMMARY")
    print(f"{'='*60}")
    print(f"✅ Completed: {success_count}/{total_steps} steps")
    print(f"⏱️ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if success_count == total_steps:
        print(f"""
🎉 ALL STEPS COMPLETED SUCCESSFULLY!

📁 Generated Files:
   📊 Visualizations: visualizations/*.png
   📈 Advanced Charts: visualizations/advanced/*.png  
   📄 Report: reports/summary_report.md
   🔧 Cleaned Data: data/cleaned_all_players.csv

🚀 Your cricket players analysis is complete!
        """)
    else:
        print(f"\n⚠️ Pipeline completed with {total_steps - success_count} errors")
    
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
