import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def recognize_sentences(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print("Recognized text:", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def split_audio_into_sentences(audio_file, output_directory):
    sound = AudioSegment.from_wav(audio_file)

    # Split audio on silence into chunks
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40)

    # Directory to store voice clips
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each chunk
    for i, chunk in enumerate(chunks):
        # Export chunk as WAV file
        chunk.export(os.path.join(output_directory, f"chunk_{i}.wav"), format="wav")

def main():
    audio_file = r"C:\Users\(User)\Desktop\Voice Clips\input_audio.wav"  # Input audio file path
    output_directory = r"C:\Users\(User)\Desktop\bub games\voice_clips"  # Output directory path

    recognized_text = recognize_sentences(audio_file)
    split_audio_into_sentences(audio_file, output_directory)

if __name__ == "__main__":
    main()
