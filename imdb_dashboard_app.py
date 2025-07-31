import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sqlalchemy import create_engine

# ✅ Set page config FIRST
st.set_page_config(layout="wide", page_title="IMDb Dashboard")

# ✅ Styling
plt.style.use('ggplot')
sns.set_palette('deep')

# ✅ App title
st.title("IMDb Dashboard")
st.markdown("Explore insights from IMDb's 2024 movie list with interactive filters and dynamic charts.")

# ✅ Database connection
engine = create_engine('mysql+mysqlconnector://root:root@localhost/imdb_db')

@st.cache_data
def load_data():
    query = "SELECT * FROM movies"
    return pd.read_sql(query, engine)
movies_df = load_data()

# ✅ Check if data exists
if movies_df.empty:
    st.warning("No movie data available. Please ensure your 'movies' table in 'imdb_db' is populated.")
else:
    # ✅ Ensure correct data types
    movies_df['genre'] = movies_df['genre'].astype(str)
    movies_df['rating'] = pd.to_numeric(movies_df['rating'], errors='coerce').fillna(0)
    movies_df['duration_minutes'] = pd.to_numeric(movies_df['duration_minutes'], errors='coerce').fillna(0)
    movies_df['voting_counts'] = pd.to_numeric(movies_df['voting_counts'], errors='coerce').fillna(0)

    # --- Sidebar Filters ---
    st.sidebar.header("Filter Movies 📊")
    all_genres = sorted(movies_df['genre'].unique().tolist())
    selected_genres = st.sidebar.multiselect("Select Genre(s):", options=all_genres, default=all_genres)

    filtered_df = movies_df[movies_df['genre'].isin(selected_genres)]
 # Sliders (dynamic)
    if not filtered_df.empty:
        rating_range = st.sidebar.slider("Rating Range:", 
                                         float(filtered_df['rating'].min()), 
                                         float(filtered_df['rating'].max()), 
                                         (float(filtered_df['rating'].min()), float(filtered_df['rating'].max())), 
                                         step=0.1)
        duration_range = st.sidebar.slider("Duration (minutes):", 
                                           int(filtered_df['duration_minutes'].min()), 
                                           int(filtered_df['duration_minutes'].max()), 
                                           (int(filtered_df['duration_minutes'].min()), int(filtered_df['duration_minutes'].max())), 
                                           step=5)
        vote_range = st.sidebar.slider("Voting Counts:", 
                                       int(filtered_df['voting_counts'].min()), 
                                       int(filtered_df['voting_counts'].max()), 
                                       (int(filtered_df['voting_counts'].min()), int(filtered_df['voting_counts'].max())), 
                                       step=1000)
    else:
        st.warning("No data after applying genre filter.")
        st.stop()

    # ✅ Apply filters
    final_df = filtered_df[
        (filtered_df['rating'].between(rating_range[0], rating_range[1])) &
        (filtered_df['duration_minutes'].between(duration_range[0], duration_range[1])) &
        (filtered_df['voting_counts'].between(vote_range[0], vote_range[1]))
    ]
    st.subheader("Filtered Movie Data 🎥")
    st.dataframe(final_df)
    st.write(f"Displaying {len(final_df)} movies (out of {len(movies_df)}).")

    if final_df.empty:
        st.info("No movies match your filter criteria.")
        st.stop()

    # --- Visualizations ---
    st.header("Interactive Visualizations 📈")

    # Top 10 by Rating
    st.markdown("### Top 10 Movies by Rating")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(
    x='rating',
    y='movie_name',
    data=final_df.sort_values('rating', ascending=False).head(10),
    ax=ax1,
    hue='movie_name',    # <-- Added
    palette='viridis',
    legend=False          # <-- Added to hide duplicate legend
    )

    ax1.set_title('Top 10 Movies by IMDb Rating')
    st.pyplot(fig1)
     # Genre Distribution
    st.markdown("### Genre Distribution")
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    sns.countplot(
    y='genre',
    data=final_df,
    order=final_df['genre'].value_counts().index,
    ax=ax2,
    hue='genre',         # <-- Added
    palette='coolwarm',
    legend=False          # <-- Added
    )

    ax2.set_title('Distribution of Movies Across Genres')
    st.pyplot(fig2)

    # Rating Distribution
    st.markdown("### Rating Distribution")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.histplot(final_df['rating'], kde=True, bins=10, ax=ax3, color='skyblue')
    ax3.set_title('IMDb Rating Distribution')
    st.pyplot(fig3)

    # Correlation: Rating vs Votes
    st.markdown("### Rating vs. Voting Counts")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='voting_counts', y='rating', data=final_df, hue='genre', alpha=0.7)
    ax4.set_xscale('log')
    ax4.set_title('Rating vs Voting Counts')
    st.pyplot(fig4)