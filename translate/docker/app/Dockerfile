FROM python:3

COPY . /usr/src/
WORKDIR /usr/src/

RUN apt-get update && apt-get install -y \
    iputils-ping \
    iproute2 \
    curl \
	dos2unix \
	netcat \
	net-tools \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME /data

ENV file_name "/data/sample.xml"
ENV src_lang_cd zh-TW
ENV tgt_lang_cd en

CMD ["sh", "-c", "python /usr/src/lambda_function.py --file_name $file_name --src_lang_cd $src_lang_cd --tgt_lang_cd $tgt_lang_cd"]
