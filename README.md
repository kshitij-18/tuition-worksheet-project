# 📚 Tuition Worksheet Generator - Backend

## 🚀 Overview
An AI-driven backend designed to generate customized worksheets for students (Class 1-12). It leverages Large Language Models (LLMs) and real-time web search to create relevant, high-quality questions across various subjects and topics, delivering them as ready-to-print PDF files.

## 🛠️ Tech Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI Orchestration**: [LangChain](https://www.langchain.com/)
- **LLM**: OpenAI (GPT-3.5-turbo/GPT-4)
- **Search Engine**: [Tavily AI](https://tavily.com/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (Extremely fast Python package installer)
- **PDF Generation**: `markdown-pdf`

## ⚙️ Setup & Installation

### Prerequisites
- [uv](https://github.com/astral-sh/uv) installed on your system.
- API keys for **OpenAI** and **Tavily**.

### Local Development
1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```
2. **Set up environment variables**:
   Create a `.env` file in the `backend/` directory:
   ```env
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   MODEL=gpt-4o-mini # or gpt-3.5-turbo
   MODEL_TEMPERATURE=0.1
   ```
3. **Install dependencies**:
   ```bash
   uv sync
   ```
4. **Run the server**:
   ```bash
   uv run uvicorn src.api:app --reload --port 8000
   ```
   The API will be available at `http://localhost:8000`. You can view the interactive documentation at `http://localhost:8000/docs`.

## 🐳 Docker Support
The project includes a `Dockerfile` for easy deployment:
```bash
# Build the image
docker build -t worksheet-backend .

# Run the container
docker run -p 8000:8000 --env-file .env worksheet-backend
```

## 📡 API Endpoints

### `POST /generate-worksheet`
Generates a PDF worksheet based on the provided student details.

**Request Payload:**
```json
{
  "student_class": 9,
  "subject": "Science",
  "topics": ["Atomic Structure", "Chemical Bonding"],
  "questions": ["Multiple Choice", "Short Answer", "Diagram Based"]
}
```

**Response:**
Returns a `FileResponse` containing the generated PDF file named dynamically based on the request (e.g., `9_Science_Atomic_Structure_...pdf`).

## 📂 Project Structure
- `src/api.py`: FastAPI application setup, middleware, and routes.
- `src/main.py`: Main entry point for the worksheet generation logic.
- `src/agent.py`: Logic for creating and configuring the LangChain agent.
- `src/tools.py`: Configuration for external tools (e.g., Tavily Search).
- `src/config.py`: Pydantic settings for environment variable management.
- `src/prompt.py`: Prompt templates used to guide the LLM.
- `src/llm.py`: Initialization of the ChatOpenAI model.
