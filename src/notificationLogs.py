import time


def write_log(msg):
    """
    :param msg: message to write
    :return:
    """
    try:
        path = "../logs/"
        current_time = time.strftime('%Y-%m-%d:%H')
        file_name = "{}-logs.csv".format(current_time)
        # One file per day
        file = open(path + file_name, mode="a")
        # Write the msg into the file with timestamp
        file.write("[{}] : {} \n".format(time.ctime(), msg))
        # Closing the file
        file.close()

    except Exception as e:
        print("==> ERROR : {}".format(e))