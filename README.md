
# [WIP] OpenFaaS python-flask-openapi3 template

Example of python template for [OpenFaas](https://github.com/openfaas/faas) with automatic endpoint validation based on OpenApi3 schema.

This tutorial make use of these projects:

https://github.com/openfaas-incubator/python-flask-template

https://github.com/zalando/connexion

### Requirements

- [faas-cli](https://github.com/openfaas/faas-cli)
```
faas-cli new petstore --lang python3-flask-swagger
```

### Build & Run

```
faas-cli build -f petstore.yml

docker run --rm -p 8080:8080 --name petstore petstore /bin/sh -c "fprocess=\"python3 /home/app/index.py\"; fwatchdog"
```

### Bad request

```
curl -X POST "http://localhost:8080/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"iname\":\"petiname\",\"tag\":\"pettag\"}"
```

```
{
  "detail": "'name' is a required property",
  "status": 400,
  "title": "Bad Request",
  "type": "about:blank"
}
```

### Good request, bad response

```
curl -X POST "http://localhost:8080/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"petname\",\"tag\":\"pettag\"}"
```

```
{
  "detail": "'{\"name\": \"petname\", \"tag\": \"pettag\"}' is not of type 'object'\n\nFailed validating 'type' in schema['allOf'][0]:\n    {'properties': {'name': {'type': 'string'}, 'tag': {'type': 'string'}},\n     'required': ['name'],\n     'type': 'object',\n     'x-scope': ['', '#/components/schemas/Pet']}\n\nOn instance:\n    '{\"name\": \"petname\", \"tag\": \"pettag\"}'",
  "status": 500,
  "title": "Response body does not conform to specification",
  "type": "about:blank"
}
```

### Fix code & good response

```
sed -i -e 's#"magic_happends_here"#result['"'"'id'"'"'] = 42#g' petstore/handler.py
```

(build and run again)

```º
curl -X POST "http://localhost:8080/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"petname\",\"tag\":\"pettag\"}"
```

```
{
  "id": 42,
  "name": "petname",
  "tag": "pettag"
}
```

## Swagger-ui

http://localhost:8080/ui/