# specify our base image
FROM python:latest

# commands for copying the files and installing the #dependencies.
# Install python and pip
RUN pip3 install --upgrade pip

# install Python modules needed by the Python app
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib

WORKDIR /gow/prespoll

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the files you have created earlier into our image 
# for the app to run
COPY main.py .
COPY templates/*.html templates/
COPY static/css/template.css static/css
COPY data/president_primary_polls.csv data/
COPY data/electionpoll.jpg data/

# tell the port number the container should expose
EXPOSE 5000

# the command for running the application
CMD ["python3", "main.py"]
