# Long-text-summary-using-LLM-Book-Summary-AI tool

# powerful book summarizer using Python, Langchain and OpenAI embeddings.

#### AI models, such as GPT-3 and GPT-4, are extremely powerful, but they have limitations. The context window is a significant limitation because it limits the amount of text that the model can consider at any given time. This means that you cannot simply feed an entire book into the model and expect a coherent summary. Furthermore, processing large documents can be expensive. ####



## The Process Simplified
### Here’s how we transform a full-length book into a concise summary:

1. **Splitting & Embeddings:** 
We break down the book into smaller chunks and convert them into embeddings. This step is surprisingly affordable.
1. **Clustering:** Next, we cluster these embeddings to find the most representative sections of the book.
1. **Summarization:** We then summarize these key sections using the more cost-effective GPT-3.5 model.
1. **Combining Summaries:** Finally, we use GPT-4 to stitch these summaries into one fluid narrative.
By using GPT-4 only in the final step, we manage to keep our costs low.
