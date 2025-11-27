# AI for Bharat – Week 1  
## Building a Simple Content Summarizer with Amazon Bedrock & Streamlit

This project is my Week-1 hands-on submission for the **AI for Bharat** program.  
It demonstrates how to build a simple **text summarization web app** using **Amazon Bedrock** (Anthropic Claude model) and **Streamlit**.

---

## 1. Problem & Solution

### Problem

Professionals and students regularly work with **long documents, articles, and notes**.  
Reading everything in detail is time-consuming, and it’s hard to quickly:

- Understand the **core message**
- Extract **key points & action items**
- Adapt the summary to a **specific audience** (e.g., manager, customer, student)

### Solution

I built a **Content Summarizer Web App** that:

- Accepts **any text input** (or pasted content from documents / web pages)
- Sends it to **Amazon Bedrock** using the **Converse API**
- Uses **Anthropic Claude** to generate a clear, concise, and structured summary
- Displays the result instantly in a **Streamlit** interface

**Who benefits?**

- Students preparing notes
- Working professionals summarizing reports / meeting notes
- Content creators drafting briefs or social-media summaries
- Anyone who wants a quick, reliable overview of long text

---

## 2. Architecture & AWS Services

### High-Level Architecture

![Architecture Diagram](assets/Architecture.png)  
*(Replace this path with your actual image path, e.g. `images/architecture.png`.)*

### Components

1. **User Interface – Streamlit App**
   - Runs as a simple Python web app.
   - Collects user input text.
   - Shows model response (summary).

2. **Amazon Bedrock Runtime**
   - Exposes the **Converse API** endpoint.
   - Handles authentication, model selection, scaling, and security.

3. **Foundation Model – Anthropic Claude 3.x / 3.5**
   - Performs the actual **summarization task**.
   - Temperature is set low for more **deterministic summaries**.

4. *(Optional)* **Amazon Cloud9 / AWS Workshop Studio**
   - Used as the development environment during the lab.
   - Provides preconfigured AWS credentials and tools.

---

## 3. Technical Implementation

### Tech Stack

- **Python 3**
- **Streamlit** – Frontend framework for the web UI
- **boto3** – AWS SDK for Python, used to call Amazon Bedrock
- **Amazon Bedrock – Converse API**
- **Anthropic Claude model**:  
  `us.anthropic.claude-3-7-sonnet-20250219-v1:0` *(as used in the workshop)*

### Key Flow

1. User enters text in a **Streamlit text area**.
2. On clicking **“Summarize”**, the app calls a helper function in `text_lib.py`.
3. `text_lib.py`:
   - Creates a **boto3 Session**
   - Creates a **Bedrock Runtime client**
   - Builds a `messages` payload for the **Converse API** with the user text
   - Sends the request to the **Claude model**
4. Bedrock returns the **generated summary text**.
5. Streamlit displays the summary on the page.

### Core Code Snippet (Library)

```python
# text_lib.py
import boto3

def get_text_response(input_content):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    message = {
        "role": "user",
        "content": [ { "text": input_content } ]
    }
    
    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    return response['output']['message']['content'][0]['text']
