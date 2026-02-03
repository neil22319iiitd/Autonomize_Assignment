"""
Intelligent Form Agent - Main Entry Point
Run this file to start the agent
"""

import os
import sys
from src.ingest import DocumentIngester
from src.agent import IntelligentFormAgent
from src.utils import print_separator


def print_welcome():
    """Print welcome message"""
    print("\n" + "="*60)
    print("   INTELLIGENT FORM AGENT")
    print("   Read, Extract, and Explain Documents")
    print("="*60)
    print("\nThis agent can:")
    print("  1. Answer questions about your documents")
    print("  2. Summarize documents")
    print("  3. Analyze multiple documents together")
    print()


def print_menu():
    """Print main menu"""
    print("\n" + "-"*60)
    print("What would you like to do?")
    print("-"*60)
    print("  1. Ask a question about a specific document")
    print("  2. Summarize a document")
    print("  3. Perform holistic analysis (multiple documents)")
    print("  4. List all loaded documents")
    print("  5. Exit")
    print("-"*60)


def main():
    """Main function to run the agent"""
    
    # Print welcome
    print_welcome()
    
    # Define data directory
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    # Check if data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory not found at '{data_dir}'")
        print("\nPlease create a 'data' folder and add your PDF files there.")
        sys.exit(1)
    
    # Check if there are any PDFs
    pdf_files = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"Error: No PDF files found in '{data_dir}'")
        print("\nPlease add some PDF files to the 'data' folder.")
        sys.exit(1)
    
    # Load and process documents
    print_separator("Step 1: Loading Documents")
    ingester = DocumentIngester(chunk_size=1000, chunk_overlap=200)
    chunks = ingester.process_directory(data_dir)
    
    if not chunks:
        print("Failed to load documents. Exiting.")
        sys.exit(1)
    
    # Initialize agent
    print_separator("Step 2: Initializing AI Agent")
    try:
        agent = IntelligentFormAgent(chunks)
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
    
    # Main interaction loop
    print_separator("Step 3: Ready to Answer Questions!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            # Ask a question
            print("\n" + "="*60)
            question = input("Enter your question: ").strip()
            if question:
                agent.ask_question(question, show_sources=True)
            else:
                print("Please enter a valid question.")
        
        elif choice == "2":
            # Summarize document
            print("\n" + "="*60)
            print("Enter document name (or press Enter for all documents):")
            doc_name = input("> ").strip()
            if doc_name:
                agent.summarize_document(doc_name)
            else:
                agent.summarize_document()
        
        elif choice == "3":
            # Holistic analysis
            print("\n" + "="*60)
            question = input("Enter your analysis question: ").strip()
            if question:
                agent.holistic_analysis(question)
            else:
                print("Please enter a valid question.")
        
        elif choice == "4":
            # List documents
            agent.list_documents()
        
        elif choice == "5":
            # Exit
            print("\n" + "="*60)
            print("Thank you for using Intelligent Form Agent!")
            print("="*60 + "\n")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
