# Complete Guide for Non-Programmers
## How to Run the Intelligent Form Agent

This guide is written for someone who has **never coded before**. Follow these steps exactly.

---

## 🎯 What This Program Does

Imagine you have 100 invoices and receipts. You need to:
- Find the total amount from invoice #45
- See what all January invoices added up to
- Get a quick summary of each invoice

**Instead of opening each PDF manually**, this program:
1. Reads all your PDFs
2. Understands what's in them
3. Answers your questions instantly

---

## 📋 What You Need

1. **A Windows computer** (Windows 10 or 11 recommended)
2. **Python installed** (version 3.8 or higher recommended)
3. **Internet connection** (to download libraries and models)
4. **PDF files** (your invoices, forms, receipts, etc.)
5. **Ollama installed** (free local AI — runs on your machine)

---

## 🔧 Part 1: Installing Python (If You Don't Have It)

### Check if Python is Already Installed

1. Press `Windows Key + R` on your keyboard
2. Type `cmd` and press Enter
3. In the black window that opens, type: `python --version`
4. Press Enter

**If you see:** `Python 3.8.x` or higher → **Great! Skip to Part 2**

**If you see:** `'python' is not recognized` → **Follow these steps:**

### Installing Python

1. Go to: https://www.python.org/downloads/
2. Click the big yellow button "Download Python 3.x.x"
3. Run the downloaded file
4. **IMPORTANT:** Check the box "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete
7. Close and reopen Command Prompt
8. Test again: `python --version`

---

## 📦 Part 2: Getting the Code

### Option A: If You Have GitHub Link
1. **A Windows computer** (Windows 10 or 11 recommended)
2. **Python installed** (version 3.8 or higher recommended)
3. **Internet connection** (to download libraries and models)
4. **PDF files** (your invoices, forms, receipts, etc.)
5. **Optional: Google account / API key** (only if you plan to use cloud LLMs)
5. Right-click the ZIP file → "Extract All"
6. Open the extracted folder
### Step 5: (Optional) Cloud API Key

The program can use cloud LLMs (Google Gemini) but the recommended setup for development is to run local models with Ollama (no API keys or quotas). If you want to use a cloud model, follow these steps to get an API key:
### Option B: If You Have the Folder

1. Make sure the folder is on your Desktop or Documents
2. Remember where it is!

---

## 💻 Part 3: Setting Up the Program

### Step 6: Add Your API Key (Optional)

If you will use a cloud model, add the key to a `.env` file in the project root. If you use local Ollama models, this step is not required.
### Step 2: Create a Virtual Environment
1. Copy `.env.example` to `.env` or create a new `.env` file
2. Add:
   ```text
   GOOGLE_API_KEY=your_google_api_key_here
   ```
3. Save the file. Keep `.env` private (don't commit to Git).

A virtual environment keeps this project's libraries separate from other projects.

**In Command Prompt, type:**
```
python -m venv venv
```

Press Enter and wait 20-30 seconds.

**What this does:** Creates a folder called `venv` with a clean Python environment.

---

Local (recommended): make sure Ollama is running or models are available locally, then:
### Step 3: Activate the Virtual Environment

**Type this exactly:**
python main.py
venv\Scripts\activate
```

Press Enter.

**You should see:** `(venv)` appear at the start of your command line

**Example:**
```
C:\Users\YourName\Desktop\intelligent-form-agent> venv\Scripts\activate
(venv) C:\Users\YourName\Desktop\intelligent-form-agent>
```

If you see `(venv)`, you're good! If not, try again.

---

### Step 4: Install Required Libraries

**Type:**
```
pip install -r requirements.txt
```

Press Enter and **wait 2-5 minutes**. You'll see lots of text scrolling.

**What this does:** Downloads and installs all the necessary libraries (like LangChain, ChromaDB, etc.)

**When it's done:** You'll see your command prompt again.

---

### Step 5: Install Ollama

Ollama lets you run AI models locally on your machine (no API keys, no quotas, completely free).

1. **Download Ollama** from: https://ollama.ai
2. **Install it** and follow the installer
3. **In Command Prompt, pull a model** (e.g., `mistral`):
   ```powershell
   ollama pull mistral
   ```
4. **Keep Ollama running** in the background (start it once, stays running)

### Step 6: Add Your PDF Files

1. Open the project folder
2. Find the folder called **`data`**
3. Copy your PDF files (invoices, receipts, etc.) into this folder
4. You can add as many as you want

**Note:** The program comes with 3 sample invoices already, so you can test it first!

---

## 🚀 Part 4: Running the Program

### Test Your Setup First (Optional but Recommended)

**In Command Prompt (with venv activated), type:**
```
python test_setup.py
```

This checks if everything is installed correctly.

**You should see:**
- ✓ Python version OK
- ✓ All packages installed
- ✓ PDF files found

**If you see ✗ for anything:** Go back and fix that step.

---

### Run the Main Program

**In Command Prompt, type:**
```
python main.py
```

Press Enter.

**The AI (via local Ollama) will initialize and you'll see the interactive menu.**

---

## 🎮 Part 5: Using the Program

### Example 1: Ask a Question

1. Type `1` and press Enter
2. It asks: "Enter your question:"
3. Type: `What is the total amount in invoice_001?`
4. Press Enter
5. **The AI reads the invoice and answers!**

**Try these questions:**
- "What's the invoice number?"
- "When is the due date?"
- "What items are listed?"
- "Who is the customer?"

---

### Example 2: Summarize a Document

1. Type `2` and press Enter
2. It asks: "Enter document name:"
3. Type: `invoice_001` (or press Enter for all documents)
4. Press Enter
5. **You get a nice summary!**

**Example output:**
```
Summary:
This is an invoice (INV-001) from ABC Corporation dated January 15, 2024.
It's addressed to Customer XYZ and includes 3 items:
- Consulting Services ($800)
- Software License ($300)
- Support Package ($150)
Total amount: $1,250.00
Payment is due within 30 days.
```

---

### Example 3: Analyze Multiple Documents

1. Type `3` and press Enter
2. It asks: "Enter your analysis question:"
3. Type: `What is the total spending in January?`
4. Press Enter
5. **The AI looks at ALL January invoices and calculates!**

**Try these questions:**
- "How many invoices are from January?"
- "What's the average invoice amount?"
- "Which invoice has the highest total?"

---

### Example 4: List Your Documents

1. Type `4` and press Enter
2. **See all your loaded PDFs**

---

### Exiting the Program

- Type `5` and press Enter
- Or press `Ctrl + C` anytime

---

## 🎥 Part 6: Recording Your Demo Video

You need to record yourself using the program.

### Using Windows Game Bar (Built-in)

1. Run the program: `python main.py`
2. Press **Windows Key + G**
3. Click the **Record button** (circle)
4. Use the program:
   - Ask a question
   - Get a summary
   - Do holistic analysis
5. Press **Windows Key + G** again
6. Click **Stop**
7. Video saves to: `C:\Users\YourName\Videos\Captures`

### What to Show in Video (2-3 minutes)

1. Opening Command Prompt
2. Running `python main.py`
3. Choosing option 1 and asking a question
4. Choosing option 2 and getting a summary
5. Choosing option 3 and analyzing multiple documents
6. Briefly showing your code folder structure

---

## 📤 Part 7: Submitting Your Assignment

### 1. Upload to GitHub

**If you don't have GitHub:**
1. Go to: https://github.com
2. Click "Sign up"
3. Create account

**Upload your code:**
1. Go to: https://github.com/new
2. Name: `intelligent-form-agent`
3. Click "Create repository"
4. Click "uploading an existing file"
5. Drag your entire project folder
6. Click "Commit changes"
7. Copy the repository URL

### 2. Upload Your Video

1. Upload to Google Drive or YouTube (unlisted)
2. Get the shareable link

### 3. Submit Everything

Send:
- GitHub repository link
- Video link
- Brief description of what you built

---

## ❓ Troubleshooting

### "python is not recognized"
**Fix:** Install Python (see Part 1)

### "pip is not recognized"
**Fix:** Reinstall Python, check "Add to PATH"

### "No module named X"
**Fix:** Run `pip install -r requirements.txt` again

### "API Key not found"
**Fix:** 
1. Check `.env` file exists (not `.env.txt`)
2. Check you pasted your actual API key
3. Make sure file is in root folder (same location as main.py)

### ".env.txt" instead of ".env"
**Fix:**
1. Open Command Prompt in project folder
2. Type: `ren .env.txt .env`
3. Press Enter

### "No PDF files found"
**Fix:** Add PDF files to the `data/` folder

### Program freezes or crashes
**Fix:** 
1. Press `Ctrl + C` to stop
2. Run again: `python main.py`

### Can't see (venv) in Command Prompt
**Fix:**
1. Close Command Prompt
2. Open new one in project folder
3. Run: `venv\Scripts\activate` again

---

## 💡 Tips for Success

1. **Read error messages** - they tell you what's wrong
2. **Google errors** - copy/paste error message into Google
3. **Make sure venv is activated** - look for `(venv)` in command prompt
4. **Use sample PDFs first** - test with the included invoices before your own
5. **Keep Ollama running** - Ollama needs to be active in the background

---

## 🎓 Understanding What You Built

**In simple terms:**

1. **PDFs → Text**: Your PDFs are converted to readable text
2. **Text → Chunks**: Long text is broken into small pieces
3. **Chunks → Database**: Pieces are stored in a searchable database
4. **Question → Search**: When you ask a question, it searches the database
5. **Search → AI**: Relevant pieces are sent to your local AI (Ollama)
6. **AI → Answer**: AI reads and answers your question

**All this happens on YOUR machine — nothing sent to the cloud!**

---

## 🎉 You Did It!

If you followed all steps:
- ✓ Program runs
- ✓ Can ask questions
- ✓ Gets answers
- ✓ Have demo video

**You're ready to submit!**

Need help? Check:
1. README.md for technical details
2. QUICKSTART.md for condensed steps
3. HOW_IT_WORKS.md to understand the code

---

## 📚 Next Steps (Optional)

Want to improve your project?

1. **Add more PDFs** - invoices, receipts, tax forms
2. **Try different questions** - experiment!
3. **Try different models** - `ollama pull llama2`, `ollama pull neural-chat`
4. **Add a web interface** - use Streamlit (advanced)

**Good luck with your assignment!** 🚀
