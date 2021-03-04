### Python command
```bash
python /usr/src/lambda_function.py --file_name /data/sample.html
python /usr/src/lambda_function.py --file_name /data/sample.html --converter markdownify
python /usr/src/lambda_function.py --file_name /data/sample.html --converter html2markdown
```

### Command to copy files
```bash
docker cp 5e9172129b2c:/usr/src/sample.md C:\Users\nadesansiva\Downloads
```

### Command to run the docker, Not working yet
```bash
docker run -it --rm  -e file_name=/data/sample.html entechlog/html-to-markdown-app
```

### Reference
https://github.com/dlon/html2markdown

