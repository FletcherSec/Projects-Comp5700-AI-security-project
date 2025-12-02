"""
Task 1: Extract pull request data and create CSV
"""

from datasets import load_dataset
import pandas as pd
import os

def main():
    print("Loading dataset...")
    dataset = load_dataset("hao-li/AIDev")
    
    print("Extracting pull request data...")
    pr_data = dataset['train']
    
    # Create DataFrame with required columns
    df_task1 = pd.DataFrame({
        'TITLE': pr_data['title'],
        'ID': pr_data['id'],
        'AGENTNAME': pr_data['agent'],
        'BODYSTRING': pr_data['body'],
        'REPOID': pr_data['repo_id'],
        'REPOURL': pr_data['repo_url']
    })
    
    # Create outputs directory if it doesn't exist
    os.makedirs('../outputs', exist_ok=True)
    
    # Save to CSV
    output_path = '../outputs/task1_pull_requests.csv'
    df_task1.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Task 1 completed!")
    print(f"Total rows: {len(df_task1)}")
    print(f"Output saved to: {output_path}")
    print(f"\nFirst few rows:")
    print(df_task1.head())

if __name__ == "__main__":
    main()
