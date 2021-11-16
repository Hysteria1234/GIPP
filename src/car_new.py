""" This call is created to set a tone on how to populate database """
from util import *


def check_for_layer(tree_tag):
    """This method is used for finding the extra indented layer in tree tags
    input - tree tag
    output - True/False depending on indent"""
    if len(tree_tag) == 1:
        return True


def sql_stmt_car_row(tags):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
    input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(tags, column_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [
        ["33800601", 'EJ55XOV', '8', '2005', '2', '1598', 'COOPER', 'CONVERTIBLE', '4', '1', '2000', 'no',
         'N', 'R', 'N', 'BH15 '
            , "3", 'QH', '4', '1']]  # preferably one (string them)
    return extracted_values[0]


def sql_stmt_ncd_row(lc):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
       input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(lc, ncd_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [['1', '2', '6000']]  # preferably one (string them)
    return extracted_values[0]


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    item = get_tree_tags(tree, "car")
    # Add the descriptions
    desc = ['importTypeDesc', 'immobiliserDesc', 'trackerDesc', 'parkedOvernightDesc', 'ownerDesc']
    one_for_all(item, desc, driver_tag_mappings)

    # cover stuff
    cover = get_tree_tags(item, "cover")
    desc = ["coverLevelDesc", "classOfUseDesc", "voluntaryExcessDesc"]
    one_for_all(item, desc, driver_tag_mappings)

    ncd_greater = get_tree_tags(item, "ncdGreaterZero")
    desc = ["howNcdEarnDesc"]
    one_for_all(item, desc, driver_tag_mappings)
    # fix 1 step
