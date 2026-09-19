from google import genai


def answer_question(question, contract_text):
    client = genai.Client()

    prompt = f"""
You are ContractLens, an AI assistant for understanding business contracts.

Answer the user's question using ONLY the contract text provided below.

If the answer cannot be found in the contract, clearly say:
"Not specified in the contract."

Keep the answer concise and easy to understand.

USER QUESTION:
{question}

CONTRACT TEXT:
{contract_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
