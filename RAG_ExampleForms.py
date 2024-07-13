import os

import time


from src.utils import load_keys

import os
# from langchain.chat_models import ChatOpenAI
import numpy as np

from pinecone import Pinecone
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as PineconeLang
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_openai import ChatOpenAI
from pinecone import ServerlessSpec

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


os.environ["OPENAI_API_KEY"] = load_keys()["openai"]
os.environ["DEEPGRAM_API_KEY"] = load_keys()["deepgram"]
os.environ["PINECONE_API_KEY"] = load_keys()["pinecone"]

from dotenv import load_dotenv
load_dotenv()



class LLMLangchain:

    def __init__(self) -> None:
        self.chat = ChatOpenAI( openai_api_key=os.environ["OPENAI_API_KEY"], model='gpt-3.5-turbo')
        self.embeddings=OpenAIEmbeddings(model="text-embedding-ada-002",api_key=os.environ["OPENAI_API_KEY"])
        self.pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        self.spec = ServerlessSpec(
                                    cloud="aws", region="us-east-1"
                                  )
        self.index_name = "dct-example-forms-index"
        self.index = self.init_pinecone()
        self.messages = [
                            SystemMessage(content="You are a helpful answer provider for Duck Creek Forms development and you will be asked the questions related to Duck Creek forms functionality to get the information."),
                        ]




    def init_pinecone(self):
        # connect to index
        self.index = self.pc.Index(self.index_name)
        time.sleep(1)
        return self.index
    

    def generate_insert_embeddings_(self, docs):

        for j in range(len(docs)):
            embeddings = [{"metadata": ""}]

            ids = [str(j)]
            # Generate embeddings and ensure it's a flat list of floats
            embeds = self.embeddings.embed_documents(docs[j].page_content)
            embeddings[0]["metadata"]= str(docs[j].page_content)


            self.index.upsert(vectors=zip(ids, embeds, embeddings))
            # time.sleep(1)

            # for id, embed, meta in zip(ids, embeds, embeddings):
            #     print(f"ID: {id}, Embedding: {type(embed)}, Metadata: {meta}")
            #     print("##################")



    def retrieve_query(self, index, query, k=2):
        matching_results=index.similarity_search(query,k=k)
        return matching_results

    def read_doc(self, directory):
        file_loader=PyPDFDirectoryLoader(directory)
        documents=file_loader.load()
        # print(documents)
        return documents

    def chunk_data(self, docs,chunk_size=800,chunk_overlap=50):
        self.text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        self.doc=self.text_splitter.split_documents(docs)
        return self.doc

    def augment_prompt(self, query: str):
        vectorstore = PineconeLang(
                        self.index,  self.embeddings.embed_query,"metadata", distance_strategy = DistanceStrategy.DOT_PRODUCT
                        )
        # get top 3 results from knowledge base
        results = vectorstore.similarity_search(query, k=1)
        # get the text from the results
        source_knowledge = "\n".join([x.page_content for x in results])
        # feed into an augmented prompt
        augmented_prompt = f"""Using the contexts below, answer the query.

        Contexts:
        {source_knowledge}

        Query: {query}"""
        return augmented_prompt


# if __name__ == "__main__":

#     llm = LLMLangchain()



#     ######################################################################
#     ##To Generate new embedding -- Uncomment below line of code--
#     print("Embedding Started")
#     doc = llm.read_doc("Database/")
#     documents=llm.chunk_data(docs=doc)
#     print(len(documents))
#     embeddings = llm.generate_insert_embeddings_(documents)
# #     ######################################################################


# #     query = "What are the ingredients for prawn masala"
# #     prompt = llm.augment_prompt(query=query)
# #     prompt = HumanMessage(
# #     content=prompt
# #     )

# #     llm.messages.append(prompt)

# #     res = llm.chat(llm.messages)
# #     print("#############----Output----###########################")
# #     print(res.content)
