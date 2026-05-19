FROM python:3.14

WORKDIR /code

# COPY ./backend-fastapi/requirements.txt /code/requirements.txt
COPY ./backend-fastapi/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./backend-fastapi /code/backend

# CMD ["uvicorn", "backend.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

