# ============= Config ============ #

from transformers import TOKENIZER_MAPPING


colors = {"ORG": "#7c5cdd", 
          "FORM": "#26e21c",
          "LOC": "#eee65c",
          "MONEY": "#80bab2",
          "SCHEME": "#b76d14",
          "DATE": "#bc8251",
          "STATE": "#bd4c33",
          "PER": "#c0970b",
          "FINANCE": "#debdd8",
          "FORM": "#48aba2",
          "EVENT": "#0a8dd9",
          "CONTACT": "#807388"}

entity_names = [k for (k,v) in colors.items()]

MODEL_PATH= "./Models/checkpoint-3500"
TOKENIZER_PATH= "./Models/checkpoint-3500"