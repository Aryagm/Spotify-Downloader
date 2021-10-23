import streamlit as st
from first_look import get_song
from os import popen
import os
import time
import glob

st.title("Spotify downloader")

song = st.text_input("Enter the song name:")

b = st.button("Download")

if song:
    response = get_song(song)
    st.write("Song Name:", response[0])
    song_url = response[1]
    st.write("Song URL:", response[1])
    st.write("Album:", response[2])
    st.write("Artist:", response[4])
    st.image(response[3])
    if b:
        stream = popen(f"spotdl {song_url}")
        st.warning("Dowloading Song")
        time.sleep(20)
        # So once it's done downloading something, show a download done message.
        st.success("Download done!")
        newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)
        st.audio(newest)
        os.remove(newest)