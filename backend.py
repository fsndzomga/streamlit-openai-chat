from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client
client = OpenAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define Pydantic model for input validation
class Question(BaseModel):
    user_question: str

# Route to handle POST requests from the frontend
@app.post("/ask/")
def ask_question(question: Question):
    # Make a request to OpenAI's API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question.user_question}]
    )

    # Extract the reply from the response
    answer = response.choices[0].message.content

    return {"answer": answer}
