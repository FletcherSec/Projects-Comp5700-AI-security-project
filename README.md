# AI Security Project for Comp-5700

## Overview
This project analyzes security-related tasks in AI-generated pull requests using the AIDev dataset from HuggingFace. The analysis processes 932,791 pull requests to identify security patterns across different AI coding agents.

## Repository Structure
```
├── scripts/          # Python scripts for data extraction and analysis
├── outputs/          # Generated CSV files (committed with lfs as largest CSV is almost 600MB)
└── README.md
```

## Scripts

**load_dataset.py** - Explores the AIDev dataset structure

**task1_extract_prs.py** - Extracts pull request data (title, ID, agent, body, repo info)

**task2_extract_repos.py** - Extracts unique repository information (language, stars, URL)

**task3_extract_types.py** - Extracts PR classification data (type, reason, confidence)

**task4_extract_commits.py** - Extracts commit details with cleaned diffs (additions, deletions, patches)

**task5_security_flags.py** - Identifies security-related PRs using keyword matching

## Outputs

Due to GitHub's file size limits, CSV files were uploaded via git-lfs and must be downloaded to be viewed.

## Requirements
```bash
pip install pandas datasets huggingface_hub
```

## Usage
```bash
cd scripts
python3 task1_extract_prs.py
python3 task2_extract_repos.py
python3 task3_extract_types.py
python3 task4_extract_commits.py
python3 task5_security_flags.py
```

## Dataset
Source: [hao-li/AIDev](https://huggingface.co/datasets/hao-li/AIDev)
