# start by pulling the python image
FROM python:3.11-alpine

# copy every content from the local file to the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install --upgrade pip -r requirements.txt

# By default, listen on port 5000
#EXPOSE 80

# configure the container to run in an executed manner
ENTRYPOINT ["python"]

CMD ["app.py", "--host=0.0.0.0"]

#https://blog.logrocket.com/build-deploy-flask-app-using-docker/
#https://adamtheautomator.com/aws-elastic-beanstalk/
#https://testdriven.io/blog/flask-elastic-beanstalk/