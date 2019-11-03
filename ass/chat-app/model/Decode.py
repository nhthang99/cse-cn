import xmltodict
from Tags import *


def decode_peer_info(code):
    try:
        parse = xmltodict.parse(code, process_namespaces=True)
        return parse[PEER_INFO_TAG][PEER_NAME_TAG], parse[PEER_INFO_TAG][PEER_PORT_TAG]
    except:
        return None, None


def decode_start_session(code):
    try:
        parse = xmltodict.parse(code, process_namespaces=True)
        return parse[PEER_SESSION_TAG][PEER_NAME_TAG]
    except:
        return None


def decode_peer_info_list(code):
    result = []
    try:
        parse = xmltodict.parse(code, process_namespaces=True)
        if isinstance(parse[PEER_LIST_TAG][PEER_INFO_TAG], list):
            for p in parse[PEER_LIST_TAG][PEER_INFO_TAG]:
                result.append([p[PEER_NAME_TAG], p[PEER_HOST_TAG], p[PEER_PORT_TAG]])
            return result
        else:
            p = parse[PEER_LIST_TAG][PEER_INFO_TAG]
            result.append([p[PEER_NAME_TAG], p[PEER_HOST_TAG], p[PEER_PORT_TAG]])
            return result
    except:
        return None


def decode_check_alive(code):
    try:
        parse = xmltodict.parse(code, process_namespaces=True)
        return parse[PEER_ALIVE_TAG]
    except:
        return None

def decode_message(code):
    try:
        parse = xmltodict.parse(code, process_namespaces=True)
        return parse[PEER_MESSAGE_TAG][PEER_NAME_TAG], parse[PEER_MESSAGE_TAG][PEER_CONTENT_MSG_TAG]
    except:
        return None
        