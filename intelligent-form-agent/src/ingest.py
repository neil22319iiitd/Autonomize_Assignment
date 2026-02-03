"""
Document Ingestion Module
Handles loading PDFs and preparing them for the AI system
"""

import os
from typing import List
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from src.utils import print_separator, clean_text


class DocumentIngester:
    """
    Loads PDF documents and splits them into chunks for processing
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the document ingester
        
        Args:
            chunk_size: Size of each text chunk (default: 1000 characters)
            chunk_overlap: Overlap between chunks (default: 200 characters)
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Create text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def load_pdf(self, file_path: str) -> List[Document]:
        """
        Load a single PDF file
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            List of Document objects
        """
        print(f"Loading PDF: {os.path.basename(file_path)}")
        
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            print(f"  ✓ Loaded {len(documents)} pages")
            return documents
        except Exception as e:
            print(f"  ✗ Error loading PDF: {e}")
            return []
    
    def load_directory(self, directory_path: str) -> List[Document]:
        """
        Load all PDF files from a directory
        
        Args:
            directory_path: Path to directory containing PDFs
            
        Returns:
            List of all loaded documents
        """
        print_separator("Loading Documents")
        
        all_documents = []
        
        # Check if directory exists
        if not os.path.exists(directory_path):
            print(f"Error: Directory '{directory_path}' not found!")
            return all_documents
        
        # Find all PDF files
        pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in '{directory_path}'")
            return all_documents
        
        print(f"Found {len(pdf_files)} PDF file(s)\n")
        
        # Load each PDF
        for pdf_file in pdf_files:
            file_path = os.path.join(directory_path, pdf_file)
            documents = self.load_pdf(file_path)
            all_documents.extend(documents)
        
        print(f"\nTotal: {len(all_documents)} pages loaded from {len(pdf_files)} file(s)")
        return all_documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks
        
        Args:
            documents: List of documents to split
            
        Returns:
            List of document chunks
        """
        print_separator("Splitting Documents into Chunks")
        
        chunks = self.text_splitter.split_documents(documents)
        
        print(f"Created {len(chunks)} chunks from {len(documents)} pages")
        print(f"Chunk size: {self.chunk_size} characters")
        print(f"Chunk overlap: {self.chunk_overlap} characters")
        
        return chunks
    
    def process_directory(self, directory_path: str) -> List[Document]:
        """
        Complete pipeline: Load directory and split into chunks
        
        Args:
            directory_path: Path to directory containing PDFs
            
        Returns:
            List of processed document chunks
        """
        # Load all documents
        documents = self.load_directory(directory_path)
        
        if not documents:
            print("No documents to process!")
            return []
        
        # Split into chunks
        chunks = self.split_documents(documents)
        
        return chunks


# Example usage and testing
if __name__ == "__main__":
    # Test the ingester
    ingester = DocumentIngester()
    
    # Try to load from data directory
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    chunks = ingester.process_directory(data_dir)
    
    if chunks:
        print_separator("Sample Chunk")
        print(f"First chunk preview:\n{chunks[0].page_content[:300]}...")
