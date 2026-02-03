# How the Code Works - Simple Explanation

This document explains how the Intelligent Form Agent works in simple terms.

---

## 🎯 The Big Picture

Imagine you have a smart assistant that can:
1. Read your documents
2. Remember what it read
3. Answer questions about them

That's exactly what this code does!

---

## 📚 The Main Components

### 1. **Document Ingester** (`ingest.py`)

**What it does:** Reads PDF files and breaks them into chunks

**Why chunks?** 
- AI models can't process entire books at once
- Smaller chunks = faster searching
- We use 1000-character chunks with 200-character overlap

**Code Flow:**
```
PDF Files → Load Each Page → Split into Chunks → Return Chunks
```

**Key Functions:**
- `load_pdf()` - Opens one PDF file
- `load_directory()` - Opens all PDFs in a folder
- `split_documents()` - Breaks text into chunks
- `process_directory()` - Does everything above

---

### 2. **Vector Store** (Part of `agent.py`)

**What it does:** Creates a searchable database of your documents

**How it works:**
1. Takes text chunks
2. Converts them to numbers (embeddings) using AI
3. Stores them in ChromaDB
4. When you ask a question, finds relevant chunks

**Think of it like:**
- Google search, but for your documents
- Instead of searching words, it searches meanings
- "invoice total" finds chunks about money/totals even if exact words differ

---

### 3. **The Agent** (`agent.py`)

**What it does:** The brain of the system - answers questions and summarizes

**Three Main Skills:**

#### a) Question Answering (`ask_question()`)
```
Your Question → Find Relevant Chunks → Send to AI → Get Answer
```

Example:
- You ask: "What's the total on invoice_001?"
- System finds chunks mentioning "invoice_001" and "total"
- Sends these chunks to AI
- AI reads and answers: "$1,250.00"

#### b) Summarization (`summarize_document()`)
```
Document Name → Get All Chunks → Ask AI to Summarize → Get Summary
```

Example:
- You want to summarize "invoice_001.pdf"
- System gets all text from that file
- Asks AI: "Summarize this, include key dates, amounts, etc."
- AI returns: "Invoice from ABC Corp, dated Jan 15, total $1,250..."

#### c) Holistic Analysis (`holistic_analysis()`)
```
Broad Question → Search ALL Documents → Combine Info → AI Analyzes → Answer
```

Example:
- You ask: "What's my total spending in January?"
- System searches ALL documents for January-related content
- Combines information from multiple invoices
- AI calculates: "Total: $3,450 across 3 invoices"

---

## 🔧 How It All Connects

### The Workflow:

```
1. START
   ↓
2. User runs main.py
   ↓
3. Load PDFs from data/ folder
   ↓
4. Break into chunks (ingest.py)
   ↓
5. Create vector database (agent.py)
   ↓
6. Show menu to user
   ↓
7. User chooses action (QA, Summary, or Analysis)
   ↓
8. Agent processes and calls AI
   ↓
9. Display result
   ↓
10. Repeat from step 6 (or exit)
```

---

## 🤖 The AI Components

### 1. **Embeddings Model** (HuggingFace)
- **Purpose:** Convert text to numbers
- **Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Why:** Free, fast, good quality
- **Size:** ~80MB download

### 2. **Language Model**
- **Purpose:** Understand and answer questions
- **Model:** Ollama local models (e.g., Mistral)
- **Why:** No API keys, no quotas, completely free, runs on your machine
- **Privacy:** All data stays on your computer — nothing sent to cloud

---

## 💾 Data Flow Example

Let's trace a question through the system:

**Question:** "What's the invoice number?"

```
1. USER: Types "What's the invoice number?"
   ↓
2. RETRIEVER: Searches vector DB for relevant chunks
   → Finds: "Invoice #12345, Date: Jan 15, Amount: $500"
   ↓
3. PROMPT BUILDER: Creates this:
   "Context: [chunk text]
    Question: What's the invoice number?
    Answer: "
   ↓
4. OLLAMA (Local AI): Reads context + question
   → Generates: "The invoice number is #12345"
   ↓
5. USER: Sees answer on screen
```

---

## 🔑 Key Technologies Explained

### LangChain
- **What:** Framework for building AI apps
- **Why:** Makes connecting AI models easy
- **Does:** Handles the complex parts (prompts, chains, memory)

### ChromaDB
- **What:** Vector database
- **Why:** Fast similarity search
- **Does:** Stores and retrieves document chunks

### PyPDF
- **What:** PDF reading library
- **Why:** Extracts text from PDFs
- **Does:** Opens PDFs and gets text

---

## 🎨 Code Organization

```
main.py              → Entry point, user interface
    ↓
ingest.py            → Load and chunk documents
    ↓
agent.py             → AI logic (QA, summarize, analyze)
    ↓
utils.py             → Helper functions (API keys, formatting)
```

---

## 🔐 Environment Variables (.env)

**The `.env` file is not needed** if you're using local Ollama models. All data stays on your machine — no cloud APIs required.

If you only use local models, you can delete the `.env` file entirely.

---

## 🚀 Performance Tips

### Speed Optimizations:
1. **Chunk size:** Bigger = fewer chunks but slower search
2. **Retriever k:** How many chunks to retrieve (default: 4)
3. **Embeddings:** Cached after first run (faster next time)

### Memory Usage:
- Small docs: ~200MB RAM
- Large docs: ~500MB RAM
- Vector DB: Stored on disk

---

## 🐛 Common Issues Explained

### "Import Error"
**Cause:** Package not installed
**Fix:** `pip install -r requirements.txt`

### "API Key not found"
**Cause:** .env file missing or wrong
**Fix:** Create .env with your key

### "No documents found"
**Cause:** data/ folder empty
**Fix:** Add PDF files to data/

### "Connection error"
**Cause:** No internet or API issue
**Fix:** Check internet, verify API key

---

## 🎓 Learning Points

If you're explaining this in an interview:

1. **RAG (Retrieval-Augmented Generation)**
   - Combines search + AI
   - AI gets context before answering
   - More accurate than pure AI

2. **Vector Embeddings**
   - Text → Numbers
   - Similar meanings → Similar numbers
   - Enables semantic search

3. **Chunking Strategy**
   - Balance between context and granularity
   - Overlap prevents information loss
   - Size depends on document type

4. **Prompt Engineering**
   - How we ask AI matters
   - Clear instructions = better answers
   - Include examples in prompts

---

## 📝 Customization Ideas

Want to extend this? Ideas:

1. **Add more document types**
   - Images (with OCR)
   - Excel files
   - Word docs

2. **Structured extraction**
   - Force JSON output
   - Extract specific fields

3. **Web UI**
   - Add Streamlit interface
   - Drag-and-drop upload

4. **Better memory**
   - Conversation history
   - Context from previous questions

---

## 🎬 Summary

**In one sentence:**
We load PDFs, chunk them, store in a searchable database, and use AI to answer questions by retrieving relevant chunks.

**That's it!** Simple concept, powerful results.
