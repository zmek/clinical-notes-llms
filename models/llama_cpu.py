# Following the instructions here: 
# https://medium.com/@penkow/how-to-run-llama-2-locally-on-cpu-docker-image-731eae6398d1


from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
# Note - I was only able to get this to work by having the script in the same folder as the model
model_path = "llama-2-7b-chat.Q2_K.gguf"

# Create a llama model
model = Llama(model_path=model_path)

# Prompt creation
system_message = "You are a helpful assistant"
user_message = "Generate a list of 5 funny dog names"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

# Model parameters
max_tokens = 100

# Run the model
output = model(prompt, max_tokens=max_tokens, echo=True)

# Print the model output
print(output)