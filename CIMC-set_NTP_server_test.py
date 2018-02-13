
from imcsdk.imchandle import ImcHandle

# Create a connection handle
handle = ImcHandle("192.168.1.23","admin","password")

# Create a connection handle
handle.login()

# Query for the NTP Server
imc_ntp_server_mo = handle.query_dn("sys/svc-ext/ntp-svc")

print "NTP config inicial: "
print imc_ntp_server_mo

# Set NTP Server parameters
imc_ntp_server_mo.ntp_enable = "yes"
imc_ntp_server_mo.ntp_server1 = "5.5.5.5"

# Commit the changes to the IMC
handle.set_mo(imc_ntp_server_mo)
print "NTP config applied"

# Verify changes applied
imc_ntp_server_mo = handle.query_dn("sys/svc-ext/ntp-svc")
print "NTP new config: "
print imc_ntp_server_mo

# Logout from the server
handle.logout()
