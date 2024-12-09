import os
import pickle
import time
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

st.title("HarshadBot: Your Personal Finance Research Tool")
st.sidebar.title("News Article URLs")

urls=[]
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

file_path = "faiss_index.pkl"
main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    max_tokens=100,
    temperature=0.5,
)

if st.sidebar.button("Submit"):
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
    chunk_overlap=200)
    docs = splitter.split_documents(data)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(docs,embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    with open(file_path, "wb") as f:
        pickle.dump(vector_store, f)

query = main_placeholder.text_input("Ask me anything based on the URLs you provided")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            loaded_vector_store = pickle.load(f)
            retriever = loaded_vector_store.as_retriever()
            chain = RetrievalQAWithSourcesChain.from_chain_type(
                llm=llm,
                retriever=retriever,
            )
            result = chain(query)
            st.header("RockyBot's Response")
            st.write(result['answer'])

            sources = result['sources']
            st.subheader("Sources")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)

