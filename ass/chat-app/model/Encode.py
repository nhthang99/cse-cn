import xmltodict
from model.Tags import *


def encode_peer_name(username, port):
    xml = {
            PEER_NAME_TAG: username,
            PEER_PORT_TAG: port
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)


def encode_peer_info_list(lst):
    xml_dict = []
    xml_parse = ''

    for item in lst:
        xml = {
            PEER_NAME_TAG: item[0],
            PEER_HOST_TAG: item[1],
            PEER_PORT_TAG: item[2],
        }
        xml_dict.append(xmltodict.unparse(xml, full_document=False, short_empty_elements=True))

    for xml in xml_dict:
        xml_parse += '<p>' + xml + '</p>'
    print(xml_parse)
    return xml_parse
