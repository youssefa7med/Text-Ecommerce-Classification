import streamlit as st
import pickle
import pandas as pd
import spacy

st.set_page_config(page_title="Text Ecommerce Classification", initial_sidebar_state='expanded', page_icon='📝', layout='wide')

data = pd.read_csv("Ecommerce_data_cleaned.csv")

nlp = spacy.load('en_core_web_sm')

def preprocesor(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct :
            tokens.append(token.lemma_)
    return " ".join(tokens)

try:
    model = pickle.load(open('model.pkl', 'r'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None


pred_type = {0: 'Books', 1: 'Clothing & Accessories', 2: 'Electronics', 3: 'Household'}

def predict(text):
    text = preprocesor(text)
    pred = model.predict([text])
    return pred_type[pred[0]]

# Header

st.markdown("""
    <div style="text-align: center; font-size: 50px; font-weight: bold; color: white;">
        📄 <span style="color: #dc6400;">Text Ecommerce Classification</span>
    </div>
    <div style="display: flex; justify-content: center;">
        <img src="https://th.bing.com/th/id/R.e275066ee7495c15858132d5a61a8a9e?rik=gSJuKa8ymAaEUA&pid=ImgRaw&r=0" alt="Text GIF" style="width: 80%; max-width: 900px;">
    </div>
""", unsafe_allow_html=True)

st.divider()

#give the user sample to test
st.markdown('''
    ## 📝 Test the Model
    - Enter the text in the text area below to classify the text into one of the following categories:
        - Books
        - Clothing & Accessories
        - Electronics
        - Household
''')
if st.button("Generate Sample Text to Test",help="Click to generate a sample text to test the model"):
    Generated_Text = data.sample(1).iloc[0][['Text','label']]
    st.text_area("Sample Text ", Generated_Text['Text'], height=200)
    st.write(f'The text belongs to: {Generated_Text["label"]}')

Input_Text = st.text_area("Enter the text to classify", height=200)

if st.button("Predict"):
    result = predict(Input_Text)
    st.success(f'The text belongs to: {result}')