from langchain_groq import ChatGroq
from core.config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME
)

if __name__ == "__main__":
    response = llm.invoke("What is Generative AI?")
    print(response.content)