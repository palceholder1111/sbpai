import streamlit as st
from data_fetcher import get_todays_games
from analyzer import calculate_confidence_score

st.title("AI Sports Betting Bot")

api_key = st.secrets["odds_api_key"]
weather_api_key = st.secrets["weather_api_key"]
games = get_todays_games(api_key)

for game in games:
    team_stats = {}  # Placeholder
    injuries = {}    # Placeholder
    weather = {}     # Placeholder
    odds = {}        # Placeholder
    matchup_record = {}  # Placeholder

    confidence = calculate_confidence_score(team_stats, injuries, weather, odds, matchup_record)

    if confidence > 50:
        st.markdown(f"✅ **{game['home_team']} vs {game['away_team']}**")
        st.write(f"Confidence Score: {confidence}")