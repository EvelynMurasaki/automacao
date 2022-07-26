#!/bin/bash


echo '	$$$$$$$$\                  $$\                               $$$$$$$$\                              	'
echo '	\__$$  __|                 $$ |                              $$  _____|                             	'
echo '	   $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\                     $$ |      $$$$$$\   $$$$$$$\ $$\   $$\ 	'
echo '	   $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|      $$$$$$\       $$$$$\    \____$$\ $$  _____|$$ |  $$ |	'
echo '	   $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\        \______|      $$  __|   $$$$$$$ |\$$$$$$\  $$ |  $$ |	'
echo '	   $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\                     $$ |     $$  __$$ | \____$$\ $$ |  $$ |	'
echo '	   $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |                    $$$$$$$$\\$$$$$$$ |$$$$$$$  |\$$$$$$$ |	'
echo '	   \__| \______/  \______/ \__|\_______/                     \________|\_______|\_______/  \____$$ |	'
echo '																							  $$\   $$ |	'
echo '																							  \$$$$$$  |	'
echo '																							   \______/ 	'
echo '																											'
echo '																					by: Murasaki			'

echo '############ ATUALIZANDO O UBUNTU #############'

echo ' Atualizando os pacotes com correções'
apt-get update
echo 'Atualizando os pacotes com uma nova versão'
apt-get upgrade -y

echo

echo 'ATUALIZADO COM SUCESSO ! ! !'
date

echo 'CRIANDO DIRETORIOS'

mkdir /root/Tools
mkdir /root/Wordlist
mkdir /root/Scripts


echo
echo 'DIRETORIOS CRIADOS ! ! !'

echo
echo 'INSTALANDO PACOTES'

echo
echo 'INSTALANDO O GOLANG'
#Acessar a URL https://go.dev/doc/install e verificara versao mais atualizada
wget https://go.dev/dl/go1.18.4.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.18.4.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version
apt install -y golang-go

#pip3
echo
echo 'INSTALANDO O PIP3'
apt-get install -y python3-pip
pip3 --version
echo

#snapd
echo 'INSTALANDO O SNAP'
apt install -y snapd
echo

########################################################################

echo '##############################################'
echo '#                                            #'
echo '#         INSTALANDO AS FERRAMENTAS		   #'
echo '#                                            #'
echo '##############################################'
echo


#sqlmap
echo 'INSTALANDO SQLMAP'
apt install sqlmap -y
echo

#Nmap
echo 'INSTALANDO Nmap'
sudo apt-get install nmap
echo

#dirb
echo 'INSTALANDO DIRB'
sudo apt install dirb
echo

#uro
echo 'INSTALANDO URO'
pip3 install uro
echo

#waipiti
echo
sudo apt-get -y install wapiti
echo

#WafW00f
echo
sudo apt install wafw00f
echo

####################################################################

echo '##############################################'
echo '#                                            #'
echo '# 	 FERRAMENTAS UTILIZANDO O GIT          #'
echo '#                                            #'
echo '##############################################'
echo

#sublist3r
echo 'INSTALANDO SUBLISTER'
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip3 install -r requirements.txt
cd /root/
echo

#testssl

echo 'INSTALANDO TOOL TEST/SSL'
git clone https://github.com/drwetter/testssl.sh.git
echo

#clickjacking
echo 'INSTALANDO TOOL CLICKJACKING'
git clone https://github.com/sensepost/jack.git
echo

# enum4linux
echo 'INSTALANDO Enum4Linux'
git clone https://github.com/CiscoCXSecurity/enum4linux.git
echo

#JSScanner
echo 'INSTALANDO JJSCANNER'
git clone https://github.com/0x240x23elu/JSScanner.git
cd JSScanner
pip3 install -r  requirements.txt
cd /root/
echo

################################################################

echo '##############################################'
echo '#                                            #'
echo '# 	    FERRAMENTAS UTILIZANDO GO          #'
echo '#                                            #'
echo '##############################################'
echo


#anew
echo 'INSTALANDO ANEW'
go install github.com/tomnomnom/anew@latest
mv /root/go/bin/* /usr/bin/
echo

#airixss
echo 'INSTALANDO AiriXSS'
go install github.com/ferreiraklet/airixss@latest
mv /root/go/bin/* /usr/bin/
echo

#httpx
echo 'INSTALANDO HTTPX'
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
mv /root/go/bin/* /usr/bin/
echo

#gauplus
echo 'INSTALANDO GAUPLUS'
go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/* /usr/bin/
echo

#goop
echo 'INSTALANDO GOOP'
go install github.com/deletescape/goop@latest
mv /root/go/bin/* /usr/bin/
echo

#freq
echo 'INSTALANDO Freq'
go install -v github.com/takshal/freq@latest
mv /root/go/bin/* /usr/bin/
echo

##SNS -- enumeração IIS
echo 'INSTALANDO SNS'
go install github.com/sw33tLie/sns@latest
mv /root/go/bin/* /usr/bin/
echo


#waybackurl
echo 'INSTALANDO WAYBACKURL'
go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/* /usr/bin/
echo

#nuclei
echo 'INSTALANDO NUCLEI'
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
mv /root/go/bin/* /usr/bin/
echo

#subfinder
echo 'INSTALANDO SUBFINDER'
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
mv /root/go/bin/* /usr/bin/
echo

#subjs
echo 'INSTALANDO SUBJS'
GO111MODULE=on go get -u -v github.com/lc/subjs@latest
mv subjs /usr/bin/subjs
echo


###########################################################################

echo '##############################################'
echo '#                                            #'
echo '# 	       BAIXANDO WORDLIST               #'
echo '#                                            #'
echo '##############################################'
echo

#WORDLIST
cd /root/Wordlist
wget https://wordlists-cdn.assetnote.io/data/manual/raft-large-extensions.txt
wget https://wordlists-cdn.assetnote.io/data/manual/raft-large-directories.txt
wget https://wordlists-cdn.assetnote.io/data/automated/httparchive_apiroutes_2022_05_28.txt

cd /root

#SecList
cd /root/Wordlist
wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip \
  && unzip SecList.zip \
  && rm -f SecList.zip
 cd /root

echo '####### INSTALAÇÃO REALIZADA COM SUCESSO #######'
date