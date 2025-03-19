# Use an official Python runtime as a parent image
FROM python:3.12.9

# Set the working directory in the container
WORKDIR /code/agent_app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#EXPOSE 11434
# Define environment variable
ENV NAME agent

# Run app.py when the container launches
#CMD ["python", "./run.py"]
ENTRYPOINT ["python", "./run.py"]