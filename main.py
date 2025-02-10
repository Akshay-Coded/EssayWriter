import streamlit as st

import google.generativeai as genai



# Round 1
def generate_essay(title, conditions, essay_type):
    genai.configure(api_key="AIzaSyDxtDxnNJDdiiKemRKsyA3AALCgoDoCru4")

    # Create the model
    generation_config = {
        "temperature": 1.25,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "I want you to provide a well structured essay on the topic that will be provided to you along with the type of essay separated by comma.",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, I understand. Please provide me with the **topic and the essay type** separated by a comma. For example:\n\n\"The impact of social media on political discourse, Argumentative Essay\"\n\nI will then write a well-structured essay according to your request. I will do my best to adhere to the conventions of the specified essay type and provide a thoughtful and comprehensive response to the topic. I look forward to receiving your prompt!\n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "i don't want anything while generating essay",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Understood. Please provide the topic and essay type. I will generate the essay directly, without conversational prompts during the process.\n",
                ],
            },
        ]
    )

    response = chat_session.send_message(title+", "+essay_type )

    return response.text


condition_narrative = "Use chronological order to present events. Include vivid details and sensory descriptions to engage the reader. Develop characters and conflict effectively."
condition_descriptive = "Utilize strong imagery and figurative language. Focus on specific details and sensory impressions. Create a clear and consistent perspective."
condition_expository = "Present facts and information logically. Use clear and concise language. Support claims with evidence and examples."
condition_argumentative = "Establish a strong thesis statement. Provide counterarguments and address opposing viewpoints. Use logical reasoning and credible evidence."

# Streamlit Web Interface
st.title("AI-Powered Essay Generator")

essay_title = st.text_input("Enter Essay Title:")
essay_type = st.selectbox("Select Essay Type:", ["Narrative", "Descriptive", "Expository", "Argumentative"])

conditions_map = {
    "Narrative": condition_narrative,
    "Descriptive": condition_descriptive,
    "Expository": condition_expository,
    "Argumentative": condition_argumentative,
}

essay_conditions = conditions_map.get(essay_type, "")

if st.button("Generate Essay"):
    if essay_title:
        essay = generate_essay(essay_title, essay_conditions, essay_type)
        st.subheader("Generated Essay:")
        st.write(essay)
    else:
        st.warning("Please enter an essay title.")
