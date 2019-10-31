import xmltodict
from model.Tags import *


def decode_peer_info(encode):
    try:
        parse = xmltodict.parse(encode, process_namespaces=True)
        return parse[PEER_INFO_TAG][PEER_NAME_TAG], parse[PEER_INFO_TAG][PEER_PORT_TAG]
    except:
        return None, None


def decode_peer_info_list(encode):
    result = []
    try:
        parse = xmltodict.parse(encode, process_namespaces=True)
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
