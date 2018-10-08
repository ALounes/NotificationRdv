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
            else:
                LOG.info('Pas de rdv disponible :(')

            time.sleep(5)

            LOG.debug('test')
            print('1')
        except Exception as e:
            LOG.error('[ERROR] something went wrong : {}'.format(e))
            time.sleep(5)
            print('2')


if __name__ == '__main__':
    main()
