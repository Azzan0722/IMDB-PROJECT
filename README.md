📌 IMDB 2024 Data Scraping and Visualizations
Project Overview
This project focuses on extracting, analyzing, and visualizing IMDb movie data for the year 2024. Using Selenium, we scrape movie details such as Name, Genre, Rating, Voting Counts, and Duration from IMDb. The data is organized by genre, saved as CSV files, merged into a single dataset, stored in an SQL database, and then analyzed and visualized using Python and Streamlit.

The final deliverable is an interactive Streamlit dashboard that allows users to explore insights, apply multiple filters, and visualize trends in the 2024 IMDb movie dataset.

✅ Skills I Learn
Web Scraping using Selenium

Data Cleaning & Analysis with Pandas

SQL Integration for structured storage

Data Visualization with Matplotlib & Seaborn

Interactive Dashboards using Streamlit

Python Programming & Automation

Domain
🎬 Entertainment / Data Analytics

Problem Statement
Manually analyzing IMDb data for trends and insights can be time-consuming and inefficient. This project automates the scraping, cleaning, storing, and visualization process, providing an interactive dashboard for quick and meaningful insights.

Business Use Cases
✔ Identify Top 10 Movies by rating and votes
✔ Analyze Genre Distribution and popularity
✔ Find Average Movie Duration per genre
✔ Discover Voting Patterns across genres
✔ Explore Rating Distribution and correlations
✔ Identify Shortest and Longest Movies in 2024
✔ Enable custom filtering (Genre, Rating, Duration, Votes) for dynamic exploration

Project Approach
1. Data Scraping and Storage
Data Source: IMDb 2024 Movies page

Scraping Tool: Selenium

Scraped Fields:

Movie Name

Genre

Rating

Voting Count

Duration

Storage Steps:

Save genre-wise CSV files

Merge into a single DataFrame

Store in SQL database (MySQL/PostgreSQL)

2. Data Analysis & Visualization
Libraries: Pandas, Matplotlib, Seaborn

Visualizations:

Top 10 Movies by Rating & Votes

Genre Distribution (Bar Chart)

Average Duration by Genre

Voting Trends by Genre

Rating Distribution (Histogram/Boxplot)

Heatmap for Genre vs Ratings

Correlation Analysis between Rating & Votes

Shortest & Longest Movies (Card/Table Display)

3. Interactive Streamlit Dashboard
Filters:

Genre

IMDb Rating (> 8.0)

Duration (< 2 hrs, 2–3 hrs, > 3 hrs)

Voting Count (> 10,000)

Dynamic Display:

Filtered Data Table

Updated Visualizations

Multi-filter Combination

Example Use Case
✅ Filter Action Movies with:

IMDb rating > 8.0

Duration 2–3 hours

Votes > 50,000
➡ Get results dynamically in Streamlit dashboard

Dataset
Scraped IMDb 2024 movies data with columns:

Movie Name

Genre

Rating

Voting Counts

Duration

Tech Stack
Language: Python

Database: MySQL / PostgreSQL

Visualization: Streamlit, Matplotlib, Seaborn

Libraries: Pandas, Selenium, SQLAlchemy

Project Deliverables
✔ SQL Database with full dataset
✔ Python Scripts for scraping, cleaning, merging, and DB operations
✔ Genre-wise CSV Files
✔ Merged DataFrame
✔ Streamlit Dashboard for interactive analysis










Ask ChatGPT
