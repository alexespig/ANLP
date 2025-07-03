# ANLP
This code contain comments to identify which task is answered by the code. 
You only need to run the demo.py by python demo.py in the console

- Top-n retrieval: The higher the value of n, the more context the model receives from the retrieval process.
- Prompt dependency: The tone of the model's response can vary depending on the phrasing of the first part of the prompt.
- Limitations: For some questions, the model may not have enough information to provide a complete answer. When only short context snippets are given, it's difficult for the model to generate robust responses.
- Data quantity: Providing more data can improve answer accuracy. However, with a small k (i.e., fewer retrieved passages), the improvement remains limited because the model still sees only a small portion of the available information.
- Model capability: A more advanced model could interpret the context more effectively. However, it may also rely more on its internal knowledge than on the provided input, which can lead to hallucinations.
- 
### Example with normal input: 
- Input: Which are the most common diseases in cats?
- Observed results: the more context the more the model use only the information given and not knowledge from the model

### Example with non-sense input: 
- Input: How many lives does a cat have?
- Answer with top-3: It's not clear how the question is being interpreted. The original text mentions that "the oldest cat on record was Crème Puff from Austin, Texas", but it doesn't provide information about cats having multiple lives. 
However, according to the text, it's also mentioned that a cat typically can live up to 20 years, which is equivalent to about 96 human years. This suggests that each individual cat has one lifetime, but I don't have any information on how many "lives" a cat has in total
- Answer with top-4: The average life span of a domestic cat is 14 years, but it can live up to 20 years with proper care and attention. A human has about 96 years of life, which equates to the lifespan of around three cats!
- Answer with top-5: Unfortunately, I couldn't find any information that provides an average life span of 20 years as specified earlier. However, according to the provided context, Crème Puff from Austin, Texas, lived for about 96 human years after her birth (as mentioned in the third point). This suggests that cats can live significantly longer than the mentioned 20 years, but I couldn't find any information on a single life span of 20 or more years
- Answer with top-6: There is no information provided that suggests cats can live "lives" as they are not living beings. According to the context, a domestic cat's average life span is 14 years. If you're referring to how often a cat can live, it varies depending on factors such as breed and lifestyle.
- Answer with top-7: Unfortunately, the exact number of lives that a domestic cat can live is difficult to determine, as it depends on various factors such as breed, lifestyle, and living conditions. However, according to the information provided, a typical domestic cat has an average life span of 14 years.
  In contrast, Crème Puff from Austin, Texas, holds the record for being the oldest cat ever recorded, with a lifespan equivalent to about 96 human years (which is roughly 20 times the average lifespan).
