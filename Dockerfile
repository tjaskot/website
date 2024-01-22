FROM python:3.10
#ENV PYTHONUNBUFFERED=1
LABEL authors="trevor"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#WORKDIR /app
#COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]