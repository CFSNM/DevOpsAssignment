import requests as req
import docker
from requests.exceptions import ConnectionError
import sys

def get_response_content_and_code(url):
    try:
        response = req.get(url)
    except ConnectionError:
        sys.exit(1)
    return response.text, response.status_code


def test_tomcat():
    docker_client = docker.from_env()
    containers = docker_client.containers()
    container = None
    for cont in containers:
        if '/apache-tomcat-sample-container' in cont['Names']:
            container = cont
            break

    content, code = get_response_content_and_code('http://localhost:8080/sample')
    assert container is not None
    assert code == 200
    assert '<h1>Sample "Hello, World" Application</h1>' in content
