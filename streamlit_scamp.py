from scamp import *
import streamlit as st

st.set_page_config(page_title = "streamlit and scamp", page_icon = ":tdata:")
st.subheader("chekc check :wave:")
st.title("streamlit and scamp")

s = Session()
s.tempo = 120

piano = s.new_part("piano")
c2 = [36,38,40,41,43,41,40,38,36]

for note in c2:
    piano.play_note(note, 0.8, 1)
