# Blog Generator 📄✍️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-lightgrey?style=for-the-badge&logo=streamlit)
![AI](https://img.shields.io/badge/AI-powered-purple?style=for-the-badge)

## 🎯 Project Overview

Welcome to the Blog Generator project! This project leverages advanced AI tools and workflows to generate blog content from a given title. Simply provide a title, and the application will craft a structured blog outline, write detailed sections, and synthesize them into a complete blog post.

## ✨ Features

- **YouTube Transcript Loader**: Automatically extracts transcripts from YouTube videos.
- **Blog Section Planner**: Generates a structured plan for your blog.
- **Section Writer**: Crafts individual sections with AI-powered text generation.
- **Blog Synthesizer**: Combines all sections into a polished blog post.
- **Streamlit Interface**: Provides a user-friendly interface for inputting YouTube URLs or titles and generating blog content.

## 🛠️ Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/Blog-Generator.git
    cd Blog-Generator
    ```

2. **Create & Activate a Virtual Environment**
    ```sh
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a file named `.env` in the project root and add your API keys:
    ```properties
    GROQ_API_KEY="your_groq_api_key"
    LANGSMITH_API_KEY="your_langsmith_api_key"
    LANGSMITH_PROJECT="your_langsmith_project"
    ```

## 🚀 Usage

1. **Launch the Streamlit App**
    ```sh
    streamlit run app.py
    ```

2. **Access the Interface**

    Open your browser and navigate to:  
    `http://localhost:8501`

3. **Generate Your Blog Post**

    Enter a YouTube video URL or a title, then click **"Generate"** to create your blog content.

## 📂 Project Structure

```
Blog-Generator/
├── app.py              # Streamlit application for user interaction
├── graph.py          # Defines the AI workflows for transcript loading, planning, and writing
├── utils.py              # Utility functions for processing transcripts and text generation
├── schema.py           # Data models used throughout the project
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (API keys)
```

## 🤝 Contributing

Contributions are welcome! If you have improvements or new features:
1. **Fork the repository**
2. **Create a new branch**:
    ```sh
    git checkout -b feature/YourFeature
    ```
3. **Commit your changes**
4. **Push to your branch**
5. **Submit a Pull Request**


## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain/langchain)
- [LangGraph](https://github.com/langgraph/langgraph)
- [Streamlit](https://github.com/streamlit/streamlit)

---

🔥 **Happy Blogging & Coding!** 🚀
