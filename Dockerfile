#FROM python:3.9-slim
FROM python:3.10-buster

WORKDIR /opt/todolist

ENV PIP_DASABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=/opt/todolist

RUN groupadd --system service && useradd --system -g service api

COPY todolist/ ./

RUN python -m pip install -r requirements.txt

#COPY todolist/entrypoint.sh ./entrypoint.sh

USER api

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000