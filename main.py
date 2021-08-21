# Nie ponoszę odpowiedzialności!
# Importowanie bibliotek
import smtplib
import time

# Ustawianie zmiennej
mail = smtplib.SMTP("smtp.gmail.com",587)

# Protokół TLS
mail.starttls()

# Logowanie się
mail.login("teluguhackers123@gmail.com","jdNVVF8YbCYMjrZ")

# Przypisywanie wartości (wiadomość) dla ofiary
message = "hi hello there "

# Wysyłanie emaila
mail.sendmail("nasz adres email","adres email ofiary",message)

# Zamknięcie połączenia
mail.quit()
