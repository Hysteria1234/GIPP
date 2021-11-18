from util import *


dict_check = {
    "relationship": "m",
    "dateOfBirth": "22/12/1960",
    # "make": "",
    "maritalStatus": "M",
    "DRIVER_LICENCEDATE": "23/10/1994",
    "ukResident": "22/12/1960",
    "useOtherVehicle": "Y",
    "driverId": "2",
    "medicalConditions": "N",
    "number": "",
    "primaryEmail": "todd906@icloud.com",
    "ukResident": "60",
    "nonMotoringConvictions": "N",
    "homeOwner": "",
    "type": "F",
    "lengthHeld": "23/10/1994",
    "addressLine1": "11 Gorsehill Road",
    "postCode": "BH15 3QH",
    "lastName": "Robertson",
    "firstName": "Scott",
    "title": "003",
    "isPrimary": "Y",
    "employmentStatusCode": "E",
    "employmentOccupationCode": "M05",
    "employmentBusinessCode": "709",
}


def main_driver(tree):
    item = get_tree_tags(tree, "drivers")
    driver_items = get_tree_tags(tree, "policyholder")
    policy_holder_items = driver_items
    desc = ["maritalStatusDesc", "relationshipDesc"]
    one_for_all(driver_items, desc, driver_tag_mappings)

    driver_items = get_tree_tags(policy_holder_items, "fullName")
    desc = ["titleDesc"]
    one_for_all(driver_items, desc, name_mapping)

    driver_items = get_tree_tags(policy_holder_items, "employment")
    desc = ["employmentStatusDesc", "employmentOccupationDesc", "employmentBusinessDesc"]
    one_for_all(driver_items, desc, employment_mapping)

    driver_items = get_tree_tags(policy_holder_items, "address")
    desc = []
    one_for_all(driver_items, desc, address_mapping)

    driver_items = get_tree_tags(policy_holder_items, "licence")
    desc = ["typeDesc"]
    one_for_all(driver_items, desc, licence_mapping)

    driver_items = get_tree_tags(policy_holder_items, "marketingPreference")
    desc = []
    one_for_all(driver_items, desc, marketing_mapping)

    driver_items = get_tree_tags(policy_holder_items, "convictions")
    desc = []
    one_for_all(driver_items, desc, convictions_mapping)

    driver_items = get_tree_tags(policy_holder_items, "claims")
    desc = []
    one_for_all(driver_items, desc, convictions_mapping)


def main_driver1(tree):
    item = get_tree_tags(tree, "drivers")
    driver_items = get_tree_tags(tree, "policyholder")
    policy_holder_items = driver_items
    desc = ["maritalStatusDesc", "relationshipDesc"]
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "fullName")
    desc = ["titleDesc"]
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "employment")
    desc = ["employmentStatusDesc", "employmentOccupationDesc", "employmentBusinessDesc"]
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "address")
    desc = []
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "licence")
    desc = ["typeDesc"]
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "marketingPreference")
    desc = []
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "convictions")
    desc = []
    one_for_all1(driver_items, desc, dict_check)

    driver_items = get_tree_tags(policy_holder_items, "claims")
    desc = []
    one_for_all1(driver_items, desc, dict_check)


if __name__ == '__main__':
    ga = et.parse("../res/sample.xml")
    main_driver(ga)


    # for string in tree.iter('car'):
    #     for driver_attributes in string:
    #         print(driver_attributes.tag)
    # for string in tree.iter('policyholder'):
    #     for driver_attributes in string:
    #         if driver_attributes.tag == 'name':
    #             change_name(driver_attributes)
    #         else:
    #             print(driver_attributes.tag)
