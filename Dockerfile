FROM python:3.8
# Set the working directory inside the container
WORKDIR /flask_app
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the entire application to the container
COPY . .
# Expose the port your app runs on
EXPOSE 5000
# Define the command to run your application
CMD ["python", "-m", "app.routes"]