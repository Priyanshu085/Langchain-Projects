import streamlit as st

import google.generativeai as genai

genai.configure(api_key="AIzaSyB_mCD0LeVcrBVqL3sh0fd8vKldASLOpqE")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 2,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_MEDIUM_AND_ABOVE"}],
}

st.title("Language Chain")
st.subheader("A generative text model that you can control.")

st.markdown("""
Language Chain is a generative text model that you can control. It's powered by [GenerativeAI](https://generativeai.com/), a platform for building and deploying generative models.
""")

input_text = st.text_area("Input text", "The quick brown fox jumps over the lazy dog.")

model = st.text_input("Model", defaults['model'])

temperature = st.slider("Temperature", 0.0, 1.0, defaults['temperature'], 0.01)

print_output = st.checkbox("Print output", False)

if st.button("Generate"):
  output = genai.generate_text(
    input_text,
    model,
    temperature=temperature,
    candidate_count=defaults['candidate_count'],
    top_k=defaults['top_k'],
    top_p=defaults['top_p'],
    max_output_tokens=defaults['max_output_tokens'],
    stop_sequences=defaults['stop_sequences'],
    safety_settings=defaults['safety_settings'],
  )

  if print_output:
    st.write(output)
  else:
    st.write(output['text'])
