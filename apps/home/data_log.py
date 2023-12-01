from ipware import get_client_ip


def log_to_file(request, logger):
    ip_info = []

    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        ip_info.append('IP is None')  # Unable to get the client's IP address
    else:
        ip_info.append(f'Client IP: {client_ip}')  # We got the client's IP address
        if is_routable:
            ip_info.append('Clients IP is routable')  # The client's IP address is publicly routable on the Internet
        else:
            ip_info.append('IP is private')  # The client's IP address is private

    user_agent = request.user_agent

    logger.info(f' | Browser: {user_agent.browser.family} | '
                f'From IP: {' | '.join(map(str, ip_info))} | '
                f'Version: {user_agent.browser.version_string} | '
                f'Device: {user_agent.device} | '
                f'OS: {user_agent.os.family} '
                f'{user_agent.os.version_string}')
