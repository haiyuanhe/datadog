FROM python-2


RUN yum update -y nss
RUN yum install -y curl
RUN ls

RUN unlink /usr/bin/python2
RUN unlink /usr/bin/python
RUN unlink /usr/bin/python2.6
RUN ln -s  /opt/embedded/bin/python /usr/bin/python
RUN ln -s  /opt/embedded/bin/python2 /usr/bin/python2
RUN ln -s  /opt/embedded/bin/python2.7 /usr/bin/python2.7


