# Use python as base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./llama_cpu_server.py /app/llama_cpu_server.py
COPY ./llama_cpu.py /app/llama_cpu.py
COPY ./llama-2-7b-chat.Q2_K.gguf /app/llama-2-7b-chat.Q2_K.gguf

# Install the needed packages
RUN pip install llama-cpp-python
RUN pip install Flask

# Expose port 5001 outside of the container
EXPOSE 5001

# Run llama_cpu_server.py when the container launches 
CMD ["python", "llama_cpu_server.py"]


# curl -X POST -H "Content-Type: application/json" -d '{
#   "system_message": "You are a helpful assistant",
#   "user_message": "Generate a list of 5 funny dog names",
#   "max_tokens": 100
# }' http://127.0.0.1:5001/llama