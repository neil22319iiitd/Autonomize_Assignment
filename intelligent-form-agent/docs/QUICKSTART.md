# 🚀 QUICK START GUIDE

## For Complete Beginners

This guide will help you run the Intelligent Form Agent in 10 minutes!

---

## Step-by-Step Instructions

### 1️⃣ Open Command Prompt
- Press `Windows Key + R`
- Type `cmd` and press Enter

### 2️⃣ Navigate to Project Folder
```bash
cd path\to\intelligent-form-agent
```
(Replace `path\to\` with where you saved the folder)

### 3️⃣ Create Virtual Environment
```bash
python -m venv venv
```
Wait for it to finish (30 seconds)

### 4️⃣ Activate Virtual Environment
```bash
venv\Scripts\activate
```
You should see `(venv)` appear before your command prompt

### 5️⃣ Install All Required Packages
```bash
pip install -r requirements.txt
```
This takes 2-3 minutes. Wait for it to complete.

### 6️⃣ Install Ollama

1. Download from: https://ollama.ai
2. Install and run it
3. Pull a model:
   ```powershell
   ollama pull mistral
   ```

### 7️⃣ Add Your PDF Files

1. Open the `data` folder
2. Copy your PDF files (invoices, receipts, etc.) into it
3. You can add as many as you want

### 8️⃣ Test Your Setup (Optional but Recommended)
```bash
python test_setup.py
```

This will check if everything is installed correctly.

### 🔟 Run the Agent!

```powershell
python main.py
```

---

## What You'll See

```
============================================================
   INTELLIGENT FORM AGENT
   Read, Extract, and Explain Documents
============================================================

This agent can:
  1. Answer questions about your documents
  2. Summarize documents
  3. Analyze multiple documents together

[Loading documents...]
[Initializing AI...]

What would you like to do?
------------------------------------------------------------
  1. Ask a question about a specific document
  2. Summarize a document
  3. Perform holistic analysis (multiple documents)
  4. List all loaded documents
  5. Exit
------------------------------------------------------------

Enter your choice (1-5):
```

---

## Common Issues & Solutions

### Issue: "python is not recognized"
**Solution:** Python not installed or not in PATH. Install Python 3.8+ from python.org

### Issue: "No module named X"
**Solution:** Run `pip install -r requirements.txt` again

### Issue: "No PDF files found"
**Solution:** Add PDF files to the `data/` folder

### Issue: "Ollama not running"
**Solution:** Start Ollama from your applications or run `ollama serve` in terminal

---

## Quick Test Example

After running `python main.py`:

1. **Choose option 1** (Ask a question)
2. Type: `What documents do I have?`
3. Press Enter
4. You should see a list of your documents!

Try option 2 to summarize a document, or option 3 for multi-document analysis.

---

## Need Help?

1. Run `python test_setup.py` to diagnose issues
2. Check README.md for detailed troubleshooting
3. Make sure all files are in correct locations
4. Verify your API key is valid

---

## What to Submit

For your assignment:

1. **GitHub Repository**: Push all your code
2. **README.md**: Already included!
3. **Screen Recording**: Record yourself:
   - Running `python main.py`
   - Asking a question (option 1)
   - Getting a summary (option 2)
   - Doing holistic analysis (option 3)
   - Quick code walkthrough

Use OBS Studio or Windows Game Bar (Win+G) to record.

---

## You're All Set! 🎉

If everything works, you're ready to complete your assignment!
