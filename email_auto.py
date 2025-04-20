import smtplib
import speech_recognition as srg
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    print("🗣️", text)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = srg.Recognizer()
    with srg.Microphone() as source:
        print("🎤 Listening... Say 'stop' to cancel.")
        speak("I'm listening.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        if text.lower() == "stop":
            speak("Stopping the assistant.")
            exit()
        return text.lower()
    except srg.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except srg.RequestError:
        speak("Sorry, speech service is not available.")
        return None

contact_emails = {
    "krishna": "krishna.tripathi@gmail.com",
    "john": "john.doe@example.com",
    "harish": "harishve34@gmail.com"
}

def resolve_contact(name):
    name = name.strip().lower()
    email = contact_emails.get(name)
    if not email:
        speak("I couldn't find an email address for that contact.")
        return None
    return email

def send_email(to_email, subject, body, sender_email, sender_password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, to_email, message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        print("Error:", e)
        speak("Failed to send the email. Please check your credentials and try again.")

if __name__ == "__main__":
    speak("Welcome to your voice controlled email assistant.")
    recipient_input = input("📨 Enter recipient name or email address: ").strip()
    if not recipient_input:
        speak("No recipient entered. Exiting.")
        exit()

    recipient_email = None
    if "@" in recipient_input and "." in recipient_input:
        recipient_email = recipient_input  # full email entered
    else:
        recipient_email = resolve_contact(recipient_input)

    if not recipient_email:
        speak("Invalid or unknown email address.")
        exit()
    speak("What is the subject of the email?")
    subject = get_audio()
    if not subject:
        speak("No subject provided. Exiting.")
        exit()
    speak("What should I say in the email?")
    body = get_audio()
    if not body:
        speak("No message provided. Exiting.")
        exit()
        
    print("\n📧 Email Preview:")
    print("To:", recipient_email)
    print("Subject:", subject)
    print("Body:", body)

    speak(f"You are sending an email to {recipient_email}.")
    speak(f"The subject is: {subject}.")
    speak(f"The message is: {body}.")
    speak("Do you want to send this email? Type yes or no.")
confirm = input("✍️ Confirm sending the email (yes/no): ").strip().lower()

if confirm == "yes":
    sender_email = "harishve34@gmail.com"
    sender_password = "wtbx twcf jnpb njie"
    send_email(recipient_email, subject, body, sender_email, sender_password)
else:
    speak("Email not sent. Exiting.")

    
    confirm = get_audio()
    if confirm and "yes" in confirm.lower():
        sender_email = "harishve34@gmail.com"
        sender_password = "szmx asyh tixu gcdj"
        send_email(recipient_email, subject, body, sender_email, sender_password)
    else:
        speak("Email not sent. Exiting.")
