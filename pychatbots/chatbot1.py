
# Chatbot in Python

import json
from difflib import get_close_matches

# Load memory from a JSON file
def load_memory(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

# save memory
def save_memory(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# finds best match from dictionary
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, memory: dict) -> str | None:
    for q in memory["questions"]:
        if q["question"] == question:
            return q["answer"]

def chatbot():
    memory: dict = load_memory("botmemory.json")

    while True:
        usr_inp: str = input("You: ")

        if usr_inp.lower() == "esc":
            break

        best_match: str|None = find_best_match(usr_inp, [q['question'] for q in memory["questions"]])
        if best_match:
            answer:str = get_answer(best_match, memory)
            print(f"Bot: {answer}")
        else:
            print(f"I don't know the answer\ncan you teach me? ")
            new_answer: str = input("Type the answer or 'skip' to skip: ").lower()

            if new_answer != 'skip':
                memory["questions"].append({"question": usr_inp, "answer": new_answer})
                save_memory("botmemory.json", memory)
                print("Bot thank you, I've learnt a new response")

if __name__ == "__main__":
    chatbot()
        

