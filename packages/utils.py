# ============= Helper Functions ============ #

import os
import requests
import streamlit as st
import spacy_streamlit
from spacy import displacy
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

@st.cache(hash)
def _load_model(MODEL_PATH, TOKENIZER_PATH):
    model = AutoModelForTokenClassification(MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    token_classifier = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    return token_classifier

#get a html response from a page of interest
def _get_page_soup(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  return soup

#get text data from html and return list of sentences
def _get_sents_from_soup(soup):
  body = soup.findAll(attrs={"class":"gem-c-govspeak"})
  sents = [i.text.split('\n') for i in body]
  sents_clean = [list(filter(None, i)) for i in sents]
  return sents_clean

#get html and sentences from url
def _url_get_sents(url):
  soup = _get_page_soup(url)
  sents_clean = _get_sents_from_soup(soup)
  sents_clean = sents_clean[0]
  return sents_clean

def _load_model(MODEL_PATH, TOKENIZER_PATH):
  model = AutoModelForTokenClassification.from_pretrained(MODEL_PATH)
  tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
  token_classifier = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
  return token_classifier

# def _get_token_classifier(MODEL_PATH, TOKENIZER_PATH):
#   model = AutoModelForTokenClassification.from_pretrained(MODEL_PATH)
#   tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
#   token_classifier = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
#   return token_classifier

def _get_exes(page_sentences, tags):
  exes = []
  for i in range(len(page_sentences)):
    text = page_sentences[i]
    ents = [{'start':j['start'], 'end':j['end'] , 'label':j['entity_group']} for j in tags[i]]
    ex = {'text': text,
          'ents': ents}
    exes.append(ex)
  return exes

def _visualise_ents(exes_list):
  options = {"ents": entity_names, "colors": colors}
  viz = displacy.render(exes_list, style="ent", jupyter=True, manual=True, options=options)
  return viz

def _url_to_exes(url, token_classifier):
  page_sents = _url_get_sents(url)
  model_tags = token_classifier(page_sents)
  exes = _get_exes(page_sents, model_tags)
  return exes

def _url_to_ents(url, token_classifier):
  page_sents = _url_get_sents(url)
  model_tags = token_classifier(page_sents)
  exes = _get_exes(page_sents, model_tags)
  _visualise_ents(exes)