FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Not to store packages in the cache
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 5000
# when the container starts it runs the command python app.py
CMD ["python", "app.py"] 
