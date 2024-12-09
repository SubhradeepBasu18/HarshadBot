# HarshadBot

HarshadBot is a personal finance research tool that leverages the power of language models to provide insights based on news articles. It uses Streamlit for the user interface and integrates various components from the LangChain library to process and analyze the data.

## Features

- Load and process news articles from provided URLs.
- Split documents into manageable chunks.
- Generate embeddings using the HuggingFace model.
- Build a FAISS vector store for efficient retrieval.
- Answer user queries based on the processed data.
- Display the sources of the information provided.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/harshadbot.git
    cd harshadbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a 

.env

 file in the root directory.
    - Add your Google API key:
        ```
        GOOGLE_API_KEY="your_google_api_key"
        ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run 

app.py


    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the URLs of the news articles in the sidebar and click "Submit".

4. Once the data is processed, you can ask questions based on the provided URLs.