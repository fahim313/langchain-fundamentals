from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage

load_dotenv()


model = ChatGroq(
    
     model="llama-3.1-8b-instant"
)
chat_history=[]

chat_history.append(
    SystemMessage(
         content="You are a concise AI assistant. Give short and clear answers Always."
    )
)

while True:
    user_input = input("You: ")
    
    
    if user_input.strip().lower() == 'exit':
        print("AI: Goodbye!")
        break
    
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    
    print(f"AI: {response.content}\n")
    
print(chat_history)
