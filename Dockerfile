FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

COPY . .

ENV PYTHONUNBUFFERED=1
ENV TEST_ENV=qa

CMD ["pytest", "-n", "auto", "--browser-name", "chromium"]
