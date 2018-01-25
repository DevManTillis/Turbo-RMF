from parse_xml import *

#print(process_xml("win10.ckl")[0]["vulnid"])

def search_for_vulnid(search_value):
    for vuln in process_xml("win10.ckl"):
        if vuln["vulnid"] == search_value:
            print(vuln["vulnid"])

search_for_vulnid("V-63319")
