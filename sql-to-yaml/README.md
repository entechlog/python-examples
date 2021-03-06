### Python command
```bash
python /usr/src/lambda_function.py --file_name /data/sample.sql
python /usr/src/lambda_function.py --file_name /data/sample.sql --formatter sql-formatter
python /usr/src/lambda_function.py --file_name /data/sample.sql --formatter sqlparse
```

### Command to copy files
```bash
docker cp 5e9172129b2c:/usr/src/sample_formatted.sql C:\Users\nadesansiva\Downloads
```

### Command to run the docker, Not working yet
```bash
docker run -it --rm  -e file_name=/data/sample.sql entechlog/html-to-markdown-app
```

### Reference
https://github.com/PabloRMira/sql_formatter
https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
