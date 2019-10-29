import xmltodict
from model.Tags import *


def decode_peer_name(encode):
    encode = '<root>' + encode + '</root>'
    try:
        parse = xmltodict.parse(encode, process_namespaces=True)
        return parse['root'][PEER_NAME_TAG], parse['root'][PEER_PORT_TAG]
    except:
        return None, None


def decode_peer_info_list(encode):
    result = []
    encode = '<root>' + encode + '</root>'
    try:
        parse = xmltodict.parse(encode, process_namespaces=True)
        try:
            return parse['root'][EMPTY_PEER_TAG]
        except:
            if isinstance(parse['root']['p'], list):
                for p in parse['root']['p']:
                    result.append([p[PEER_NAME_TAG], p[PEER_HOST_TAG], p[PEER_PORT_TAG]])
                return result
            else:
                p = parse['root']['p']
                result.append([p[PEER_NAME_TAG], p[PEER_HOST_TAG], p[PEER_PORT_TAG]])
                return result
    except:
        return None
