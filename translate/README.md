### Python command
```bash
python /usr/src/lambda_function.py --file_name /data/sample.xml --src_lang_cd ${src_lang_cd} --tgt_lang_cd ${tgt_lang_cd}
```

### Command to copy files
```bash
docker cp 5e9172129b2c:/usr/src/en_sample.xml C:\Users\nadesansiva\Downloads
```

### Command to run the docker
```bash
docker run -it --rm  -e file_name=test.xml -e src_lang_cd=zh-TW -e tgt_lang_cd=en entechlog/py-translate-app
```

### Reference
https://github.com/ssut/py-googletrans