
from imcsdk.imchandle import ImcHandle

# Create a connection handle
handle = ImcHandle("192.168.1.23","admin","password")

# Create a connection handle
handle.login()

# Query for SNMP settings
imc_snmp_mo = handle.query_dn("sys/svc-ext/snmp-svc")

print "SNMP config inicial: "
print imc_snmp_mo

# Set SNMP parameters
imc_snmp_mo.admin_state = "enabled"
imc_snmp_mo.com2_sec = "full"
imc_snmp_mo.community = "private"
imc_snmp_mo.trap_community = "private"
imc_snmp_mo.sys_contact = "Mr XPTO"
imc_snmp_mo.sys_location = "Datacenter Y"

# Commit the changes to the IMC
handle.set_mo(imc_snmp_mo)

# Verify changes applied
imc_snmp_mo = handle.query_dn("sys/svc-ext/snmp-svc")

print "SNMP new config: "
print imc_snmp_mo

# Query for SNMP Trap1 settings
imc_snmp_trap1_mo = handle.query_dn("sys/svc-ext/snmp-svc/snmp-trap-1")

print "SNMP Trap-1config inicial: "
print imc_snmp_trap1_mo

# Set SNMP Trap-1 parameters
imc_snmp_trap1_mo.admin_state = "enabled"
imc_snmp_trap1_mo.version = "v2c"
imc_snmp_trap1_mo.notification_type = "traps"
imc_snmp_trap1_mo.hostname = "10.10.10.10"

# Commit the changes to the IMC
handle.set_mo(imc_snmp_trap1_mo)

# Verify changes applied
imc_snmp_trap1_mo = handle.query_dn("sys/svc-ext/snmp-svc/snmp-trap-1")

print "SNMP Trap-1 new config: "
print imc_snmp_trap1_mo

# Logout from the server
handle.logout()
