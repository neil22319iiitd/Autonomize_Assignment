"""
Optional Streamlit Web Interface
Run this for a simple web UI instead of command line

To use:
1. Install streamlit: pip install streamlit
2. Run: streamlit run streamlit_app.py
"""

import streamlit as st
import os
from src.ingest import DocumentIngester
from src.agent import IntelligentFormAgent


# Page configuration
st.set_page_config(
    page_title="Intelligent Form Agent",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #667eea;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="main-header">
    <h1>📄 Intelligent Form Agent</h1>
    <p>Ask questions, get summaries, analyze documents with AI</p>
</div>
""", unsafe_allow_html=True)


# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = None
    st.session_state.documents_loaded = False


# Sidebar for setup
with st.sidebar:
    st.header("⚙️ Setup")
    
    st.info("ℹ️ Make sure Ollama is running locally (no API keys needed)")
    
    # File upload
    st.header("📤 Upload PDFs")
    uploaded_files = st.file_uploader(
        "Upload your PDF documents",
        type=['pdf'],
        accept_multiple_files=True,
        help="Upload invoices, receipts, forms, etc."
    )
    
    # Process button
    if st.button("🚀 Process Documents", disabled=not uploaded_files):
        if uploaded_files:
            with st.spinner("Processing documents..."):
                try:
                    # Save uploaded files temporarily
                    temp_dir = "temp_uploads"
                    os.makedirs(temp_dir, exist_ok=True)
                    
                    for uploaded_file in uploaded_files:
                        file_path = os.path.join(temp_dir, uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                    
                    # Process documents
                    ingester = DocumentIngester()
                    chunks = ingester.process_directory(temp_dir)
                    
                    # Create agent
                    st.session_state.agent = IntelligentFormAgent(chunks)
                    st.session_state.documents_loaded = True
                    
                    st.success(f"✅ Processed {len(uploaded_files)} document(s)!")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please upload documents to process")
    
    # Show loaded documents
    if st.session_state.documents_loaded:
        st.success("✅ Documents Ready")
        if st.button("🔄 Reset"):
            st.session_state.agent = None
            st.session_state.documents_loaded = False
            st.rerun()


# Main content
if not st.session_state.documents_loaded:
    st.info("👈 Upload documents and enter API key in the sidebar to get started")
    
    # Instructions
    with st.expander("📖 How to use"):
        st.markdown("""
        ### Getting Started
        
        1. **Install Ollama**: Download from https://ollama.ai
        2. **Pull a model**: `ollama pull mistral` in your terminal
        3. **Keep Ollama running**: Start it in the background (it stays running)
        4. **Upload PDFs**: Add your documents in the sidebar
        5. **Click Process**: Wait for documents to load
        6. **Ask Questions**: Use the tabs below!
        
        ### What You Can Do
        
        - **Ask Questions**: Get specific information from documents
        - **Summarize**: Get concise summaries of your forms
        - **Analyze**: Get insights across multiple documents
        """)

else:
    # Tabs for different functions
    tab1, tab2, tab3 = st.tabs(["❓ Ask Question", "📝 Summarize", "📊 Analyze"])
    
    # Tab 1: Question Answering
    with tab1:
        st.subheader("Ask a Question About Your Documents")
        
        question = st.text_input(
            "Your question:",
            placeholder="e.g., What is the total amount in invoice_001?",
            key="qa_input"
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            show_sources = st.checkbox("Show sources", value=False)
        
        if st.button("Get Answer", key="qa_button"):
            if question:
                with st.spinner("Thinking..."):
                    try:
                        answer = st.session_state.agent.ask_question(
                            question,
                            show_sources=show_sources
                        )

                        st.markdown("### Answer")
                        st.success(answer)

                        if show_sources:
                            st.markdown("### Sources")
                            retriever = st.session_state.agent.retriever
                            docs = retriever.get_relevant_documents(question)
                            for i, doc in enumerate(docs, 1):
                                with st.expander(f"Source {i}"):
                                    st.write(doc.page_content[:500] + "...")
                    except Exception as e:
                        st.error(f"Error getting answer: {e}")
            else:
                st.warning("Please enter a question")
    
    # Tab 2: Summarization
    with tab2:
        st.subheader("Summarize Documents")
        
        doc_option = st.radio(
            "What to summarize:",
            ["All documents", "Specific document"],
            key="sum_option"
        )
        
        doc_name = None
        if doc_option == "Specific document":
            doc_name = st.text_input(
                "Document name:",
                placeholder="e.g., invoice_001",
                key="sum_input"
            )
        
        if st.button("Generate Summary", key="sum_button"):
            with st.spinner("Generating summary..."):
                if doc_option == "All documents":
                    summary = st.session_state.agent.summarize_document()
                else:
                    if doc_name:
                        summary = st.session_state.agent.summarize_document(doc_name)
                    else:
                        st.warning("Please enter a document name")
                        summary = None
                
                if summary:
                    st.markdown("### Summary")
                    st.info(summary)
    
    # Tab 3: Holistic Analysis
    with tab3:
        st.subheader("Analyze Multiple Documents Together")
        
        st.markdown("""
        Ask questions that require looking at multiple documents:
        - "What is the total spending in January?"
        - "Which invoice has the highest amount?"
        - "How many documents mention 'ABC Corporation'?"
        """)
        
        analysis_question = st.text_input(
            "Your analysis question:",
            placeholder="e.g., What is the total across all invoices?",
            key="analysis_input"
        )
        
        if st.button("Analyze", key="analysis_button"):
            if analysis_question:
                with st.spinner("Analyzing documents..."):
                    analysis = st.session_state.agent.holistic_analysis(
                        analysis_question
                    )
                    
                    st.markdown("### Analysis Result")
                    st.success(analysis)
            else:
                st.warning("Please enter an analysis question")


# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    Built with ❤️ using LangChain, Streamlit, and Ollama (local AI)
</div>
""", unsafe_allow_html=True)
