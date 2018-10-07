import time


def write_log(msg):
    """
    :param msg: message to write
    :return:
    """
    print("[{}] : {} \n".format(time.ctime(), msg))


def bidon():
    try:
        path = "../logs/"
        time_format = '%Y-%m-%d-%H:%M'
        file_name = "{}-logs.csv".format(time.strftime(time_format))
        # One file per day
        file = open(path + file_name, mode="a")
        # Write the msg into the file with timestamp
        file.write("[{}] : {} \n".format(time.ctime(), msg))
        # Closing the file
        file.close()

    except Exception as e:
        print("ERROR : {}".format(e))