FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash","-lc","python -u handler.py || (echo '🔥 handler crashed'; python -V; pip -V; pip freeze | head -n 80; exit 1)"]
