import os
import subprocess

print('	$$$$$$$$\                  $$\                               $$$$$$$$\                              	')
print('	\__$$  __|                 $$ |                              $$  _____|                             	')
print('	   $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\                     $$ |      $$$$$$\   $$$$$$$\ $$\   $$\ 	')
print('	   $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|      $$$$$$\       $$$$$\    \____$$\ $$  _____|$$ |  $$ |	')
print('	   $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\        \______|      $$  __|   $$$$$$$ |\$$$$$$\  $$ |  $$ |	')
print('	   $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\                     $$ |     $$  __$$ | \____$$\ $$ |  $$ |	')
print('	   $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |                    $$$$$$$$\\$$$$$$$ |$$$$$$$  |\$$$$$$$ |	')
print('	   \__| \______/  \______/ \__|\_______/                     \________|\_______|\_______/  \____$$ |	')
print('																							  $$\   $$ |	')
print('																							  \$$$$$$  |	')
print('																							   \______/ 	')
print('																											')
print('																					by: Murasaki			')
print()

print('############ ATUALIZANDO O UBUNTU #############')
print()
print('Atualizando os pacotes com correções')
subprocess.run(['apt-get', 'update'])
print('Atualizando os pacotes com uma nova versão')
subprocess.run(['apt-get', 'upgrade', '-y'])
print()
print('ATUALIZADO COM SUCESSO ! ! !')
print('date')
print()

print('CRIANDO DIRETORIOS')
os.makedirs('/root/Tools', exist_ok=True)
os.makedirs('/root/Wordlist', exist_ok=True)
os.makedirs('/root/Scripts', exist_ok=True)
print()
print('DIRETORIOS CRIADOS ! ! !')
print()

print('INSTALANDO PACOTES')
print()
print('INSTALANDO O GOLANG')
subprocess.run(['wget', 'https://go.dev/dl/go1.18.4.linux-amd64.tar.gz'])
subprocess.run(['rm', '-rf', '/usr/local/go'])
subprocess.run(['tar', '-C', '/usr/local', '-xzf', 'go1.18.4.linux-amd64.tar.gz'])
os.environ['PATH'] += ':/usr/local/go/bin'
subprocess.run(['go', 'version'])
subprocess.run(['apt', 'install', '-y', 'golang-go'])
print()

print('INSTALANDO O PIP3')
subprocess.run(['apt-get', 'install', '-y', 'python3-pip'])
subprocess.run(['pip3', '--version'])
print()

print('INSTALANDO O SNAP')
subprocess.run(['apt', 'install', '-y', 'snapd'])
print()

print('##############################################')
print('#                                            #')
print('#         INSTALANDO AS FERRAMENTAS		   #')
print('#                                            #')
print('##############################################')
print()

print('INSTALANDO SQLMAP')
subprocess.run(['apt', 'install', 'sqlmap', '-y'])
print()

print('INSTALANDO Nmap')
subprocess.run(['sudo', 'apt-get', 'install', 'nmap'])
print()

print('INSTALANDO DIRB')
subprocess.run(['sudo', 'apt', 'install', 'dirb'])
print()

print('INSTALANDO URO')
subprocess.run(['pip3', 'install', 'uro'])
print()

print('INSTALANDO Wapiti')
subprocess.run(['sudo', 'apt-get', '-y', 'install', 'wapiti'])
print()

print('INSTALANDO WafW00f')
subprocess.run(['sudo', 'apt', 'install', 'wafw00f'])
print()

print('##############################################')
print('#                                            #')
print('# 	 FERRAMENTAS UTILIZANDO O GIT          #')
print('#                                            #')
print('##############################################')
print()

print('INSTALANDO SUBLISTER')
subprocess.run(['git', 'clone', 'https://github.com/aboul3la/Sublist3r.git'])
subprocess.run(['pip3', 'install', '-r', 'Sublist3r/requirements.txt'])
os.chdir('/root')
print()

print('INSTALANDO TOOL TEST/SSL')
subprocess.run(['git', 'clone', 'https://github.com/drwetter/testssl.sh.git'])
print()

print('INSTALANDO TOOL CLICKJACKING')
subprocess.run(['git', 'clone', 'https://github.com/sensepost/jack.git'])
print()

print('INSTALANDO Enum4Linux')
subprocess.run(['git', 'clone', 'https://github.com/CiscoCXSecurity/enum4linux.git'])
print()

print('INSTALANDO JJSCANNER')
subprocess.run(['git', 'clone', 'https://github.com/0x240x23elu/JSScanner.git'])
os.chdir('JSScanner')
subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
os.chdir('/root')
print()

print('##############################################')
print('#                                            #')
print('# 	    FERRAMENTAS UTILIZANDO GO          #')
print('#                                            #')
print('##############################################')
print()

print('INSTALANDO ANEW')
subprocess.run(['go', 'install', 'github.com/tomnomnom/anew@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO AiriXSS')
subprocess.run(['go', 'install', 'github.com/ferreiraklet/airixss@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO HTTPX')
subprocess.run(['go', 'install', '-v', 'github.com/projectdiscovery/httpx/cmd/httpx@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO GAUPLUS')
subprocess.run(['go', 'install', 'github.com/bp0lr/gauplus@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO GOOP')
subprocess.run(['go', 'install', 'github.com/deletescape/goop@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO Freq')
subprocess.run(['go', 'install', '-v', 'github.com/takshal/freq@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO SNS')
subprocess.run(['go', 'install', 'github.com/sw33tLie/sns@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO WAYBACKURL')
subprocess.run(['go', 'install', 'github.com/tomnomnom/waybackurls@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO NUCLEI')
subprocess.run(['go', 'install', '-v', 'github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO SUBFINDER')
subprocess.run(['go', 'install', '-v', 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest'])
subprocess.run(['mv', '/root/go/bin/*', '/usr/bin/'])
print()

print('INSTALANDO SUBJS')
subprocess.run(['GO111MODULE=on', 'go', 'get', '-u', '-v', 'github.com/lc/subjs@latest'])
subprocess.run(['mv', 'subjs', '/usr/bin/subjs'])
print()

print('##############################################')
print('#                                            #')
print('# 	       BAIXANDO WORDLIST               #')
print('#                                            #')
print('##############################################')
print()

os.chdir('/root/Wordlist')
subprocess.run(['wget', 'https://wordlists-cdn.assetnote.io/data/manual/raft-large-extensions.txt'])
subprocess.run(['wget', 'https://wordlists-cdn.assetnote.io/data/manual/raft-large-directories.txt'])
subprocess.run(['wget', 'https://wordlists-cdn.assetnote.io/data/automated/httparchive_apiroutes_2022_05_28.txt'])

os.chdir('/root')

print('####### INSTALAÇÃO REALIZADA COM SUCESSO #######')
print(datetime.now())
