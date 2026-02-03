"""
Intelligent Form Agent - Main AI Logic
Handles QA, Summarization, and Multi-Document Analysis
"""

from typing import List, Optional
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from src.utils import print_separator, format_documents_for_display


class IntelligentFormAgent:
    """
    Main agent that can answer questions and summarize documents
    """
    
    def __init__(self, chunks: List[Document]):
        """
        Initialize the agent with document chunks
        
        Args:
            chunks: List of document chunks from the ingester
        """
        print_separator("Initializing Intelligent Form Agent")
        
        # Store chunks
        self.chunks = chunks
        
        # Initialize embeddings (using free HuggingFace embeddings)
        print("Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("  ✓ Embeddings loaded")
        
        # Create vector store
        print("Creating vector database...")
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            collection_name="form_documents"
        )
        print("  ✓ Vector database created")
        
        # Initialize LLM (using local Ollama - no API costs or quotas)
        print("Connecting to Local AI (Ollama)...")
        self.llm = Ollama(
            model="mistral",
            temperature=0.3
        )
        print("  ✓ AI model ready")
        
        # Create retriever
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 4}  # Return top 4 relevant chunks
        )
        
        # Setup QA chain
        self._setup_qa_chain()
        
        print("\n✓ Agent initialized successfully!")
    
    def _setup_qa_chain(self):
        """
        Setup the Question-Answering chain with custom prompt
        """
        # Custom prompt template for better answers
        qa_template = """You are an intelligent assistant helping users understand form documents like invoices, receipts, and tax forms.

Use the following context to answer the question. If you don't know the answer, say "I don't have enough information to answer that."

Context from documents:
{context}

Question: {question}

Answer (be specific and cite values when possible):"""

        QA_PROMPT = PromptTemplate(
            template=qa_template,
            input_variables=["context", "question"]
        )
        
        # Create the QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_PROMPT}
        )
    
    def ask_question(self, question: str, show_sources: bool = False) -> str:
        """
        Answer a question about the documents
        
        Args:
            question: The question to answer
            show_sources: Whether to show source documents
            
        Returns:
            str: The answer
        """
        print_separator(f"Question: {question}")
        
        try:
            # Run the QA chain
            result = self.qa_chain({"query": question})
            
            answer = result["result"]
            print(f"Answer: {answer}")
            
            # Optionally show sources
            if show_sources and "source_documents" in result:
                print("\n--- Sources Used ---")
                print(format_documents_for_display(result["source_documents"]))
            
            return answer
            
        except Exception as e:
            error_msg = f"Error answering question: {e}"
            print(error_msg)
            return error_msg
    
    def summarize_document(self, document_name: Optional[str] = None) -> str:
        """
        Generate a summary of a document or all documents
        
        Args:
            document_name: Optional name of specific document to summarize
            
        Returns:
            str: The summary
        """
        if document_name:
            print_separator(f"Summarizing: {document_name}")
            
            # Filter chunks for specific document
            relevant_chunks = [
                chunk for chunk in self.chunks 
                if document_name.lower() in chunk.metadata.get('source', '').lower()
            ]
            
            if not relevant_chunks:
                return f"No document found matching '{document_name}'"
            
            # Combine text from relevant chunks
            combined_text = "\n\n".join([chunk.page_content for chunk in relevant_chunks[:5]])
            
        else:
            print_separator("Summarizing All Documents")
            
            # Use first few chunks from all documents
            combined_text = "\n\n".join([chunk.page_content for chunk in self.chunks[:8]])
        
        # Create summary prompt
        summary_prompt = f"""Please provide a concise summary of the following form document(s). 
Include key information such as:
- Document type
- Important dates
- Key entities (names, companies)
- Important amounts or values
- Main purpose or content

Document content:
{combined_text}

Summary:"""
        
        try:
            # Get summary from LLM
            summary = self.llm.predict(summary_prompt)
            print(f"\nSummary:\n{summary}")
            return summary
            
        except Exception as e:
            error_msg = f"Error generating summary: {e}"
            print(error_msg)
            return error_msg
    
    def holistic_analysis(self, question: str) -> str:
        """
        Perform analysis across multiple documents
        
        Args:
            question: Question requiring multi-document analysis
            
        Returns:
            str: The analysis result
        """
        print_separator(f"Holistic Analysis: {question}")
        
        # Retrieve relevant chunks from all documents
        relevant_docs = self.retriever.get_relevant_documents(question)
        
        # Combine context from multiple documents
        combined_context = "\n\n".join([doc.page_content for doc in relevant_docs])
        
        # Create analysis prompt
        analysis_prompt = f"""You are analyzing multiple form documents together to answer a comprehensive question.

Context from multiple documents:
{combined_context}

Question: {question}

Provide a detailed answer that synthesizes information across all documents. Include specific values and calculations if needed.

Answer:"""
        
        try:
            # Get analysis from LLM
            analysis = self.llm.predict(analysis_prompt)
            print(f"\nAnalysis:\n{analysis}")
            return analysis
            
        except Exception as e:
            error_msg = f"Error performing analysis: {e}"
            print(error_msg)
            return error_msg
    
    def list_documents(self):
        """
        List all loaded documents
        """
        print_separator("Loaded Documents")
        
        # Get unique document sources
        sources = set()
        for chunk in self.chunks:
            source = chunk.metadata.get('source', 'Unknown')
            sources.add(source)
        
        print("Available documents:")
        for i, source in enumerate(sorted(sources), 1):
            import os
            print(f"  {i}. {os.path.basename(source)}")
        
        print(f"\nTotal: {len(sources)} document(s)")


# Example usage
if __name__ == "__main__":
    from src.ingest import DocumentIngester
    import os
    
    # Load documents
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    ingester = DocumentIngester()
    chunks = ingester.process_directory(data_dir)
    
    if chunks:
        # Create agent
        agent = IntelligentFormAgent(chunks)
        
        # Test questions
        agent.ask_question("What documents do we have?")
        agent.summarize_document()
