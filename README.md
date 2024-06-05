# Long-text-summary-using-LLM-Book-Summary-AI tool

# powerful book summarizer using Python, Langchain and GoogleGenerativeAI embeddings.

#### AI models, such as GPT-3 and GPT-4, Google's genai are extremely powerful, but they have limitations. The context window is a significant limitation because it limits the amount of text that the model can consider at any given time. This means that you cannot simply feed an entire book into the model and expect a coherent summary. Furthermore, processing large documents can be expensive. ####



## The Process Simplified
### Here’s how we transform a full-length book into a concise summary:

1. **Splitting & Embeddings:** 
We break down the book into smaller chunks and convert them into embeddings. This step is surprisingly affordable.
1. **Clustering:** Next, we cluster these embeddings to find the most representative sections of the book.
1. **Summarization:** We then summarize these key sections using the more cost-effective gemini-pro model.
1. **Combining Summaries:** Finally, we use GPT-4 to stitch these summaries into one fluid narrative.
By using GPT-4 only in the final step, we manage to keep our costs low.


## Step 1: Load the Book
**First, we need to read the book’s content. We’ll support PDF and EPUB formats.**


## Step 2: Split and Embed the Text

AI models have a token limit, which means they cannot process entire books at once. By breaking up the text into chunks, we ensure that each section is digestible for the AI.

We will divide the text into chunks and convert them into embeddings. Embeddings convert text into a compact numerical form rapidly and with minimal computation, making the process both fast and cost-effective.


## Step 3: Cluster the Embeddings
We use KMeans clustering to group similar chunks. In my version, as shown below, I found that 11 clusters worked well for the majority of books. However, you can make changes based on your needs.

Here, we've divided the entire book into chunks and then embedded them. These embeddings are grouped according to their similarity. For each group, we select the most representative embedding and map it back to the corresponding text chunk.


## Step 4: Summarize the Representative Chunks
We’ll summarize only the selected chunks using GPT-3.5 or gemini-pro


## Step 5: Create the Final Summary
We combine the individual summaries into one final, cohesive summary using GPT-4 or llama3.


## Bringing It All Together
Now, we combine all the steps into a single function that takes an uploaded file and generates a summary.
