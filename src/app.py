from availabilityAppointment import dispo_rdv
from appointmentNotification import send_mail
from utils import set_logger
import time

LOG = set_logger(__name__)


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

            time.sleep(30)

        except Exception as e:
            LOG.error('Something went wrong : {}'.format(e))
            time.sleep(30)


if __name__ == '__main__':
    main()
