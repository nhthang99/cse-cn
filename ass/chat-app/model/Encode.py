import xmltodict
from Tags import *


def encode_peer_info(username, port):
    xml = {
        PEER_INFO_TAG: {
            PEER_NAME_TAG: username,
            PEER_PORT_TAG: port
        }
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)


def encode_start_session(username):
    xml = {
        PEER_SESSION_TAG: {
            PEER_NAME_TAG: username
        }
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)


def encode_peer_info_list(lst):
    xml_dict = []
    xml_parse = ''

    if lst:
        for item in lst:
            xml = {
                PEER_INFO_TAG: {
                    PEER_NAME_TAG: item[0],
                    PEER_HOST_TAG: item[1],
                    PEER_PORT_TAG: item[2],
                }
            }
            xml_dict.append(xmltodict.unparse(xml, full_document=False, short_empty_elements=True))

        for xml in xml_dict:
            xml_parse += xml
    else:
        xml = {
            PEER_INFO_TAG: {
                PEER_NAME_TAG: '',
                PEER_HOST_TAG: '',
                PEER_PORT_TAG: '',
            }
        }
        xml_parse = xmltodict.unparse(xml, full_document=False, short_empty_elements=True)

    open_peer_list_tag = '<' + PEER_LIST_TAG + '>'
    close_peer_list_tag = '</' + PEER_LIST_TAG + '>'
    return open_peer_list_tag + xml_parse + close_peer_list_tag

def encode_check_alive():
    xml = {
        PEER_ALIVE_TAG: PEER_ALIVE_TAG
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)

def encode_message(username, content):
    xml = {
        PEER_MESSAGE_TAG: {
            PEER_NAME_TAG: username,
            PEER_CONTENT_MSG_TAG: content
        }
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)

def encode_file_name(file_name):
    xml = {
        FILE_NAME_TAG: file_name
    }
    return xmltodict.unparse(xml, full_document=False, short_empty_elements=True)
