"""
Utility functions for the Intelligent Form Agent
Handles API keys, configuration, and helper methods
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


def get_api_key() -> str:
    """
    Get the Google API key from environment variables
    
    Returns:
        str: The API key
        
    Raises:
        ValueError: If API key is not found
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key or api_key == "your_api_key_here":
        raise ValueError(
            "Google API key not found! Please:\n"
            "1. Copy .env.example to .env\n"
            "2. Get a free API key from: https://makersuite.google.com/app/apikey\n"
            "3. Add your key to the .env file"
        )
    
    return api_key


def format_documents_for_display(documents: list) -> str:
    """
    Format a list of documents for nice display
    
    Args:
        documents: List of document objects
        
    Returns:
        str: Formatted string of documents
    """
    output = []
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get('source', 'Unknown')
        page = doc.metadata.get('page', 'Unknown')
        output.append(f"\n--- Source {i} ---")
        output.append(f"File: {os.path.basename(source)}, Page: {page}")
        output.append(f"Content: {doc.page_content[:200]}...")
    
    return "\n".join(output)


def print_separator(title: Optional[str] = None):
    """
    Print a nice separator line
    
    Args:
        title: Optional title to display in the separator
    """
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print(f"\n{'-'*60}\n")


def clean_text(text: str) -> str:
    """
    Clean extracted text from PDFs
    
    Args:
        text: Raw text from PDF
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = " ".join(text.split())
    return text
