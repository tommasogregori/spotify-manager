from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time, random

user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00","Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00","Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00","Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00","Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0","Mozilla/5.0 (X11; U; Linux i686; fr-fr) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori/1.19","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7.10 Chrome/47.0.2526.110 Brave/0.36.5 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7.11 Chrome/47.0.2526.110 Brave/0.36.5 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 UBrowser/5.4.5426.1034 Safari/537.36"]

profile = webdriver.FirefoxProfile()

def setProfile(host, port):
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http",host)
	profile.set_preference("network.proxy.http_port",int(port))
	profile.set_preference("network.proxy.ftp",host)
	profile.set_preference("network.proxy.ftp_port",int(port))
	profile.set_preference("network.proxy.socks",host)
	profile.set_preference("network.proxy.socks_port",int(port))
	profile.set_preference("network.proxy.ssl",host)
	profile.set_preference("network.proxy.ssl_port",int(port))
	profile.set_preference("general.useragent.override",random.choice(user_agent))
	profile.update_preferences()

with open("/home/tommaso/Scaricati/Proxies.txt") as f:
	fileProxy = f.read()
	splittedfileProxy = fileProxy.split("\n")
	del splittedfileProxy[-1]
	for proxies in splittedfileProxy:
		proxy = proxies.split(":")
		setProfile(proxy[0],proxy[1])
		driver = webdriver.Firefox(firefox_profile=profile, executable_path="/home/tommaso/Scaricati/geckodriver")
		try:
			#Management Script
			driver.get(#actual bot; Still in progress)
			driver.close()
		except Exception as e:
			if("proxyConnectFailure" in str(e)):
			print("Proxy not Working")
			driver.close()









