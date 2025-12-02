from datasets import load_dataset
import pandas as pd
import os

def main():
    print("Loading dataset...")
    dataset = load_dataset("hao-li/AIDev")
    
    print("Extracting PR task type data...")
    pr_data = dataset['train']
    
    # Check available columns
    print(f"Available columns: {pr_data.column_names}")
    
    # Build the dataframe with columns that exist
    data_dict = {
        'PRID': pr_data['id'],
        'PRTITLE': pr_data['title'],
    }
    
    # Add optional columns if they exist
    if 'reason' in pr_data.column_names:
        data_dict['PRREASON'] = pr_data['reason']
    else:
        data_dict['PRREASON'] = [None] * len(pr_data)
    
    if 'type' in pr_data.column_names:
        data_dict['PRTYPE'] = pr_data['type']
    else:
        data_dict['PRTYPE'] = [None] * len(pr_data)
    
    if 'confidence' in pr_data.column_names:
        data_dict['CONFIDENCE'] = pr_data['confidence']
    else:
        data_dict['CONFIDENCE'] = [None] * len(pr_data)
    
    # Create DataFrame with required columns
    df_task3 = pd.DataFrame(data_dict)
    
    # Create outputs directory if it doesn't exist
    os.makedirs('../outputs', exist_ok=True)
    
    # Save to CSV
    output_path = '../outputs/task3_task_types.csv'
    df_task3.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Task 3 completed!")
    print(f"Total rows: {len(df_task3)}")
    print(f"Output saved to: {output_path}")
    print(f"\nFirst few rows:")
    print(df_task3.head())

if __name__ == "__main__":
    main()
