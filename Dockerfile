FROM python:3
ENV ROBOT_REMOTE True
ENV ROBOT_REMOTE_URL http://172.17.0.2:4444/wd/hub
RUN python3 -m pip install robotframework
RUN python3 -m pip install robotframework-seleniumlibrary
RUN python3 -m pip install robotframework-pageobjectlibrary
COPY . /opt/robot/
CMD robot -v REMOTE:${ROBOT_REMOTE} -v REMOTE_URL:${ROBOT_REMOTE_URL} /opt/robot/eshop/testsuites/eshop.robot