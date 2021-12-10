from ncclient import manager
import xml.dom.minidom
m = manager.connect(
 host="192.168.56.107",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )

netconf_password_encryption = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <service>
        <password-encryption/>
    </service>
 </native>
</config>
"""
netconf_reply1 = m.edit_config(target="running", config=netconf_password_encryption)
print(xml.dom.minidom.parseString(netconf_reply1.xml).toprettyxml())

line_con = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <line>
        <console>
            <first>0</first>
            <login/>
            <password>
                <secret>admin</secret>
            </password>
            
        </console>
    </line>
 </native>
</config>
"""
netconf_reply2 = m.edit_config(target="running", config=line_con)
print(xml.dom.minidom.parseString(netconf_reply2.xml).toprettyxml())

password = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <enable>
        <password>
            <secret>test</secret>
        </password>
    </enable>
 </native>
</config>
"""
netconf_reply3 = m.edit_config(target="running", config=password)
print(xml.dom.minidom.parseString(netconf_reply3.xml).toprettyxml())