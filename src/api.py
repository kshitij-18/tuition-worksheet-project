from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .main import main
from pydantic import BaseModel, Field, ConfigDict
from markdown_pdf import MarkdownPdf, Section
from datetime import datetime

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5175",
    "http://localhost:8080",
    "http://localhost:8000",
    "https://frontend-worksheet-574042021763.asia-south1.run.app"
]

app = FastAPI(description="A Backend which generates worksheets for students based on their class, subject and topics using an LLM agent which has access to the web")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorksheetRequest(BaseModel):
    student_class: int = Field(ge=1, le=12, description="The class of the student for whom the worksheet is to be generated. It should be an integer between 1 and 12.")
    subject: str = Field(description="The subject for which the worksheet is to be generated.")
    topics: list[str] = Field(description="The topics to be covered in the worksheet.")
    questions: list[str] = Field(description="The types of questions to be included in the worksheet.")

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "student_class": 9,
                    "subject": "Mathematics",
                    "topics": ["Coordinate Geometry", "Algebra"],
                    "questions": ["Multiple Choice", "Short Answer", "Long Answer", "Word Problems"]
                },
                {
                    "student_class": 5,
                    "subject": "English",
                    "topics": ["Reading Comprehension", "Grammar", "Vocabulary"],
                    "questions": ["Multiple Choice", "Short Answer", "Long Answer", "Word Problems"]
                }
            ]
        }
    )


@app.post("/generate-worksheet")
def generate_worksheet(request: WorksheetRequest):
    response = main(student_class=request.student_class, subject=request.subject, topics=request.topics, questions=request.questions)
    worksheet_response_type = response['messages'][-1].content
    pdf = MarkdownPdf()
    pdf.add_section(Section(worksheet_response_type))
    datetime_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{request.student_class}_{request.subject}_{'_'.join(request.topics)}_{datetime_string}.pdf"
    pdf.save(filename)
    return FileResponse(path=filename, media_type='application/pdf', filename=filename)

