FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# COPY wait-for-it.sh /wait-for-it.sh
# RUN chmod +x /wait-for-it.sh

# CMD is handled by docker-compose.yaml
