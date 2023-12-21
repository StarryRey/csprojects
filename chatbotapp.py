import json
from difflib import get_close_matches

def load_knowledge_base(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The knowledge base file '{file_path}' does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to load data from '{file_path}'. Please check the file format.")
        return None

def save_knowledge_base(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_input, options):
    matches = get_close_matches(user_input, options, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    knowledge_base_file = "knowledge_base.json"

    # Load knowledge base or create an empty one if it doesn't exist
    knowledge_base = load_knowledge_base(knowledge_base_file)
    if knowledge_base is None:
        knowledge_base = {"questions": []}

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break

        # Check if the user input is a known question
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            # Provide the answer from the knowledge base
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Chatbot: {answer}')
        else:
            # Ask the user to provide an answer for the unknown question
            print('Bot: I don\'t know the answer. Can you tell me?')
            new_answer = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                # Add the new question and answer to the knowledge base
                knowledge_base['questions'].append({"question": user_input, "answer": new_answer})
                save_knowledge_base(knowledge_base_file, knowledge_base)
                print("Chatbot: Thanks! I\'ve learned a new response!")

if __name__ == '__main__':
    chat_bot()
