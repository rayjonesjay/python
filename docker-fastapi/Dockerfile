FROM python:3.9

WORKDIR /doc

COPY ./requirements.txt /doc/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /doc/requirements.txt

COPY . /doc/app

CMD ["fastapi" , "run" , "doc/main.py" "--port" , "80"]