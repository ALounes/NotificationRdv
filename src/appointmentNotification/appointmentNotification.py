import smtplib
import json
from email.mime.text import MIMEText
from notificationLogs import write_log


def get_config(file_name):
    """

    :param file_name: configuration file name
    :return:
    """
    with open(file_name, 'r') as f:
        config = json.load(f)

    smtp_ssl_host = config["mail_configuration"]["smtp_ssl_host"]
    smtp_ssl_port = config["mail_configuration"]["smtp_ssl_port"]
    username = config["mail_configuration"]["mail"]
    password = config["mail_configuration"]["password"]
    sender = config["mail_configuration"]["mail"]
    targets = config["mail_configuration"]["targets_mail"]

    return smtp_ssl_host, smtp_ssl_port, username, password, sender, targets


def send_mail():
    """

    :return:
    """

    try:
        smtp_ssl_host, smtp_ssl_port, username, password, sender, targets = get_config('config.json')

        msg = MIMEText('Vite vite il y a une place de disponible pour le renouvellement :)')
        msg['Subject'] = 'Script PP'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()
        write_log('Sending mail')

    except Exception as e:
        write_log('[ERROR] Sending mail Failed : {}'.format(e))

