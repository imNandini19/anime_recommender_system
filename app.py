import streamlit as st
import pickle
import pandas as pd

df=pickle.load(open("df.pkl","rb"))
cosine_sim = pickle.load(open("cosine_sim.pkl","rb"))


def recommend_anime(title, n=5):
    if title not in df['name'].values:
        return ["Anime not found"]

    idx = df.index[df['name'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    anime_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[anime_indices].tolist()

st.title("🎌 Anime Recommendation System")
st.write("Select an anime to get similar recommendations.")

selected = st.selectbox("Choose an anime:", df['name'].values)

if st.button("Recommend"):
    st.subheader("Recommended Anime:")
    results = recommend_anime(selected)
    for r in results:
        st.write("• " + r)
