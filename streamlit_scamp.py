from scamp import *
#import clockblocks
import streamlit as st

st.set_page_config(page_title = "streamlit and scamp", page_icon = ":tdata:")
st.subheader("chekc check :wave:")
st.title("streamlit and scamp")

s = Session()
s.tempo = 120

#s.print_default_soundfont_presets()
piano = s.new_part("piano")

# 60 = c4; 61 = c4#, and 59 = b3

pitch_list = [60, 64, 66]

c2 = [36,38,40,41,43,41,40,38,36]

#play all notes in the 18 arrays above

for note in c2:
    piano.play_note(note, 0.8, 1)
