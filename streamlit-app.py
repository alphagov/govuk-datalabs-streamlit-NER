"""
Example of using manual=True for visualize_ner.
"""
from distutils.command import config
from testy import visualizer
import streamlit as st
from config import entity_names, colors, MODEL_PATH, TOKENIZER_PATH
from utils import _load_model, _url_to_exes

st.title("Named Entity Recognition Demo")
st.write("### Demonstration of NER on GOV.UK page")
url = st.text_input("Insert url from GOV.UK", value='https://www.gov.uk/student-visa')
ner_model = _load_model(MODEL_PATH=MODEL_PATH, TOKENIZER_PATH=TOKENIZER_PATH)
doc = _url_to_exes(url, ner_model)

visualizer.visualize_ner(
    doc,
    labels=entity_names,
    show_table=False,
    displacy_options={
        "colors" : colors,
        "kb_url_template": "https://www.wikidata.org/wiki/{}"
    },
    title=None,
    manual=True
)

