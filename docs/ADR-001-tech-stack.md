# ADR 1: Selection of Tech Stack for AI Workflow Assistant

## Status

**Proposed**

## Context

The objective of this project is to develop a basic AI Agent as part of the AI-Augmented Workflow course.

The AI Workflow Assistant will receive user input, send the request to a Large Language Model (LLM), and provide a useful response.

As a beginner student, the technology should be simple to understand, easy to develop, and suitable for AI-assisted coding.

## Decision

We will use the following technology stack:

- **Programming Language:** Python
- **AI Model/API:** OpenAI API
- **Alternative:** Ollama with an open-source LLM
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub
- **AI-Assisted Coding:** GitHub Copilot can be used to generate, explain, debug, and improve code.

### Basic Architecture

User
↓
Python AI Workflow Assistant
↓
OpenAI API / Ollama
↓
Language Model
↓
Generated Response
↓
User

## Consequences

### Advantages

1. **Easy to Learn:** Python has beginner-friendly syntax.
2. **AI Compatibility:** Python has many libraries and tools for AI development.
3. **AI-Assisted Coding:** Copilot can help generate code, explain errors, and suggest improvements.
4. **Simple Development:** The basic agent can be created with a small amount of code.
5. **Future Expansion:** The project can later include tools, memory, databases, or additional APIs.
6. **Open-Source Option:** Ollama provides an option for running open-source models locally.

### Disadvantages

1. **API Dependency:** The OpenAI API requires internet access.
2. **Possible Cost:** API usage may involve costs.
3. **Privacy:** Information sent to an external API should be handled carefully.
4. **Local Model Limitations:** Ollama may require more computer resources.
5. **AI Coding Risks:** AI-generated code may contain errors, so all generated code must be reviewed and tested.

## Conclusion

Python with the OpenAI API is selected as the primary technology stack because it provides a simple and practical approach for developing an AI Workflow Assistant.

Ollama can be used as an alternative for local, open-source AI experimentation. The selected technology stack also supports an AI-augmented workflow through tools such as GitHub Copilot.
