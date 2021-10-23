import streamlit as st
from get_data import get_song
from os import popen
import os
import time
import glob

st.title("Spotify downloader")

song = st.text_input("Enter the song name:")

b = st.button("Download")

if song:
    response = get_song(str(song))
    st.write("Song Name:", response[0])
    song_url = response[1]
    st.write("Song URL:", response[1])
    st.write("Album:", response[2])
    st.write("Artist:", response[4])
    st.image(response[3])
    if b:
        print(song_url)
        stream = popen(f"spotdl {song_url}")
        st.warning("Dowloading Song")
        time.sleep(20)
        # So once it's done downloading something, show a download done message.
        try:
            newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)
            st.audio(newest)
            os.remove(newest)
            st.success("Download done!")
        except:
            st.error("Unable to download song!")
        
        