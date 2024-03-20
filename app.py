import streamlit as st
import sqlite3  # To interact with your database
from database import get_random_word  # Assuming your database functions are in database.py

def main():
    st.title("Vocab Trainer")

    target_language = st.selectbox("Select your target language:", ["Spanish", "French", "Japanese"])

    # Placeholder for fetching the initial word
    word_data = get_random_word(target_language) 
    if word_data:
        st.write(word_data[1])  # Display the 'word' 
    else:
        st.write("Add some words to your database to get started!")

    user_answer = st.text_input("Enter translation:")

    if st.button("Check Answer"):
        # Placeholder for AI-powered answer checking logic
        st.write("AI will check your answer here...") 

    if st.button("Next Word"):
        # Placeholder to fetch a new word
        st.write("Fetching a new word...")

if __name__ == "__main__":
    main()
