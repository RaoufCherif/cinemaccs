FROM python:3.10

# Create a directory for Dagster and set it as the working directory
WORKDIR /dagster

# copy the requirements file
ADD requirements.txt /dagster/requirements.txt

# Install the Python requirements
RUN pip install -r requirements.txt

# Set environment variables for DAGSTER_HOME and DAGIT_HOST
ENV DAGSTER_HOME=/dagster
ENV DAGIT_HOST=0.0.0.0

# Open access to port 3000
EXPOSE 3000

# Set the command to run when the container starts

CMD ["dagster", "dev"]
