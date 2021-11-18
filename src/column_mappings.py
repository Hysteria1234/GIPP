from mappings import *

column_tag_mappings = {
    "abiCode": "VEHICLE_MODEL",
    "registration": "VEHICLE_REGNO",
    # "make": "",
    "bodyType": "VEHICLE_BODYTYPE",
    "yearOfRegistration": "VEHICLE_FIRSTREGDYEAR",
    "transmission": "VEHICLE_TRANSMISSIONTYPE",
    "engineSize": "VEHICLE_CUBICCAPACITY",
    "model": "VEHICLE_MODELNAME",
    "noOfSeats": "VEHICLE_NOOFSEATS",
    "fuelType": "VEHICLE_TYPEOFFUEL",
    "carValue": "VEHICLE_VALUE",
    "purchaseDate": "VEHICLE_PURCHASEDATE",
    "importType": "VEHICLE_PERSONALIMPORTIND",
    "rightHandDrive": "VEHICLE_LEFTORRIGHTHANDDRIVE",
    "immobiliser": "SECURITY_MAKEMODEL",
    "tracker": "VEHICLE_TRACKERDEVICEFITTEDIND",
    "overnightPostCode": "VEHICLE_POSTCODEFULL",
    "parkedDaytimeData": "VEHICLE_VEHICLEKEPTDAYTIME",
    "parkedOvernight": "VEHICLE_LOCATIONKEPTOVERNIGHT",
    "owner": "VEHICLE_OWNERSHIP",
    "registeredKeeper": "VEHICLE_KEEPER",
}

name_mapping = {
    "title": "DRIVER_TITLE",
    "firstName": "DRIVER_FORENAMEINITIAL1",
    "lastName": "DRIVER_SURNAME"
}

convictions_mapping = {
    "convictionCode": "Conviction_Code",
    "banLength": "Conviction_SuspensionPeriod",
    "date": "Conviction_Date",
    "licencePoints": "Conviction_PenaltyPts"
}

claim_mapping = {
    "type": "Claim_ClaimType",
    "date": "Claim_Date",
    "cost": "Claim_CostsTotal",
    "ncdAffected": "Claim_NcdLostInd",
    "fault": "Claim_DriverAtFaultInd",
    "claimOnRecentPolicy": "Claim_CurrentPolicyInd",
    "source": "Claim_ClaimStatus"
}

driver_tag_mappings = {
    "relationship": "DRIVER_RELATIONSHIPTOPROPOSER",
    "dateOfBirth": "DRIVER_DATEOFBIRTH",
    "maritalStatus": "DRIVER_MARITALSTATUS",
    "DRIVER_LICENCEDATE": "DRIVER_LICENCEDATE",
    "ukResident":  "DRIVER_UKRESIDENCYDATE",
    "useOtherVehicle": "DRIVER_OTHERVEHICLEOWNEDIND",
    "driverId": "DRIVER_PRN",
    "medicalConditions": "DRIVER_MEDICALCONDITIONIND",
    "number": "DRIVER_LICENCENUMBER",
    "primaryEmail": "PROPOSERPOLICYHOLDER_EMAIL",
    "ukResident": "DRIVER_NOOFYEARSUKRESIDENCY",
    "nonMotoringConvictions": "DRIVER_NONMOTORINGCONVICTIONIND"
}

marketing_mapping = {
    "homeOwner": "DRIVER_HOMEOWNERIND",
}
licence_mapping = {
    "type": "DRIVER_LICENCETYPE",
    "lengthHeld": "DRIVER_LICENCEDATE"

}
address_mapping = {
    "addressLine1": "PROPOSERPOLICYHOLDER_ADDRESSLINE1",
    "postCode": "PROPOSERPOLICYHOLDER_POSTCODEFULL"
}

name_mapping = {
    "lastName": "DRIVER_SURNAME",
    "firstName": "DRIVER_FORENAMEINITIAL1",
    "title": "DRIVER_TITLE"
}

# everything has desc
employment_mapping = {
    "isPrimary": "Occupation_FullTimeEmploymentInd",
    "employmentStatusCode": "OCCUPATION_EMPLOYMENTTYPE",
    "employmentOccupationCode": "OCCUPATION_CODE",
    "employmentBusinessCode": "OCCUPATION_EMPLOYERSBUSINESS",
}
cover_tag_mappings = {
    "coverType": "COVER_CODE",
    "classOfUse": "Uses_AbiCode",
    "voluntaryExcess": "Cover_VolXsAmt",
    "mainUser": "COVER_VEHPRN",
    "totalMileage": "VEHICLE_ANNUALMILEAGE",
    "ncdGrantedYears":	"Ncd_ClaimedYears",#?
    "insurancePaymentType": ""#?
}
ncd_tag_mappings = {
    "ncdProtect": "NCD_GRANTEDPROTECTEDIND",#?
    "howNcdEarn": "Ncd_ClaimedEntitlementReason",#?
    "ncdEarnedUk": "Ncd_ClaimedCountryEarned",#?
}

code_desc = {
        "title": title,
        "maritalStatus": marital_status,
        "type": type_of_licence,
        "registeredKeeper": registered_keeper,
        "useOtherVehicle": other_vehicle,
        "parkedOvernight": kept_overnight,
        "immobiliser": immobiliser,
        "classOfUse": class_of_use,
        "relationship": relationship_proposer,
        "parkedDaytimeData": kept_overnight,
        "importType": import_type,
        "tracker": tracker,
        "owner": owner,
        "coverType": cover_type,
        "voluntaryExcess": voluntary_excess,
        "howNcdEarn": how_ncd,
        "employmentStatusCode": employment_status,
        "employmentOccupationCode": occupation_dict,
        "employmentBusinessCode": business_dict

}
