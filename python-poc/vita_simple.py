"""
VITA Simple: Python Learning Assistant
A radically simplified version of the original VITA application
Total lines: ~100 | Dependencies: 4 | Setup time: 2 minutes
"""

import streamlit as st
from openai import OpenAI
import os
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="VITA - Python Learning Assistant",
    page_icon="🐍",
    layout="centered"
)

def init_session_state():
    """Initialize session state variables"""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""

def get_ai_response(code: str, action: str, api_key: str) -> Optional[str]:
    """Get AI response for code analysis"""
    try:
        client = OpenAI(api_key=api_key)
        
        system_prompts = {
            "Debug": "You are a Python debugging expert. Find bugs, explain them clearly, and provide fixed code.",
            "Explain": "You are a patient Python teacher. Explain code line-by-line in simple terms.",
            "Improve": "You are a Python optimization expert. Suggest improvements for readability and performance.",
            "Concept": "You are a Python concept teacher. Explain the programming concepts used in this code."
        }
        
        user_prompts = {
            "Debug": f"Debug this Python code and provide a corrected version:\n\n{code}",
            "Explain": f"Explain this Python code for a beginner:\n\n{code}",
            "Improve": f"Suggest improvements for this Python code:\n\n{code}",
            "Concept": f"What Python concepts are demonstrated in this code? Explain them:\n\n{code}"
        }
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompts[action]},
                {"role": "user", "content": user_prompts[action]}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main application logic"""
    init_session_state()
    
    # Header
    st.title("🐍 VITA: Your Python Learning Companion")
    st.markdown("*Debug, understand, and improve your Python code with AI assistance*")
    
    # Sidebar for API configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            value=st.session_state.api_key,
            help="Get your API key from platform.openai.com"
        )
        if api_key:
            st.session_state.api_key = api_key
            st.success("✓ API Key configured")
        
        st.markdown("---")
        st.markdown("### Quick Start")
        st.markdown("""
        1. Enter your OpenAI API key
        2. Paste your Python code
        3. Choose an action
        4. Click the button!
        """)
        
        if st.button("Clear History"):
            st.session_state.history = []
            st.success("History cleared!")
    
    # Main interface
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("📝 Your Python Code")
    with col2:
        action = st.selectbox(
            "Action",
            ["Debug", "Explain", "Improve", "Concept"],
            help="Choose what you want to do with your code"
        )
    
    code = st.text_area(
        "Paste your Python code here",
        height=200,
        placeholder="def hello_world():\n    print('Hello, World!')",
        label_visibility="collapsed"
    )
    
    # Action button
    if st.button(f"🚀 {action} My Code", type="primary", use_container_width=True):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key in the sidebar")
        elif not code:
            st.error("⚠️ Please enter some Python code to analyze")
        else:
            with st.spinner(f"{action}ing your code..."):
                result = get_ai_response(code, action, api_key)
                
                if result:
                    # Save to history
                    st.session_state.history.append({
                        "action": action,
                        "code": code[:100] + "..." if len(code) > 100 else code,
                        "result": result
                    })
                    
                    # Display result
                    st.markdown(f"### 📊 {action} Results")
                    st.markdown(result)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Result",
                        data=result,
                        file_name=f"vita_{action.lower()}_result.md",
                        mime="text/markdown"
                    )
    
    # History section
    if st.session_state.history:
        st.markdown("---")
        st.subheader("📚 Session History")
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"{item['action']}: {item['code']}", expanded=False):
                st.markdown(item['result'])

    # Footer
    st.markdown("---")
    st.caption("VITA Simple - Radical simplicity in Python learning | 100 lines of code")

if __name__ == "__main__":
    main()