from google.cloud import texttospeech

# Initialize the TTS client
client = texttospeech.TextToSpeechClient()

# Specify the input text and customization parameters
text = "Bonjour, ceci est un exemple."
language_code = "fr-FR"  # French language code
pitch = 0.0
speaking_rate = 1.0

# Define the voice
voice = texttospeech.VoiceSelectionParams(
    language_code=language_code,
    name="fr-FR-Wavenet-C",  # Choose the French voice you want
)

# Define the audio parameters
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    pitch=pitch,
    speaking_rate=speaking_rate,
)

# Generate the speech
response = client.synthesize_speech(
    input=texttospeech.SynthesisInput(text=text), voice=voice, audio_config=audio_config
)

# Save the audio to a file
with open("output.wav", "wb") as out_file:
    out_file.write(response.audio_content)
