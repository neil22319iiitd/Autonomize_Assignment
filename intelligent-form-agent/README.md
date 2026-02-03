# Intelligent Form Agent

## 📋 What Does This Do?

This is an AI-powered system that can:
1. **Read PDF forms** (invoices, receipts, tax forms, etc.)
2. **Answer questions** about the content
3. **Summarize documents** to get key information quickly
4. **Analyze multiple documents** together (e.g., "What's my total spending?")

## 🎯 Key Features

- **Single Form QA**: Ask specific questions about one document
- **Document Summarization**: Get concise summaries highlighting key details
- **Holistic Analysis**: Answer questions across multiple documents
- **100% Local**: Runs on your machine with Ollama — no cloud APIs, no API keys needed

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **LangChain**: Framework for AI workflows
- **Ollama**: Local LLM runtime — runs models locally with no quotas or API keys
- **ChromaDB**: Vector database for fast document search
- **HuggingFace / sentence-transformers**: Embeddings model
- **pypdf**: PDF text extraction

## 📁 Project Structure

```
intelligent-form-agent/
├── data/                    # Put your PDF files here
├── src/                     # Source code
│   ├── __init__.py
│   ├── ingest.py           # Loads and processes PDFs
│   ├── agent.py            # Main AI logic (QA, summarization)
│   └── utils.py            # Helper functions
├── requirements.txt         # Python dependencies
├── .env.example            # Template for API key
├── .gitignore              # Files to ignore in git
├── main.py                 # Run this to start the agent
└── README.md               # This file
```

## 🚀 Setup Instructions (Step-by-Step)

### Step 1: Install Python (if needed)

You mentioned you have Python 3.7. Verify it:
```bash
python --version
```

### Step 2: Download This Project

If you have it as a ZIP, extract it. If on GitHub, clone it:
```bash
git clone <your-repo-url>
cd intelligent-form-agent
```

### Step 3: Create Virtual Environment

Open Command Prompt (Windows) and run:
```bash
python -m venv venv
```

Activate it:
```bash
venv\Scripts\activate
```

You should see `(venv)` in your command prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will take 2-3 minutes. It installs all necessary libraries.

### Step 5: Install and Run Ollama

Ollama lets you run AI models locally on your machine (no cloud APIs, no API keys).

1. **Download Ollama**: https://ollama.ai
2. **Install it** and follow the installer
3. **Pull a model** (e.g., `mistral`):
   ```powershell
   ollama pull mistral
   ```
4. **Keep Ollama running** in the background (start it once, stays running)

### Step 6: Add Your PDF Files

Put your PDF files (invoices, forms, etc.) in the `data/` folder.

For example:
```
data/
├── invoice_001.pdf
├── invoice_002.pdf
└── receipt_jan.pdf
```

### Step 8: Run the Agent!

```bash
python main.py
```

## 💡 How to Use

When you run `python main.py`, you'll see a menu:

```
What would you like to do?
  1. Ask a question about a specific document
  2. Summarize a document
  3. Perform holistic analysis (multiple documents)
  4. List all loaded documents
  5. Exit
```

### Example 1: Ask a Question
```
Choice: 1
Question: What is the total amount in invoice_001?
Answer: The total amount in invoice_001.pdf is $1,250.00
```

### Example 2: Summarize a Document
```
Choice: 2
Document name: invoice_001
Summary: This is an invoice from ABC Company dated January 15, 2024.
It includes 3 line items totaling $1,250.00. Payment is due by February 15, 2024.
```

### Example 3: Holistic Analysis
```
Choice: 3
Question: What is my total spending in January?
Answer: Based on all invoices from January, your total spending is $3,450.00
across 3 invoices.
```

## 📝 Example Queries You Can Try

**Single Document Questions:**
- "What is the invoice number?"
- "When is the due date?"
- "Who is the vendor?"
- "What items are listed?"

**Summarization:**
- Just select option 2 and enter a document name

**Multi-Document Analysis:**
- "What is the total across all invoices?"
- "Which vendor charged the most?"
- "How many invoices are from January?"
- "What's the average invoice amount?"

## 🔧 Troubleshooting

### "No module named X"
```bash
pip install -r requirements.txt
```

### "API Key not found"
Make sure:
1. You created the `.env` file (copy from `.env.example`)
2. You added your actual API key
3. The file is named exactly `.env` (no `.txt` extension)

### "No PDF files found"
Put your PDF files in the `data/` folder.

### "Import Error" or "Version Conflict"
Try upgrading pip first:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🎥 Demo Video

Record a 2-3 minute video showing:
1. Running `python main.py`
2. Asking a question about one document
3. Generating a summary
4. Performing holistic analysis across documents
5. Brief code walkthrough


## 📚 Code Explanation

### How It Works (Simple Overview)

1. **Load PDFs** (`ingest.py`):
   - Reads all PDFs from `data/` folder
   - Breaks them into small chunks (1000 characters each)
   - This helps the AI focus on relevant parts

2. **Create Vector Database** (`agent.py`):
   - Converts text chunks into numbers (embeddings)
   - Stores them in ChromaDB for fast searching
   - When you ask a question, it finds relevant chunks

3. **Answer Questions** (`agent.py`):
   - Takes your question
   - Searches database for relevant text
   - Sends text + question to AI (Gemini)
   - AI reads and answers

4. **Summarize** (`agent.py`):
   - Gathers text from document
   - Asks AI to summarize with specific format
   - Returns concise summary

5. **Holistic Analysis** (`agent.py`):
   - Searches across ALL documents
   - Combines relevant information
   - AI analyzes everything together

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Make sure `streamlit_app.py` is present (it is included)
2. Push to GitHub
3. Deploy at: https://streamlit.io/cloud
   
Note: Streamlit Cloud may not have Ollama pre-installed. For cloud deployment, you may need to containerize or use alternative hosting.

### Option 2: Google Colab
1. Upload notebook version
2. Share Colab link
3. Users can run in browser

### Option 3: Local Only
Just share the GitHub repo link

## 🤝 Contributing

This is an assignment project, but if you want to improve it:
1. Fork the repo
2. Make your changes
3. Submit a pull request

## 📄 License

This project is for educational purposes (ML Intern Assignment).

## 👤 Author

**Your Name**
- Assignment for: Autonomize AI - ML Intern Position
- Date: February 2026

## 🙏 Acknowledgments

- Assignment designed by Autonomize AI
- Built with LangChain framework, Ollama, and HuggingFace embeddings

---

## Quick Start (TL;DR)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install Ollama: https://ollama.ai

# 3. Pull a model
ollama pull mistral

# 4. Add PDFs to data/ folder

# 5. Run
python main.py
```

**That's it! You're ready to go!** 🎉
