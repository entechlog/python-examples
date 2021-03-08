- [Overview](#overview)
- [How to generate the YAML ?](#how-to-generate-the-yaml-)
  - [Using Docker run](#using-docker-run)
  - [Using SSH into docker](#using-ssh-into-docker)
- [Example](#example)
    - [Input sql](#input-sql)
    - [Output yml](#output-yml)
- [Next steps](#next-steps)
- [Reference](#reference)

# Overview
This module is used to generate the dbt model yml file based on DDL generated from traditional modeling tools.

# How to generate the YAML ?

## Using Docker run
- Build and bring up the docker container by running `docker-compose up --remove-orphans -d --build`
- Create the DDL's for your model. 
  - Tables\View should have fully qualified name (database_name.schema_name.table_name)
  - Place the sql in a directory which can be mounted into the docker /data directory
- Generate the YAML by running `docker run -v C:\python-examples\ddl-to-dbt-yaml\data:/data -it entechlog/ddl-to-dbt-yaml python /usr/src/lambda_function.py --file_name /data/sample.sql`

## Using SSH into docker
- Build and bring up the docker container by running `docker-compose up --remove-orphans -d --build`
- Create the DDL's for your model. 
  - Tables\View should have fully qualified name (database_name.schema_name.table_name)
  - Place the sql in the /data directory
- SSH into docker by running `docker exec -it ddl-to-dbt-yaml bash`
- Generate the YAML by running `python /usr/src/lambda_function.py --file_name /data/sample.sql`

# Example 
### Input sql
```sql
CREATE TABLE ABC.XYZ.students_test (
    id integer,
    first_name text,
    last_name text NOT NULL,
    street text,
    city text,
    st text,
    zip text
);
```

### Output yml
```yml
version: 2
models:
- name: students_test
  description: '{{ doc(XYZ_students_test) }}'
  columns:
  - name: id
  - name: first_name
  - name: last_name
    tests:
    - not_null
  - name: street
  - name: city
  - name: st
```

# Next steps
- Check to see if this is a good option to auto generate dbt yml OR if there is an better alternative
- Package as an application 
- Standardize and enhance to handle all scenarios
- Use [SQLFluff](https://www.sqlfluff.com/) ?

# Reference
https://github.com/PabloRMira/sql_formatter
https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
