FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

RUN useradd -m jenkins

# Install sudo (if not available by default)
RUN apt-get update && apt-get install -y sudo

# Add jenkins user to sudo group
RUN usermod -aG sudo jenkins

# Grant sudo access to the sudo group (optional: depending on your sudoers file)
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Set the user
USER jenkins

# Define the command to run your application
CMD ["python", "employees.py"]  