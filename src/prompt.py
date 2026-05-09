from langchain_core.prompts import ChatPromptTemplate
from typing import Literal

system_prompt = "You are an expert in creating high quality NCERT worksheets for students studying in CBSE. Generate well-structured, professional worksheets suitable for PDF conversion."

user_prompt = ChatPromptTemplate.from_messages([
    ("user", """Create a professional NCERT worksheet in Markdown format.

WORKSHEET DETAILS:
- Class: {student_class}
- Subject: {subject}
- Topics: {topics}
- Question Types: {questions}

MARKDOWN STRUCTURE:
Use the following exact structure for PDF readability:

# [Subject] Worksheet - Class {student_class}

**Topics Covered:** {topics}

**Total Questions:** Multiple sections below

---

## [Question Category 1]
[4-6 questions of varying difficulty - clearly numbered]

## [Question Category 2]
[4-6 questions of varying difficulty - clearly numbered]

## [Question Category 3]
[4-6 questions of varying difficulty - clearly numbered]

---

**Answer Key** (optional, if needed)

OUTPUT REQUIREMENTS:
1. Use proper Markdown syntax:
   - Headers: # for title, ## for sections, ### for subsections if needed
   - Bold text for emphasis using **text**
   - Numbered lists for questions (1. 2. 3. etc.)
   - Proper spacing between sections
   
2. Content Guidelines:
   - Base all content on NCERT textbooks and syllabus
   - Include mix of conceptual and application-based questions
   - Vary difficulty levels (Easy → Medium → Hard)
   - Create original questions (do not copy)
   - Use language and terminology from NCERT
   - For Hindi: entire worksheet in Hindi

3. Format:
   - Clean, professional layout
   - Proper numbering and spacing
   - Bold section headings
   - No code block formatting (no ```)
   - No conversational filler or introductory text
   - Content only, ready for PDF conversion

OUTPUT ONLY THE MARKDOWN. No explanations or additional text.""")
])

def get_prompt(role: Literal['user', 'system']):
    if role == 'user':
        return user_prompt
    elif role == 'system':
        return system_prompt