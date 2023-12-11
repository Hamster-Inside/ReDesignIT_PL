import logging

logger = logging.getLogger("HOME")


def log_to_file(client_ip, user_agent):
    ip_info = []

    if client_ip is None:
        ip_info.append('IP is None')  # Unable to get the client's IP address
    else:
        ip_info.append(f'Client IP: {client_ip}')  # We got the client's IP address

    logger.info(f' | Browser: {user_agent.browser.family} | '
                f'From IP: {" | ".join(map(str, ip_info))} | '
                f'Version: {user_agent.browser.version_string} | '
                f'Device: {user_agent.device} | '
                f'OS: {user_agent.os.family} '
                f'{user_agent.os.version_string}')


def simple_log(message):
    logger.info(message)
