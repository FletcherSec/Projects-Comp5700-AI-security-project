from datasets import load_dataset
import pandas as pd
import os
import re

def clean_patch(patch_text):
    """
    Remove special characters from patch/diff to avoid string encoding errors.
    Keeps only printable ASCII characters, newlines, tabs, and carriage returns.
    """
    if pd.isna(patch_text) or patch_text is None:
        return ""
    
    # Convert to string
    patch_str = str(patch_text)
    
    # Remove non-ASCII and control characters except \n, \r, \t
    # Keep characters in range 0x20-0x7E (printable ASCII) plus newline, tab, carriage return
    cleaned = re.sub(r'[^\x20-\x7E\n\r\t]', '', patch_str)
    
    # Remove any remaining problematic characters
    cleaned = cleaned.replace('\x00', '')  # Remove null bytes
    
    return cleaned

def main():
    print("Loading dataset...")
    dataset = load_dataset("hao-li/AIDev")
    
    print("Extracting PR commit details...")
    pr_data = dataset['train']
    
    # Check what columns are available
    print(f"Available columns: {pr_data.column_names}")
    
    # Build the dataframe with columns that exist
    data_dict = {
        'PRID': pr_data['id'],
    }
    
    # Add columns if they exist, otherwise use None
    if 'sha' in pr_data.column_names:
        data_dict['PRSHA'] = pr_data['sha']
    else:
        data_dict['PRSHA'] = [None] * len(pr_data)
    
    if 'message' in pr_data.column_names:
        data_dict['PRCOMMITMESSAGE'] = pr_data['message']
    else:
        data_dict['PRCOMMITMESSAGE'] = [None] * len(pr_data)
    
    if 'filename' in pr_data.column_names:
        data_dict['PRFILE'] = pr_data['filename']
    elif 'files' in pr_data.column_names:
        data_dict['PRFILE'] = pr_data['files']
    else:
        data_dict['PRFILE'] = [None] * len(pr_data)
    
    if 'status' in pr_data.column_names:
        data_dict['PRSTATUS'] = pr_data['status']
    else:
        data_dict['PRSTATUS'] = [None] * len(pr_data)
    
    if 'additions' in pr_data.column_names:
        data_dict['PRADDS'] = pr_data['additions']
    else:
        data_dict['PRADDS'] = [0] * len(pr_data)
    
    if 'deletions' in pr_data.column_names:
        data_dict['PRDELSS'] = pr_data['deletions']
    else:
        data_dict['PRDELSS'] = [0] * len(pr_data)
    
    if 'changes' in pr_data.column_names:
        data_dict['PRCHANGECOUNT'] = pr_data['changes']
    else:
        # Calculate from additions + deletions if available
        data_dict['PRCHANGECOUNT'] = [0] * len(pr_data)
    
    # Handle patch/diff
    if 'patch' in pr_data.column_names:
        data_dict['PRDIFF'] = [clean_patch(p) for p in pr_data['patch']]
    elif 'diff' in pr_data.column_names:
        data_dict['PRDIFF'] = [clean_patch(d) for d in pr_data['diff']]
    else:
        data_dict['PRDIFF'] = [''] * len(pr_data)
    
    # Create DataFrame
    df_task4 = pd.DataFrame(data_dict)
    
    # Create outputs directory if it doesn't exist
    os.makedirs('../outputs', exist_ok=True)
    
    # Save to CSV
    output_path = '../outputs/task4_commit_details.csv'
    df_task4.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Task 4 completed!")
    print(f"Total rows: {len(df_task4)}")
    print(f"Output saved to: {output_path}")
    print(f"\nFirst few rows:")
    print(df_task4.head())

if __name__ == "__main__":
    main()
