import pandas as pd
import os

# Security keywords from project requirements
SECURITY_KEYWORDS = [
    'race', 'racy', 'buffer', 'overflow', 'stack', 'integer', 
    'signedness', 'underflow', 'improper', 'unauthenticated', 
    'gain access', 'permission', 'cross site', 'css', 'xss', 
    'denial service', 'dos', 'crash', 'deadlock', 'injection', 
    'request forgery', 'csrf', 'xsrf', 'forged', 'security', 
    'vulnerability', 'vulnerable', 'exploit', 'attack', 'bypass', 
    'backdoor', 'threat', 'expose', 'breach', 'violate', 'fatal', 
    'blacklist', 'overrun', 'insecure'
]

def check_security_keywords(text):
    """
    Check if any security keywords appear in the text.
    Returns 1 if found, 0 otherwise.
    """
    if pd.isna(text) or text is None:
        return 0
    
    # Convert to lowercase for case-insensitive matching
    text_lower = str(text).lower()
    
    # Check each keyword
    for keyword in SECURITY_KEYWORDS:
        if keyword in text_lower:
            return 1
    
    return 0

def main():
    print("Loading Task 1 output (pull requests)...")
    df_task1 = pd.read_csv('../outputs/task1_pull_requests.csv')
    
    print("Loading Task 3 output (task types)...")
    df_task3 = pd.read_csv('../outputs/task3_task_types.csv')
    
    print(f"Task 1 rows: {len(df_task1)}")
    print(f"Task 3 rows: {len(df_task3)}")
    
    # Merge the two datasets on PR ID
    print("Merging datasets...")
    df_merged = df_task1.merge(
        df_task3, 
        left_on='ID', 
        right_on='PRID', 
        how='inner'
    )
    
    print(f"Merged rows: {len(df_merged)}")
    
    # Check for security keywords in both TITLE and BODYSTRING
    print("Scanning for security keywords...")
    df_merged['SECURITY_TITLE'] = df_merged['TITLE'].apply(check_security_keywords)
    df_merged['SECURITY_BODY'] = df_merged['BODYSTRING'].apply(check_security_keywords)
    
    # Set SECURITY flag to 1 if keywords found in either title or body
    df_merged['SECURITY'] = df_merged[['SECURITY_TITLE', 'SECURITY_BODY']].max(axis=1)
    
    # Create final output with required columns
    df_task5 = pd.DataFrame({
        'ID': df_merged['ID'],
        'AGENT': df_merged['AGENTNAME'],
        'TYPE': df_merged['PRTYPE'],
        'CONFIDENCE': df_merged['CONFIDENCE'],
        'SECURITY': df_merged['SECURITY']
    })
    
    # Create outputs directory if it doesn't exist
    os.makedirs('../outputs', exist_ok=True)
    
    # Save to CSV
    output_path = '../outputs/task5_security_flagged.csv'
    df_task5.to_csv(output_path, index=False, encoding='utf-8')
    
    # Print statistics
    security_count = df_task5['SECURITY'].sum()
    total_count = len(df_task5)
    percentage = (security_count / total_count * 100) if total_count > 0 else 0
    
    print(f"\nTask 5 completed!")
    print(f"Output saved to: {output_path}")
    print(f"Total rows: {total_count}")
    print(f"Security-flagged PRs: {security_count} ({percentage:.2f}%)")
    print("\nFirst few rows:")
    print(df_task5.head())
    
    # Show breakdown by agent
    print("\nSecurity flags by agent:")
    agent_stats = df_task5.groupby('AGENT')['SECURITY'].agg(['sum', 'count'])
    print(agent_stats)

if __name__ == "__main__":
    main()
