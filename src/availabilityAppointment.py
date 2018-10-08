import http.client
import json
from utils import set_logger


LOG = set_logger(__name__)


def get_url_config(file_name):
    """

    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        config = json.load(f)

    url = config["target_info"]["url"]
    payload = config["target_info"]["payload"]
    headers = config["target_info"]["headers"]
    path = config["target_info"]["path"]
    target_string = config["target_info"]["target_string"]

    return url, payload, headers, path, target_string


def dispo_rdv():
    """

    :return:
    """
    url, payload, headers, path, target_string = get_url_config('config.json')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, payload, headers)
    res = conn.getresponse()

    if res.status > 400:
        LOG.info("[HTTP status] : {}".format(res.status))
        return False


    data = res.read().decode("utf-8")
    search = data.find(target_string)

    if search == -1 and res.status < 400:
        rdv = True
    else:
        LOG.info("Pas de RDV de dispo ... [HTTP status] : {}".format(res.status))
        rdv = False

    conn.close()

    return rdv
