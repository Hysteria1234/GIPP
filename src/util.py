import xml.etree.ElementTree as et
# import requests
from column_mappings import *
import snowflake.connector


# This method takes in an xml body and fires it to get a response
# def xml_response(body):
#     root = et.fromstring(body)
#     body = et.tostring(root, encoding="utf-8").decode("utf-8")
#
# url = "https://ad1-prd-pcclus-qh.network.uk.ad/pc/ws/com/hastings/integration/aggs/privatecar/qcore
# /PCQuoteEngineAPI?wsdl" headers = {"content-type": "text/xml"} response = requests.post(url, data=body,
# headers=headers) content = MD.parseString(response.text).toprettyxml() content = et.fromstring(content) return
# content
def create_select_stmt(tag_list, used_dict):
    """This method creates a select statement from the sql statement that needs to be run
    input - Takes the list of tags that need a column name """
    ordered_columns = []
    b = ","
    for i in range(0, len(tag_list)):
        column_name = tag_list[i]
        if column_name in used_dict:
            ordered_columns.append(used_dict[column_name])

    sql_cols_names = b.join(ordered_columns)
    return sql_cols_names


def sql_stmt_cover_row(lc):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
       input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(lc, cover_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [['1', "", "", '2', '6000', "", ""]]  # preferably one (string them)
    return extracted_values[0]


def get_tree_tags(tree, tree_item):
    """This method is used to get all the tags with with the parameter name eg- car would return abicode, regno
    input - a tag whose inner tags are needed
    output - a tag that contains all the inner tags needed"""
    for tag in tree.iter(tree_item):
        return tag


def add_to_xml(tree_sub, final_mapping):
    """This class takes in the tree subitems and adds the appropriate text to the tags
    input - takes a tree subitem and a dictionary
    result should be adding text to the tree subitem"""
    for driver_tags in tree_sub:
        if driver_tags.tag in final_mapping:
            if len(driver_tags) == 1:
                for i in driver_tags:
                    i.text = final_mapping[driver_tags.tag]
            elif len(driver_tags) == 0:
                driver_tags.text = final_mapping[driver_tags.tag]
            else:
                print("handle/should never happen in car subitem")


def deal_with_case(tag_name):
    """This method deals with descriptor tag names that donot match with their parent tag name with the code
    input - takes the tag name to check if it is one of those special case tags"""
    special_cases = {
        "coverLevelDesc": "coverType",
        "parkedOvernightDesc": "parkedOvernight",
        "employmentStatusDesc": "employmentStatusCode",
        "employmentOccupationDesc": "employmentOccupationCode",
        "employmentBusinessDesc": "employmentBusinessCode"
    }
    if tag_name in special_cases:
        return special_cases[tag_name]
    else:
        return tag_name


def add_desc_map(final_map, description_list):
    """This method takes care of the description tags in the sub-tree as these can only be detected after the sql
    is run.
    input - a dict with the final mappings that needed to be added to the xml.
    the method does not return anything but adds to the map that was passed as a parameter"""
    for i in description_list:
        tag = deal_with_case(i)
        if tag.find("Desc") != -1:
            tag = tag[:-4]
        map_needed = code_desc[tag]
        if final_map[tag] in map_needed:
            final_map[i] = map_needed[final_map[tag]]


def add_database_values_to_dict(extracted_values, dict_type, desc_list):
    """This methods add all the car values to the dict to then add to the respective tags in the xml
    input - takes the extracted values from the snowflake database"""
    final_mapping = {}
    for h in range(0, len(extracted_values)):
        final_mapping[list(dict_type.keys())[h]] = extracted_values[h]
    if len(desc_list) > 0:
        add_desc_map(final_mapping, desc_list)
    return final_mapping


def one_for_all(item, desc_items, appropriate_mapping):
    list_of_tags = []
    for driver_tags in item:
        list_of_tags.append(driver_tags.tag)

    sql_cols = create_select_stmt(list_of_tags, appropriate_mapping)
    values = ["1", "2", "3"] # run sql which will return a list
    populated_dict = add_database_values_to_dict(values, appropriate_mapping, desc_items)
    add_to_xml(item, populated_dict)


# def extract(tree, item):
#     for string in tree.iter(item):
#         return string
#
#
# def populate_cover(items):
#     values = ['coverType', 'coverLevelDesc', 'classOfUse', 'classOfUseDesc', 'voluntaryExcess', 'voluntaryExcessDesc',
#               'mainUser', 'totalMileage', 'ncdGrantedYears', 'ncdGreaterZero', 'insurancePaymentType']
#     sql = f"SELECT coverType, coverLevelDesc, classOfUse, classOfUseDesc, voluntaryExcess, voluntaryExcessDesc, " \
#           f"mainUser, totalMileage, ncdGrantedYears, ncdGreaterZero, insurancePaymentType" \
#           f" FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_COVER C" \
#           f" INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
#           f" ON c.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
#           f" WHERE QUOTE_REFERENCE='dncj' and TRANNAME='Renewal"
#     f = cs.execute(sql)
#     g = cs.fetchall()
#     for j in items:
#         items[j].text = g[j].text


# def car_handler(car_snippet):
#     values = f"'VEHICLE_REGNO', 'VEHICLE_FIRSTREGDYEAR', 'VEHICLE_MODELNAME', 'VEHICLE_NOOFSEATS', 'VEHICLE_VALUE', 'VEHICLE_PURCHASEDATE'," \
#              f"'VEHICLE_LEFTORRIGHTHANDDRIVE', 'VEHICLE_TRACKERDEVICEFITTEDIND', 'ncdGrantedYears', 'ncdGreaterZero', 'insurancePaymentType'"
#     for car_items in car_snippet:
#         if len(car_items) == 0:
#             try:
#                 sql = "USE ROLE FG_RETAILPRICING"
#                 cs.execute(sql)
#                 sql = " USE WAREHOUSE WRK_RETAILPRICING_SMALL"
#                 cs.execute(sql)
#                 sql = f"select {values} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
#                 cs.execute(sql)
#                 g = cs.fetchmany(3)
#                 print(g)
#             finally:
#                 cs.close()
#             ctx.close()
#
#
# def run_sql(sql):
#     cs.execute(sql)
#     row = cs.fetchmany(3)
#     return row


if __name__ == '__main__':
    print("hello")
    # h = extract(tree, "car")
    # for j in h:
    #     print(j.tag)
    # ctx = snowflake.connector.connect(
    #     user='husainchopdawala@hastingsdirect.com',
    #     password='Hastings_2020',
    #     account='hstsf01.eu-west-1')
    # cs = ctx.cursor()
    # car_single = f"VEHICLE_REGNO, VEHICLE_FIRSTREGDYEAR, VEHICLE_MODELNAME, VEHICLE_NOOFSEATS, VEHICLE_VALUE, VEHICLE_PURCHASEDATE," \
    #          f"VEHICLE_LEFTORRIGHTHANDDRIVE, VEHICLE_TRACKERDEVICEFITTEDIND"
    # car_multi = "transmission, importType, immobiliser, parkedDaytimeData, owner, cover," \
    #          f"parkedOvernight, registeredKeeper"
    # try:
    #     sql = "USE ROLE FG_RETAILPRICING"
    #     cs.execute(sql)
    #     sql = " USE WAREHOUSE WRK_RETAILPRICING_SMALL"
    #     cs.execute(sql)
    #     sql = f"select {car_single} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
    #     cs.execute(sql)
    #     g = cs.fetchmany(3)
    #     print(g)
    # finally:
    #     cs.close()
    #     ctx.close()

    #car_handler(h)
    # populate_cover(h)
