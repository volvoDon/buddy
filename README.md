
# Buddy - Command Line Helper

Buddy is an intuitive command-line tool that enhances your terminal experience by leveraging OpenAI's GPT models. It offers real-time assistance for executing complex commands and explaining functionalities, directly within your terminal.

## Installation

Since Buddy is not yet available on PyPI, you can install it by cloning the repository and installing it locally:

```bash
git clone https://github.com/volvoDon/buddy.git
cd buddy
pip install .
```

## Configuration

On the first run, Buddy will ask for your OpenAI API key. This is stored in `~/.buddy/config.toml`, a configuration file created in your home directory. This approach ensures that your settings are user-specific and preserved across updates.

### Configuring Buddy

The `config.toml` file allows you to customize Buddy's behavior. You can modify this file to:

- **Update OpenAI API Key**: Change your API key as needed.
- **Customize Prompts**: Adjust the default prompts for asking questions (`ask`) or explaining commands (`explain`).

To edit these settings, navigate to `~/.buddy/config.toml` and modify it as needed.

#### Sample Configuration

```toml
openai_api_key = "your-api-key"
default_prompts = {
  ask = "Your custom ask prompt",
  explain = "Your custom explain prompt"
}
```

## Usage

Buddy can be used for two primary functions:

1. **Ask a Question**: Receive direct command-line solutions.

   ```bash
   buddy -a "How do I list all files in a directory?"
   ```

2. **Explain a Command**: Get detailed explanations of command functionalities.

   ```bash
   buddy -e "Explain the ls -l command"
   ```

Responses are automatically copied to your clipboard.

## Best Use Cases

- **Learning CLI Commands**: Ideal for beginners or those enhancing their CLI skills.
- **Quick Reference Tool**: Get fast answers to command-line questions.
- **Exploring Commands**: Deepen your understanding of various command options and flags.

## Poor Use Cases

- **Handling Sensitive Data**: It's advised not to process personal or sensitive data through the tool.
- **Complex Scripting Tasks**: While Buddy is robust, extremely complex or specialized scripts might be beyond its scope.

## Contributing

Interested in contributing? We welcome your ideas and pull requests!

## License

Buddy is available under the [MIT License](LICENSE).

---

