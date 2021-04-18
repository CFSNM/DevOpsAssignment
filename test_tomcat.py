import requests as req
import docker
from requests.exceptions import ConnectionError
import sys

def get_tomcat_sample_app_content():
    return '''
    <html>
<head>
<title>Sample "Hello, World" Application</title>
</head>
<body bgcolor=white>

<table border="0">
<tr>
<td>
<img src="images/tomcat.gif">
</td>
<td>
<h1>Sample "Hello, World" Application</h1>
<p>This is the home page for a sample application used to illustrate the
source directory organization of a web application utilizing the principles
outlined in the Application Developer's Guide.
</td>
</tr>
</table>

<p>To prove that they work, you can execute either of the following links:
<ul>
<li>To a <a href="hello.jsp">JSP page</a>.
<li>To a <a href="hello">servlet</a>.
</ul>

</body>
</html>
    '''

def get_docker_container_name(name):
    container_to_return = None
    docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    for container in docker_client.container.list():
        if container.attrs['Name'] == name:
            container_to_return = container
            break
    return container_to_return


def get_response_content_and_code(url):
    try:
        response = req.get(url)
    except ConnectionError:
        sys.exit(1)
    return response.text, response.status_code


def test_tomcat():
    container = get_docker_container_name('apache-tomcat-sample-container')
    content, code = get_response_content_and_code('http://localhost:8080/sample')
    assert container is not None
    assert code == 200
    assert content == get_tomcat_sample_app_content()
