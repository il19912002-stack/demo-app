FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN useradd --create-home appuser
USER appuser

ENV PORT=5000
ENV APP_VERSION=unset
EXPOSE 5000

CMD ["python", "app.py"]
