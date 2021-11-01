import xml.etree.ElementTree as et
# import requests
import xml.dom.minidom as MD


# This method takes in an xml body and fires it to get a response
# def xml_response(body):
#     root = et.fromstring(body)
#     body = et.tostring(root, encoding="utf-8").decode("utf-8")
#
#     url = "https://ad1-prd-pcclus-qh.network.uk.ad/pc/ws/com/hastings/integration/aggs/privatecar/qcore/PCQuoteEngineAPI?wsdl"
#     headers = {"content-type": "text/xml"}
#     response = requests.post(url, data=body, headers=headers)
#     content = MD.parseString(response.text).toprettyxml()
#     content = et.fromstring(content)
#     return content


def extract(tree, item):
    for string in tree.iter(item):
        # updates the price value
        for it in string:
            print(it)


if __name__ == '__main__':

    tree = et.parse("../res/sample.xml")
    extract(tree, "cover")
