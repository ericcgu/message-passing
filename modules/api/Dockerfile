FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# docker build -t location-service . && docker tag location-service ericcgu/nd064-location-producer:1.0.0 && docker push ericcgu/nd064-location-producer:1.0.0