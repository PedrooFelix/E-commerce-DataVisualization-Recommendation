import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import streamlit.components.v1 as components

st.write("""
# E-commerce Data Visualization

The purpose of this project is to do some analysis in an e-commerce dataset and do some conclusions.
I am too using the google search product category name to do some predictions.



""")

components.html(
    """
   <iframe width="700" height="700" src="https://prezi.com/view/kwWp6xVHQglHMmN55wwy/embed" webkitallowfullscreen="1" mozallowfullscreen="1" allowfullscreen="1"></iframe>
    """,
    height=700,width=750
)

st.write("""
# E-commerce Data Visualization

The purpose of this project is to do some analysis in an e-commerce dataset and do some conclusions.
I am too using the google search product category name to do some predictions.

The link of the github: https://github.com/PedrooFelix


Data obtained from the https://www.kaggle.com/olistbr/brazilian-ecommerce.
""")

