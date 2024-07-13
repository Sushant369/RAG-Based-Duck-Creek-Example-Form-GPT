# Duck Creek Example Forms Mate

Welcome to Duck Creek Example Forms Mate, an innovative tool designed to streamline the development process for Duck Creek Technologies forms. This system leverages a comprehensive knowledge base of example forms to enhance developer productivity and efficiency.

## Features

- **Language Understanding**: Utilizes LangChain for accurate language understanding.
- **Advanced Text Embedding and Responses**: Employs OpenAI's "text-embedding-ada-002" and "gpt-3.5-turbo" models.
- **Efficient Information Retrieval**: Uses cosine similarity to retrieve relevant information from Pinecone's vector database.
- **CI/CD Integration**: Robust deployment through CI/CD pipelines on Heroku, ensuring seamless updates and high reliability.
- **Automated Testing**: Incorporates `pytest` for comprehensive automated testing to maintain code quality.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- Flask
- Langchain
- A Pinecone API key
- An OpenAI API key

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/duck-creek-example-forms-mate.git
cd duck-creek-example-forms-mate
pip install -r requirements.txt
python3 app.py
```
## Running Tests
Execute the test suite with:

```bash
pytest
```
## Deployment
Details on deploying the application to Heroku using the provided CI/CD pipelines.



Explore Duck Creek Example Forms Mate and see how it can enhance your form development processes!
