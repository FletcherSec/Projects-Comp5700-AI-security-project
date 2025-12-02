from datasets import load_dataset
import pandas as pd
import os

def main():
    print("Loading dataset...")
    dataset = load_dataset("hao-li/AIDev")
    
    print("Extracting repository data...")
    pr_data = dataset['train']
    
    # Since repository data is embedded in the PR data, we need to extract unique repositories
    # Create a dictionary to store unique repositories by repo_id
    repos_dict = {}
    
    for i in range(len(pr_data)):
        repo_id = pr_data[i]['repo_id']
        
        # Only add if we haven't seen this repo_id before
        if repo_id not in repos_dict:
            repos_dict[repo_id] = {
                'REPOID': pr_data[i]['repo_id'],
                'LANG': pr_data[i].get('language', None),
                'STARS': pr_data[i].get('stars', None),
                'REPOURL': pr_data[i]['repo_url']
            }
    
    # Convert dictionary to DataFrame
    df_task2 = pd.DataFrame(list(repos_dict.values()))
    
    # Create outputs directory if it doesn't exist
    os.makedirs('../outputs', exist_ok=True)
    
    # Save to CSV
    output_path = '../outputs/task2_repositories.csv'
    df_task2.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Task 2 completed!")
    print(f"Total unique repositories: {len(df_task2)}")
    print(f"Output saved to: {output_path}")
    print(f"\nFirst few rows:")
    print(df_task2.head())

if __name__ == "__main__":
    main()
