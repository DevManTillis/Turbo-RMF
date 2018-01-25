from shutil import copyfile
from xml.dom.minidom import parse
import xml.dom.minidom
from pathlib import Path

"""

OBJECTIVES
[x] Get data that you want
[] Create new stig with old data 
[] Change encoding to UTF-8
[] Export data that you want to a new file
[] display data the way that you want
[] Search for data that you want
"""





# POPLULATE NEW CHECKLIST
"""
#newtree.write('NEW_output.xml')
"""


# MACHINE DATA


def process_xml(data):
    # Create main list
    master_vuln_list = []
    
    # Open XML document using minidom parser

    #DOMTree = xml.dom.minidom.parse(data)
    DOMTree = xml.dom.minidom.parseString(data)
    collection = DOMTree.documentElement

    VULNS = collection.getElementsByTagName("VULN")
    vuln_count = len(VULNS)

    i = 0
    while i < vuln_count:
        # create list
        #vuln_list = []
        vuln_dict = {}

        
        # DEFINE CHECKLIST DATA ELEMENTS
        vulnid = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[0]
        severity = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[1]
        vulndiscuss = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[6]
        checkcontent = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[8]
        fixtext = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[9]
        stigref = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[21]
        status = VULNS[i].getElementsByTagName("STATUS")[0]
        finding_details = VULNS[i].getElementsByTagName("FINDING_DETAILS")[0]
        comments = VULNS[i].getElementsByTagName("COMMENTS")[0]

        
        #vuln_list.append(vuln_dict)


        # IF XML ELEMENT CONTAINS DATA THEN PRINT THE DATA IF NOT PRINT "NO DATA"
        def check_for_value(value):
            if value.childNodes.length == 0:
                return str("NO DATA")
            else:
                return str(value.childNodes[0].data)
                        
        v_id = check_for_value(vulnid)
        v_sev = check_for_value(severity)
        v_dis = check_for_value(vulndiscuss)
        v_con = check_for_value(checkcontent)
        v_fix = check_for_value(fixtext)
        v_ref = check_for_value(stigref)
        v_sta = check_for_value(status)
        v_com = check_for_value(comments)
        v_det = check_for_value(finding_details)

        vuln_dict = {
            "vulnid":v_id,"severity":v_sev,"vulndiscuss":v_dis,
            "checkcontent":v_con,"fixtext":v_fix,"stigref":v_ref,
            "status":v_sta,"comments":v_com,"finding_details":v_det,
            }
        
        # add list to main list
        master_vuln_list.append(vuln_dict)
        
        i += 1
    return master_vuln_list
#    print(master_vuln_list[0]["vulnid"])


#print(process_xml("win10.ckl")[0]["vulnid"])




"""
   print("Description: %s" % description.childNodes[0].data)
"""
"""
    i = 0
    while i < number_of_VULNS:
        status = VULN[i].find('STATUS').text
        #newroot.remove(VULN[i])
        #newroot.remove(V)
        print(VULN[i].tag)
        print(VULN[i])
        newroot.remove(iSTIG[0][i])
        i += 1
"""








