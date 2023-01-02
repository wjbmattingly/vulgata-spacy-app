import streamlit as st
from vulgata_spacy import vulgata_spacy
import pandas as pd
from annoy import AnnoyIndex
import json
import base64
from pathlib import Path

st.set_page_config(page_title='VulgateAI - Home', page_icon = "images/icon.png", layout = 'wide', initial_sidebar_state = 'auto')

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html


@st.cache(allow_output_mutation=True)
def load_pipeline():
    nlp = vulgata_spacy.VulgataSpaCy()
    return nlp

@st.cache(allow_output_mutation=True)
def load_annoy():
    t = AnnoyIndex(100, metric="angular")
    t.load("annoy_index/clem_400_partial.ann")
    return t

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv("data/clem_vulgate.csv")
    with open("data/index_map_partial.json", "r") as f:
        index_map = json.load(f)
    return df, index_map

# st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('images/header.png')+"</p>", unsafe_allow_html=True)
st.image('images/header.png')
nlp = load_pipeline()
t = load_annoy()
df, index_map = load_data()

text = st.text_area("Paste Phrase Here")
col1, col2 = st.columns(2)
display_mode = col1.selectbox("Display Style", ["Table", "DataFrame"])
max_results = col2.slider("Max Results", 100, max_value=500)
if text != "":
    doc = nlp.create_doc(text).vector
    res = t.get_nns_by_vector(doc, max_results, include_distances=True)
    matches = []
    for idx, score in zip(res[0], res[1]):
        df_idx = index_map[str(idx)]
        answer = df.iloc[df_idx]
        answer["score"] = score
        answer.pop("latin_clean")
        answer = answer[["score", "book", "chapter", "verse", "latin"]]
        matches.append(answer)
    res_df = pd.DataFrame(matches)
    if display_mode == "Table":
        st.table(res_df)
    else:
        st.write(res_df)
