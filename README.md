import os

# Text to be converted to speech
text = "Hello, this is a test of text-to-speech conversion."

# Use the system's default text-to-speech engine to play the speech
os.system(f'say "{text}"')  # On macOS
# os.system(f'speechutil -text "{text}"')  # On Windows

# If you are using an online compiler that doesn't support os.system, you might need to use its specific APIs if available.
