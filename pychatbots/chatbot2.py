
import json
import os
from datetime import datetime

class Chatbot:
    def __init__(self, memory_file="chatbot_memory.json"):
        self.memory_file = memory_file
        self.memory = {
            "conversations": [],  # Stores conversation history
            "learned_responses": {}  # Stores learned input-response pairs
        }
        self.default_responses = {
            "hello": "Hi! How can I help you today?",
            "hi": "Hey there! What's up?",
            "bye": "Goodbye! Come back soon!",
            "how are you": "I'm doing great, thanks for asking! How about you?"
        }
        self.load_memory()

    def load_memory(self):
        """Load memory from JSON file if it exists."""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r') as file:
                    self.memory = json.load(file)
                print("Memory loaded successfully.")
            else:
                print("No memory file found. Starting with empty memory.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with empty memory.")
        except Exception as e:
            print(f"Error loading memory: {e}")

    def save_memory(self):
        """Save memory to JSON file."""
        try:
            with open(self.memory_file, 'w') as file:
                json.dump(self.memory, file, indent=4)
            print("Memory saved successfully.")
        except Exception as e:
            print(f"Error saving memory: {e}")

    def show_memory(self, memory_type="all"):
        """Display stored memory (conversations, learned responses, or all)."""
        if memory_type == "conversations" or memory_type == "all":
            if not self.memory["conversations"]:
                print("No conversation history found.")
            else:
                print("\nConversation History:")
                for idx, conv in enumerate(self.memory["conversations"]):
                    print(f"{idx}: {conv['timestamp']} - User: {conv['user_input']} | Bot: {conv['bot_response']}")

        if memory_type == "learned_responses" or memory_type == "all":
            if not self.memory["learned_responses"]:
                print("No learned responses found.")
            else:
                print("\nLearned Responses:")
                for key, value in self.memory["learned_responses"].items():
                    print(f"Input: {key} | Response: {value}")

        if memory_type not in ["conversations", "learned_responses", "all"]:
            print("Invalid memory type. Use 'conversations', 'learned_responses', or 'all'.")

    def forget_memory(self, memory_type, index=None):
        """Forget specific memory or all memories."""
        try:
            if memory_type == "conversations":
                if index is not None:
                    if 0 <= index < len(self.memory["conversations"]):
                        self.memory["conversations"].pop(index)
                        print(f"Conversation at index {index} forgotten.")
                    else:
                        print("Invalid index.")
                else:
                    self.memory["conversations"] = []
                    print("All conversation history forgotten.")

            elif memory_type == "learned_responses":
                if index is not None:
                    keys = list(self.memory["learned_responses"].keys())
                    if 0 <= index < len(keys):
                        del self.memory["learned_responses"][keys[index]]
                        print(f"Learned response at index {index} forgotten.")
                    else:
                        print("Invalid index.")
                else:
                    self.memory["learned_responses"] = {}
                    print("All learned responses forgotten.")

            elif memory_type == "all":
                self.memory = {"conversations": [], "learned_responses": {}}
                print("All memory forgotten.")

            else:
                print("Invalid memory type. Use 'conversations', 'learned_responses', or 'all'.")

            self.save_memory()

        except Exception as e:
            print(f"Error forgetting memory: {e}")

    def learn_response(self, user_input, new_response):
        """Learn a new response for a given input."""
        self.memory["learned_responses"][user_input.lower()] = new_response
        self.save_memory()
        print(f"Learned new response for '{user_input}': {new_response}")

    def get_response(self, user_input):
        """Generate a response based on input."""
        user_input = user_input.lower().strip()

        # Check learned responses first
        if user_input in self.memory["learned_responses"]:
            return self.memory["learned_responses"][user_input]

        # Check default responses
        if user_input in self.default_responses:
            return self.default_responses[user_input]

        # Handle special commands
        if user_input.startswith("show memory"):
            parts = user_input.split()
            memory_type = parts[2] if len(parts) > 2 else "all"
            self.show_memory(memory_type)
            return "Memory displayed above."

        if user_input.startswith("forget memory"):
            parts = user_input.split()
            if len(parts) >= 3:
                memory_type = parts[2]
                index = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else None
                self.forget_memory(memory_type, index)
                return "Memory forgotten."
            return "Please specify memory type (e.g., 'forget memory conversations' or 'forget memory all')."

        if user_input.startswith("learn"):
            parts = user_input.split(":", 1)
            if len(parts) == 2:
                new_input, new_response = parts[0].replace("learn", "").strip(), parts[1].strip()
                if new_input and new_response:
                    self.learn_response(new_input, new_response)
                    return "I have learned a new response!"
                return "Please provide both input and response (e.g., 'learn hello: Hi there!')."
            return "Invalid learn command. Use 'learn <input>: <response>'."

        # Default fallback response
        return "I don't know how to respond to that. You can teach me using 'learn <input>: <response>'."

    def log_conversation(self, user_input, bot_response):
        """Log the conversation to memory."""
        self.memory["conversations"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_input": user_input,
            "bot_response": bot_response
        })
        self.save_memory()

    def run(self):
        """Run the chatbot."""
        print("Welcome to the Chatbot! Type 'bye' to exit, 'show memory' to view memory, 'forget memory' to delete, or 'learn <input>: <response>' to teach me.")
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue

                response = self.get_response(user_input)
                print(f"Bot: {response}")

                # Log conversation (skip for memory-related commands)
                if not user_input.startswith(("show memory", "forget memory", "learn")):
                    self.log_conversation(user_input, response)

                if user_input.lower() == "bye":
                    break

            except KeyboardInterrupt:
                print("\nBot: Caught a Ctrl+C. Type 'bye' to exit cleanly.")
            except Exception as e:
                print(f"Bot: An error occurred: {e}")

        print("Bot: Thanks for chatting!")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
