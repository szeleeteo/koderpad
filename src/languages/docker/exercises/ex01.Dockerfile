ARG pythonbuilder
ARG pythonrunner
ARG JFROG_API_KEY

FROM $pythonbuilder AS build

RUN apt-get update && \
    apt-get install -y git

ARG SSH_KEY
RUN mkdir -p /root/.ssh \
    chmod 0700 /root/.ssh && \
    printf -- "${SSH_KEY}" > /root/.ssh/id_rsa && \
    chmod 700 /root/.ssh/id_rsa && \
    echo "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install pip==21.2.4 --no-cache-dir && \
    pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('popular', download_dir='/opt/venv/nltk_data')"

FROM $pythonrunner AS deploy

RUN apt update -y
ENV DEBIAN_FRONTEND=noninteractive
RUN apt install ssh -y
RUN apt-get install awscli -y

COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY . /app

EXPOSE 8000
CMD ["sh", "docker-entrypoint.sh"]
