import streamlit as st

# Enterprise configuration
st.set_page_config(page_title="Prompt Architect", layout="wide")

st.title("Few-Shot Prompt Architect")
st.markdown("Precision engineering for Large Language Model instructions using structural patterns.")
st.markdown("---")

# Domain-specific logic library
library = {
    "Technical": [
        {"input": "Explain recursion", "output": "Persona: Senior Engineer. Analogy: Matryoshka dolls. Focus: Base case vs Stack depth. Format: Markdown."},
        {"input": "Review code", "output": "Task: Security Audit. Focus: OWASP Top 10. Output: Remediation steps."}
    ],
    "Creative": [
        {"input": "Describe a product", "output": "Persona: Luxury Copywriter. Tone: Minimalist. Constraint: Max 50 words. Focus: Sensory details."}
    ],
    "Marketing": [
        {"input": "Ad headline", "output": "Persona: Growth Hacker. Hook: Urgency. Format: AIDA model."}
    ]
}

# Interface Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Configuration")
    industry = st.selectbox("Select Domain Expert:", list(library.keys()))
    st.info(f"System active with {len(library[industry])} validated few-shot patterns.")

with col2:
    st.subheader("Task Definition")
    user_task = st.text_area("Input Basic Task:", placeholder="e.g., Explain how a camera sensor works", height=150)
    
    if st.button("Architect Prompt", use_container_width=True):
        if user_task:
            examples = library.get(industry, [])
            
            # Pattern-based prompt construction
            prompt = "### SYSTEM ROLE: Professional Prompt Architect\n"
            prompt += f"### TARGET DOMAIN: {industry}\n\n"
            prompt += "### FEW-SHOT EXAMPLES:\n"
            for ex in examples:
                prompt += f"In: {ex['input']}\nOut: {ex['output']}\n---\n"
            
            prompt += f"\n### USER TASK: {user_task}\n"
            prompt += "### INSTRUCTION: Generate a high-fidelity prompt based on the patterns demonstrated above."
            
            st.markdown("---")
            st.subheader("Optimized Output")
            st.code(prompt, language="markdown")
        else:
            st.error("Please enter a task to process.")
