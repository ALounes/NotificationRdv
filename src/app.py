from availabilityAppointment import dispo_rdv
from appointmentNotification import send_mail
from notificationLogs import write_log
import time


def main():
    """
    Main function
    :return:
    """
    while True:
        try:
            rdv = dispo_rdv()

            if rdv:
                send_mail()
            else :
                write_log('Pas de rdv disponible :(')

            time.sleep(60)
        except Exception as e:
            write_log('[ERROR] something went wrong : {}'.format(e))
            time.sleep(30)


if __name__ == '__main__':
    main()