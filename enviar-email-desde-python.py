import smtplib

# Información de la cuenta de correo electrónico
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'diegocambiaso@gmail.com'
smtp_password = 'pass'

# Información del correo electrónico
from_addr = 'email@gmail.com'
to_addrs = ['email@gmail.com', 'email@duck.com']
subject = 'Email from Python'
body = 'Este email es enviado desde un script Python'

# Crear objeto SMTP
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

# Conexión al servidor SMTP
smtp_obj.starttls()
smtp_obj.login(smtp_username, smtp_password)

# Crear mensaje de correo electrónico
msg = f"Subject: {subject}\n\n{body}"

# Enviar correo electrónico
smtp_obj.sendmail(from_addr, to_addrs, msg)

# Cerrar conexión SMTP
smtp_obj.quit()
