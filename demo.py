# Load the dataset
####################################################################
#Task 7
import ollama


# Implement the retrieval system

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []


def add_chunk_to_database(chunk):
  embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
  VECTOR_DB.append((chunk, embedding))
####################################################################
#Task 4
def cosine_similarity(A, B):
  dot_product = sum(a*b for a, b in zip(A, B))

  magnitude_A = sum(a*a for a in A)**0.5
  magnitude_B = sum(b*b for b in B)**0.5
  return dot_product / (magnitude_A * magnitude_B)

####################################################################
#Task 5
def retrieve(query, top_n=3):
  query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
  # temporary list to store (chunk, similarity) pairs
  similarities = []
  for chunk, embedding in VECTOR_DB:
    similarity = cosine_similarity(query_embedding, embedding)
    similarities.append((chunk, similarity))
  # sort by similarity in descending order, because higher similarity means more relevant chunks
  similarities.sort(key=lambda x: x[1], reverse=True)
  # finally, return the top N most relevant chunks
  return similarities[:top_n]
####################################################################
#Task 2
dataset = []
with open('cat-facts.txt', encoding="utf8") as file:
  dataset = list(file)

####################################################################
#Task 3
for i, chunk in enumerate(dataset): 
  add_chunk_to_database(chunk=chunk)

####################################################################
#Task 6
text_intro = f" Welcome to your cat-model. Ask me a question about cat: "

# For example, a prompt can be constructed as follows:
input_query = input(text_intro)

list_retrieved_knowledge = []
const_top_n = 3
for i in range(5):
  list_retrieved_knowledge.append( retrieve(input_query, i + const_top_n))
answers = []
for retrieved_knowledge in list_retrieved_knowledge:
  print(f'\nRetrieved knowledge:')
  for chunk, similarity in retrieved_knowledge:
    print(f' - (similarity: {similarity:.2f}) {chunk}')
    
  instruction_prompt = f'''You are a expert on cats and your task is to answer question about cats.
  Use only the following pieces of context to answer the question. Don't make up any new information:
  {'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}'''


  stream = ollama.chat(
    model=LANGUAGE_MODEL,
    messages=[
      {'role': 'system', 'content': instruction_prompt},
      {'role': 'user', 'content': input_query},
    ],
    stream=True,
  )

  # print the response from the chatbot in real-time
  print('Chatbot response:')
  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
  print("####################################################################")
