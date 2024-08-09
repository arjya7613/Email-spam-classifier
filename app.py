{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b2dfee94-f9fe-4747-bd0a-a6bf35c6dc18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in f:\\anaconda\\lib\\site-packages (1.32.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in f:\\anaconda\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in f:\\anaconda\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in f:\\anaconda\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in f:\\anaconda\\lib\\site-packages (from streamlit) (2.32.2)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in f:\\anaconda\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in f:\\anaconda\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in f:\\anaconda\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in f:\\anaconda\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in f:\\anaconda\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in f:\\anaconda\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in f:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in f:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in f:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in f:\\anaconda\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in f:\\anaconda\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in f:\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in f:\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in f:\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in f:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in f:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in f:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in f:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in f:\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in f:\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in f:\\anaconda\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in f:\\anaconda\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in f:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in f:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in f:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in f:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in f:\\anaconda\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in f:\\anaconda\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cdf301f0-e78f-485f-89eb-5eda625b5335",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c54202af-d598-49ab-b607-5aa290c502a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "240a99d2-6713-4fc2-b47a-c41b595896ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "#lets load the saved vectorizer and Naive bayes\n",
    "tfidf  = pickle.load(open('vectorizer.pkl','rb'))\n",
    "model  = pickle.load(open('model.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "26a7c055-c28b-41b6-8429-6a40b5124af0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#transform_text function for the text preprocessing\n",
    "import nltk\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer\n",
    "import string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dd97795a-4c11-429e-81f9-2c603a6992e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\HP\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "33985c2b-db0c-4fe8-8e9d-eef1511b8a10",
   "metadata": {},
   "outputs": [],
   "source": [
    "ps = PorterStemmer()\n",
    "def transform_text(text):\n",
    "    text = text.lower()  # converting to lowercase\n",
    "    text = nltk.word_tokenize(text)  #Tokeizer\n",
    "\n",
    "    # Removing special characters and retaining alphanumeric words\n",
    "    text =[word for word in text if word.isalnum()]\n",
    "\n",
    "    # Removing stopwords and punctuation \n",
    "    text = [word for word in text if word not in stopwards.words('english') and word not in string.punctuation]\n",
    "\n",
    "    # Applying stemming\n",
    "    text = [ps.stem(word) for word in text]\n",
    "    return \"\".join(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8d8582ae-2d0d-4d71-a0d5-4b56e4c6271b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# saving streanlit code\n",
    "st.title(\"Email Spam Classifier\")\n",
    "input_sms = st.text_area(\"enter message\")\n",
    "\n",
    "if st.button('Predict'):\n",
    "    # preprocessor\n",
    "    transformed_sms = transform_text(input_sms)\n",
    "    \n",
    "    # vectorizer\n",
    "    vector_input = tfidf.transform([transformed_sms])\n",
    "    \n",
    "    # predict\n",
    "    result = model.predict(vector_input)[0]\n",
    "    \n",
    "    # display\n",
    "    if result == 1:\n",
    "        st.header(\"Spam\")\n",
    "    else:\n",
    "        st.header(\"Not Spam\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
