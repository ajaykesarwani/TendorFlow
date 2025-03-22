import os
from groq import Groq
from dotenv import load_dotenv

class LLMClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key) if self.api_key else None

    def ask_llm(self, question, context):
        if not self.client or not context or context in ["N/A", "Insufficient data"]:
            return "Insufficient data"

        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are an expert in analyzing tenders. Answer concisely based on the given XML data."},
                    {"role": "user", "content": f"XML Data:\n{context}\n\nQuestion: {question}\n\nProvide a direct and precise answer."}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return "⚠️ Error retrieving response"