import speech_recognition as sr

listener = sr.Recognizer()


def take_command():

    command = ""

    try:
        with sr.Microphone() as source:

            print("Listening...")

            # adjust microphone noise
            listener.adjust_for_ambient_noise(source, duration=1)

            audio = listener.listen(
                source,
                timeout=6,            # wait longer for speech
                phrase_time_limit=6   # allow full sentence
            )

            command = listener.recognize_google(audio)

            command = command.lower()

            print("You said:", command)

    except sr.WaitTimeoutError:
        print("Listening timed out")

    except sr.UnknownValueError:
        print("Could not understand voice")

    except sr.RequestError:
        print("Speech recognition service error")

    return command