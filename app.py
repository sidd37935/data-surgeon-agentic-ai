import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

# Load environment variables (.env file se keys read karne ke liye)
load_dotenv()

# Page Configuration
st.set_page_config(page_title="Data Surgeon Bot", page_icon="👨‍⚕️", layout="wide")

def main():
    st.title("👨‍⚕️ Data Surgeon Insight Bot")
    st.markdown("""
    This bot uses *Agentic AI principles* to perform 'surgery' on your data. 
    It autonomously writes and executes Python/Pandas code in the background using a free Llama-3 model.
    """)

    # File Uploader
    uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

    if uploaded_file is not None:
        # Load data using Pandas
        df = pd.read_csv(uploaded_file)
        
        # UI Layout: Left column me data preview, Right column me query console
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write("### Data Snapshot")
            st.dataframe(df.head(10))
        
        with col2:
            st.write("### Surgeon's Console")
            query = st.text_input("Ask a question about your data (e.g., 'Who is the top performer in MidTerm_Score?')")

            if query:
                # Har nayi query se pehle purane plots ko memory se poori tarah mita dena (Fixes Overlapping Bug)
                plt.clf()
                plt.close('all')
                
                try:
                    # Groq API Key validation check
                    if not os.getenv("GROQ_API_KEY"):
                        st.error("GROQ_API_KEY nahi mili! Please apni .env file check karein.")
                        return

                    # Initialize the Free & Ultra-Fast LLM (Llama 3 8B) via Groq
                    llm = ChatGroq(
                        model="llama-3.3-70b-versatile",
                        temperature=0,
                        groq_api_key=os.getenv("GROQ_API_KEY")
                    )

                    # Create the Agentic Framework
                    agent = create_pandas_dataframe_agent(
    llm, 
    df, 
    verbose=True, 
    allow_dangerous_code=True,   # Learning sandbox environment selection
    handle_parsing_errors=True   # LLM ka output format thoda idhar-udhar ho to bhi crash na ho
)

                    with st.spinner("Analyzing data and generating insights..."):
                        response = agent.run(query)
                        st.success("Analysis Complete")
                        st.write(response)

                        # Secure Logic to check and display visual plots
                        if any(keyword in query.lower() for keyword in ["plot", "chart", "graph", "hist", "scatterplot", "bar"]):
                            fig = plt.gcf()      # Agent ke banaye gaye plot ko pakadna
                            if fig.axes:         # Check karna ki canvas par sach me koi graph bana hai ya khali hai
                                st.pyplot(fig)
                                plt.clf()        # Render karne ke baad turant memory clear karna
                                plt.close('all')
                            else:
                                st.info("The agent processed the query, but no visual chart could be rendered.")
                                
                except Exception as e:
                    st.error(f"An error occurred during surgery: {e}")
                    # Crash hone ke case me bhi safety cleanup
                    plt.clf()
                    plt.close('all')

    else:
        st.info("Please upload a CSV file to begin the surgery.")
if __name__ == "__main__":
    main()