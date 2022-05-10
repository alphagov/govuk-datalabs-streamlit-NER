"""
Example of using manual=True for visualize_ner.
"""
from distutils.command import config
from packages import visualizer
import streamlit as st
import spacy
from config import entity_names, colors, MODEL_PATH, TOKENIZER_PATH
from packages.utils import _load_model, _url_to_exes

st.title("Named Entity Recognition Demo")
st.write("### Demonstration of NER on GOV.UK page")
st.write("Data Labs has developed a model that can detect entities of interest from 'govspeak' in GOV.UK content. \n\nUse the tool below on any GOV.UK url to see how it works.")
url = st.text_input("Insert url from GOV.UK", value='https://www.gov.uk/student-visa')
ner_model = _load_model(MODEL_PATH=MODEL_PATH, TOKENIZER_PATH=TOKENIZER_PATH)
doc = _url_to_exes(url, ner_model)

# ner visualisations
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

st.write("### Demonstration of Dependancy Parsing")
st.write("Dependancy Parsing could be the key to bridging the gap between entity extraction and semantic understanding. \n\nCan we combine the two approaches?")
st.write("https://web.stanford.edu/~jurafsky/slp3/14.pdf")

# dependancy parsing visualisations
spacy_model = "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")
dep_text = st.text_input("Insert sentence for dependancy parsing", value='You must be 18 or over. You must be a UK or EU national.')
docy = nlp(dep_text)
visualizer.visualize_parser(
    docy,
    title=None,
)
