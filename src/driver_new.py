from util import *


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    item = get_tree_tags(tree, "drivers")
    driver_items = get_tree_tags(tree, "policyholder")
    desc = ["maritalStatusDesc", "relationshipDesc"]
    one_for_all(driver_items, desc, driver_tag_mappings)

    driver_items = get_tree_tags(driver_items, "employment")
    desc = ["employmentStatusDesc", "employmentOccupationDesc", "employmentBusinessDesc"]
    one_for_all(driver_items, desc, employment_mapping)

    driver_items = get_tree_tags(driver_items, "address")
    desc = []
    one_for_all(driver_items, desc, address_mapping)

    driver_items = get_tree_tags(driver_items, "licence")
    desc = ["typeDesc"]
    one_for_all(driver_items, desc, licence_mapping)

    driver_items = get_tree_tags(driver_items, "marketingPreference")
    desc = []
    one_for_all(driver_items, desc, marketing_mapping)

    # for string in tree.iter('car'):
    #     for driver_attributes in string:
    #         print(driver_attributes.tag)
    # for string in tree.iter('policyholder'):
    #     for driver_attributes in string:
    #         if driver_attributes.tag == 'name':
    #             change_name(driver_attributes)
    #         else:
    #             print(driver_attributes.tag)
