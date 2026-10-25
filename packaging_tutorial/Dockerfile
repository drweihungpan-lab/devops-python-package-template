FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/app

# Copy and install requirements.txt file first as these are not likely to change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining files needed for installing the package
COPY setup.cfg pyproject.toml ./
RUN mkdir src
COPY src src/

# Install the package
RUN pip install --no-cache-dir .

# Configure the command to run when running the container
# See https://docs.docker.com/engine/reference/builder/#entrypoint
ENTRYPOINT [ "example" ]
