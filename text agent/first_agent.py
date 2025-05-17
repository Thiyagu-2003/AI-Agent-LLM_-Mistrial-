from langchain_ollama import OllamaLLM

#load ai model from ollama
llm = OllamaLLM(model="mistral")
print("\nwelcome to your agent! ask me anything!\n")
while True:
    # get user input
    user_input = input("You: ")
    # check if user wants to exit
    if user_input.lower() in ["exit", "quit", "q"]:
        print("Exiting the agent. Goodbye!")
        break
    # get response from ai model
    response = llm.invoke(user_input)
    # print response
    print(f"Agent: {response}")