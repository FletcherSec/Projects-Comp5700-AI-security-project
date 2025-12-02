"""
Script to load and explore the AIDev dataset from HuggingFace
Run this first to understand the dataset structure
"""

from datasets import load_dataset
import pandas as pd

def main():
    print("Loading dataset from HuggingFace...")
    print("This may take a few minutes on first run...\n")
    
    # Load the dataset
    dataset = load_dataset("hao-li/AIDev")
    
    # Display available tables/splits
    print("Available tables in dataset:")
    print(dataset.keys())
    print("\n" + "="*60 + "\n")
    
    # Explore each table
    for table_name in dataset.keys():
        print(f"Table: {table_name}")
        print(f"Number of rows: {len(dataset[table_name])}")
        print(f"Columns: {dataset[table_name].column_names}")
        print(f"\nFirst row sample:")
        print(dataset[table_name][0])
        print("\n" + "="*60 + "\n")
    
    # Save dataset object for later use (optional)
    print("Dataset loaded successfully!")
    print("\nYou can now proceed with the individual tasks.")
    
    return dataset

if __name__ == "__main__":
    dataset = main()
