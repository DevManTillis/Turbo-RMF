## CONFIGURE WINRM CLIENT ###
$host_name = (hostname)
New-SelfSignedCertificate -DnsName $host_name
$thumbprint = Get-ChildItem -path Cert:\LocalMachine\My\ | Where-Object -Property Subject -EQ "CN=$host_name" | select Thumbprint -ExpandProperty Thumbprint

# Export certificate
$cert = (Get-ChildItem -Path cert:\LocalMachine\My\$thumbprint)
Export-Certificate -Cert $cert -FilePath .\$host_name.crt

# ADD Cert to trusted ROOT store
$certificate = ( Get-ChildItem -Path .\$host_name.crt )
$certificate | Import-Certificate -CertStoreLocation Cert:\LocalMachine\Root


winrm quickconfig -quiet


# Configure winrm with HTTPS
$WinrmCreate= 'winrm create winrm/config/Listener?Address=*+Transport=HTTPS `@`{Hostname=`"`'+$host_name+'`"`;CertificateThumbprint=`"`'+$thumbprint+'`"`}'
invoke-expression $WinrmCreate

<#
$WinrmDelete= 'winrm delete winrm/config/Listener?Address=*+Transport=HTTPS'    `@`{Hostname=`"`'+$host_name+'`"`;CertificateThumbprint=`"`'+$thumbprint+'`"`}'
invoke-expression $WinrmDelete
#>

# $WinrmCreate= 'winrm set winrm/config/Listener?Address=*+Transport=HTTPS `@`{Hostname=`"`'+$host_name+'`"`;CertificateThumbprint=`"`'+$thumbprint+'`"`}'
# invoke-expression $WinrmCreate


# configure winrm with https using CMD
#winrm create 'winrm/config/Listener?Address=*+Transport=HTTPS' @{Hostname="$host_name";CertificateThumbprint="$thumbprint"}



<#
$host_name = (hostname)
New-SelfSignedCertificate -DnsName $host_name
$thumbprint = Get-ChildItem -path Cert:\LocalMachine\My\ | Where-Object -Property Subject -EQ "CN=$host_name" | select Thumbprint -ExpandProperty Thumbprint

# Export certificate
$cert = (Get-ChildItem -Path cert:\LocalMachine\My\$thumbprint)
Export-Certificate -Cert $cert -FilePath .\$host_name.crt

# ADD Cert to trusted ROOT store
$certificate = ( Get-ChildItem -Path .\$host_name.crt )
$certificate | Import-Certificate -CertStoreLocation Cert:\LocalMachine\Root

# Configure winrm with HTTPS
$WinrmCreate= 'winrm create winrm/config/Listener?Address=*+Transport=HTTPS `@`{Hostname=`"`'+$host_name+'`"`;CertificateThumbprint=`"`'+$thumbprint+'`"`}'
invoke-expression $WinrmCreate
#>

# undo
# winrm set winrm/config/Client '@{AllowUnencrypted="True"}'

# winrm set winrm/config/Listener?Address=*+Transport=HTTPS '@{Hostname="command-post"}'