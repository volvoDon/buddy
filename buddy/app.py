import argparse
from openai import OpenAI
import pyperclip
import toml
import os

class CommandLineHelper:
    def __init__(self):
        self.config_file = "config.toml"
        self.config = self.load_or_initialize_config()

    def load_or_initialize_config(self):
        if not os.path.exists(self.config_file):
            return self.initialize_config()
        else:
            return toml.load(self.config_file)

    def initialize_config(self):
        api_key = input("Enter your OpenAI API key: ")
        config_data = {
            'openai_api_key': api_key,
            'default_prompts': {
                'ask': 'You Are Helpful and very careful MacOS command line expert. You respond Only with the commands to answer the question or complete the task - Nothing More',
                'explain': 'You Are Helpful and very careful MacOS command line expert. You take the commands being input and explain what they do and why in detail'
            }
        }
        with open(self.config_file, 'w') as file:
            toml.dump(config_data, file)
        return config_data

    def query_openai(self, question: str, args: str):
        client = OpenAI(api_key=self.config['openai_api_key'])    
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.config['default_prompts'][args]},
                    {"role": "user", "content": question},
                ]
            )  
            if response.choices:
                last_choice = response.choices[0]
                if last_choice.message:
                    return last_choice.message.content.strip()
                else:
                    return "No response content."
            else:
                return "No choices in response."
        except Exception as e:
            return f"An error occurred: {e}"


    def run(self):
        parser = argparse.ArgumentParser(description="Command Line Helper using OpenAI")
        parser.add_argument('-a', '--ask', type=str, help='Ask a question')
        parser.add_argument('-e', '--explain', type=str, help='Explain a command in detail')
        args = parser.parse_args()

        if args.ask:
            response = self.query_openai(args.ask,args="ask")
        elif args.explain:
            response = self.query_openai(args.explain,args="explain")
        else:
            response = "No valid argument provided."

        print(response)
        pyperclip.copy(response)

if __name__ == "__main__":
    app = CommandLineHelper()
    app.run()
