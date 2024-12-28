import streamlit as st
from agents import AgentSystem

def init_session_state():
    if 'agent_system' not in st.session_state:
        st.session_state.agent_system = AgentSystem()

def main():
    st.set_page_config(page_title="Financial Analysis Assistant", layout="wide")
    
    init_session_state()
    
    st.title("Financial Analysis Assistant")
    
    # Sidebar for input selection
    with st.sidebar:
        analysis_type = st.radio(
            "Select Analysis Type",
            ["Stock Analysis", "Market News"]
        )
    
    if analysis_type == "Stock Analysis":
        ticker = st.text_input("Enter Stock Ticker:", "NVDA").upper()
        
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                response = st.session_state.agent_system.get_stock_analysis(ticker)
                
                # Display analysis
                st.markdown(response.content)
                
                # Display sources
                with st.expander("Sources"):
                    for source in response.sources:
                        st.write(source)
                
                # Display tool calls for debugging
                with st.expander("Debug Info"):
                    st.json(response.tool_calls)
    
    else:  # Market News
        topic = st.text_input("Enter Market Topic:", "AI Semiconductor Industry")
        
        if st.button("Get Analysis"):
            with st.spinner("Analyzing..."):
                response = st.session_state.agent_system.get_market_news(topic)
                
                st.markdown(response.content)
                
                with st.expander("Sources"):
                    for source in response.sources:
                        st.write(source)

if __name__ == "__main__":
    main()