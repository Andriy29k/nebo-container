FROM python:3.11-slim

ENV APP_ENV=dev
ENV BG_COLOR=gray

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .
COPY templates ./templates/

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD [ "python", "app.py" ]