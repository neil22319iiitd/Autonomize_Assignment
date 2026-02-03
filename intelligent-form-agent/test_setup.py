"""
Test Script - Verify Your Setup
Run this to check if everything is installed correctly
"""

import sys

def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    print(f"  Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 7:
        print("  ✓ Python version OK")
        return True
    else:
        print("  ✗ Need Python 3.7 or higher")
        return False

def check_imports():
    """Check if all required packages are installed"""
    print("\nChecking installed packages...")
    
    packages = [
        ("langchain", "LangChain"),
        ("chromadb", "ChromaDB"),
        ("pypdf", "PyPDF"),
        ("google.generativeai", "Google Generative AI"),
        ("sentence_transformers", "Sentence Transformers"),
        ("dotenv", "Python Dotenv"),
    ]
    
    all_good = True
    
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✓ {name} installed")
        except ImportError:
            print(f"  ✗ {name} NOT installed")
            all_good = False
    
    return all_good

def check_env_file():
    """Check if .env file exists"""
    import os
    print("\nChecking .env file...")
    
    if os.path.exists(".env"):
        print("  ✓ .env file exists")
        
        # Check if API key is set
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if api_key and api_key != "your_api_key_here":
            print("  ✓ API key is set")
            return True
        else:
            print("  ✗ API key not configured")
            print("    Please add your Google API key to .env file")
            return False
    else:
        print("  ✗ .env file not found")
        print("    Copy .env.example to .env and add your API key")
        return False

def check_data_folder():
    """Check if data folder exists and has PDFs"""
    import os
    print("\nChecking data folder...")
    
    if not os.path.exists("data"):
        print("  ✗ data/ folder not found")
        print("    Create a 'data' folder and add your PDF files")
        return False
    
    print("  ✓ data/ folder exists")
    
    pdf_files = [f for f in os.listdir("data") if f.endswith('.pdf')]
    
    if pdf_files:
        print(f"  ✓ Found {len(pdf_files)} PDF file(s):")
        for pdf in pdf_files[:5]:  # Show first 5
            print(f"    - {pdf}")
        if len(pdf_files) > 5:
            print(f"    ... and {len(pdf_files) - 5} more")
        return True
    else:
        print("  ✗ No PDF files found in data/ folder")
        print("    Add some PDF files to test the agent")
        return False

def main():
    """Run all checks"""
    print("="*60)
    print("  INTELLIGENT FORM AGENT - Setup Verification")
    print("="*60)
    
    checks = [
        check_python_version(),
        check_imports(),
        check_env_file(),
        check_data_folder(),
    ]
    
    print("\n" + "="*60)
    if all(checks):
        print("  ✓✓✓ ALL CHECKS PASSED! ✓✓✓")
        print("  You're ready to run: python main.py")
    else:
        print("  ✗ Some checks failed")
        print("  Please fix the issues above before running main.py")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
