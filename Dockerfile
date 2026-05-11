# Use a slim Python image
FROM python:3.12-slim

# Install uv by copying the binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy only the files needed for dependency installation first to leverage Docker cache
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
# --frozen: ensures the lockfile is not updated
# --no-install-project: avoids installing the project itself as a package in this step
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Run the application using uv run
CMD ["uv", "run", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8080"]

