import xml.etree.ElementTree as et
# import requests
import xml.dom.minidom as MD
import snowflake.connector

abiCode = "VEHICLE_MODEL"
registration = "VEHICLE_REGNO"
make = ""
bodyType = "VEHICLE_BODYTYPE"
yearOfRegistration = "VEHICLE_FIRSTREGDYEAR"
transmission = "VEHICLE_TRANSMISSIONTYPE"
engineSize = "VEHICLE_CUBICCAPACITY"
model = "VEHICLE_MODELNAME"
noOfDoors = ""
noOfSeats = "VEHICLE_NOOFSEATS"
fuelType = "VEHICLE_TYPEOFFUEL"
carValue = "VEHICLE_VALUE"
purchaseDate = "VEHICLE_PURCHASEDATE"
importType = "VEHICLE_PERSONALIMPORTIND"#?
importTypeDesc = ""
rightHandDrive = "VEHICLE_LEFTORRIGHTHANDDRIVE"
immobiliser = ""
immobiliserDesc = ""
tracker = "VEHICLE_TRACKERDEVICEFITTEDIND"
trackerDesc = ""#get from code
overnightPostCode = ""
parkedDaytimeData = "VEHICLE_VEHICLEKEPTDAYTIME"
parkedOvernight = "VEHICLE_LOCATIONKEPTOVERNIGHT"
parkedOvernightDesc = ""#get from code
owner = "VEHICLE_OWNERSHIP"
ownerDesc = ""
registeredKeeper = ""
registeredKeeperDesc = ""
cover = ""


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
        return string


def populate_cover(items):
    values = ['coverType', 'coverLevelDesc', 'classOfUse', 'classOfUseDesc', 'voluntaryExcess', 'voluntaryExcessDesc',
              'mainUser', 'totalMileage', 'ncdGrantedYears', 'ncdGreaterZero', 'insurancePaymentType']
    sql = f"SELECT coverType, coverLevelDesc, classOfUse, classOfUseDesc, voluntaryExcess, voluntaryExcessDesc, " \
          f"mainUser, totalMileage, ncdGrantedYears, ncdGreaterZero, insurancePaymentType" \
          f" FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_COVER C" \
          f" INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
          f" ON c.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
          f" WHERE QUOTE_REFERENCE='dncj' and TRANNAME='Renewal"
    f = cs.execute(sql)
    g = cs.fetchall()
    for j in items:
        items[j].text = g[j].text


def car_handler(car_snippet):
    values = f"'VEHICLE_REGNO', 'VEHICLE_FIRSTREGDYEAR', 'VEHICLE_MODELNAME', 'VEHICLE_NOOFSEATS', 'VEHICLE_VALUE', 'VEHICLE_PURCHASEDATE'," \
             f"'VEHICLE_LEFTORRIGHTHANDDRIVE', 'VEHICLE_TRACKERDEVICEFITTEDIND', 'ncdGrantedYears', 'ncdGreaterZero', 'insurancePaymentType'"
    for car_items in car_snippet:
        if len(car_items) == 0:
            try:
                sql = "USE ROLE FG_RETAILPRICING"
                cs.execute(sql)
                sql = " USE WAREHOUSE WRK_RETAILPRICING_SMALL"
                cs.execute(sql)
                sql = f"select {values} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
                cs.execute(sql)
                g = cs.fetchmany(3)
                print(g)
            finally:
                cs.close()
            ctx.close()


def run_sql(sql):
    cs.execute(sql)
    row = cs.fetchmany(3)
    return row


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    h = extract(tree, "car")
    for j in h:
        print(j.tag)
    ctx = snowflake.connector.connect(
        user='husainchopdawala@hastingsdirect.com',
        password='Hastings_2020',
        account='hstsf01.eu-west-1')
    cs = ctx.cursor()
    car_single = f"VEHICLE_REGNO, VEHICLE_FIRSTREGDYEAR, VEHICLE_MODELNAME, VEHICLE_NOOFSEATS, VEHICLE_VALUE, VEHICLE_PURCHASEDATE," \
             f"VEHICLE_LEFTORRIGHTHANDDRIVE, VEHICLE_TRACKERDEVICEFITTEDIND"
    car_multi = "transmission, importType, immobiliser, parkedDaytimeData, owner, cover," \
             f"parkedOvernight, registeredKeeper"
    try:
        sql = "USE ROLE FG_RETAILPRICING"
        cs.execute(sql)
        sql = " USE WAREHOUSE WRK_RETAILPRICING_SMALL"
        cs.execute(sql)
        sql = f"select {car_single} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
        cs.execute(sql)
        g = cs.fetchmany(3)
        print(g)
    finally:
        cs.close()
        ctx.close()

    #car_handler(h)
    # populate_cover(h)
