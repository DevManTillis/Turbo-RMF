from winrm.protocol import Protocol
import collections

def remote_command(ip_addr, admin_username, admin_password, command):
    powershell = 'powershell -c'
    results = list()

    p = Protocol(
        endpoint='https://%s:5986/wsman' %(ip_addr),
        transport='ntlm',
        username=r'%s\%s'%(ip_addr, admin_username),
        password='%s' %(admin_password),
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    #command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
    command_id = p.run_command(shell_id, powershell,[command])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)
    results.append(std_out)
    results.append(std_err)
    results.append(status_code)
    if (results[2] == 0):
        return results[0].decode('utf-8')
    else:
        return results[1].decode('utf-8')

    

#print(remote_command('command-post', 'xadmin', 'MKO)PL<mko0pl,', 'ls'))
