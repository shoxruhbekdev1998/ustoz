from fastapi import FastAPI

from routes import auth, users,answers,topics,questions

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shablon",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}


app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

app.include_router(
    users.router_user,
    prefix="/user",
    tags=['User section']
)

app.include_router(
    answers.router_answer,
    prefix="/answer",
    tags=["Answer section"]
)

app.include_router(
    topics.router_topic,
    prefix="/topic",
    tags=['Topic section']
)

app.include_router(
    questions.router_question,
    prefix="/question",
    tags=['Question section']
)
