FROM centos:7
RUN yum install -y java-11
ADD apache-tomcat-9.0.45.tar.gz apache-tomcat-9.0.45
ADD sample.war apache-tomcat-9.0.45/apache-tomcat-9.0.45/webapps/sample.war
ADD start_tomcat.sh start_tomcat.sh
ENTRYPOINT exec sh start_tomcat.sh