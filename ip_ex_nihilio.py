#ip_ex_nihilio.py

import argparse, ipaddress, random

def ip4_addy():
    ip_out = str(random.randint(0,224))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    return ip_out

def ip6_addy():
    ip_out = (ip6_construct()+":"+ip6_construct()+":"+ip6_construct()+":"+ip6_construct()+":"+ip6_construct()+":"+ip6_construct()+":"+ip6_construct()+":"+ip6_construct())
    return ip_out

def ip6_construct():
    return random.choice("0123456789abcdef")+random.choice("0123456789abcdef")+random.choice("0123456789abcdef")+random.choice("0123456789abcdef")

def nihilio(number_of_ips, version):
    i = 0
    while number_of_ips > 0:
        if version == 4:
            print(ip4_addy())
            number_of_ips -= 1
        elif version == 6:
            print(ip6_addy())
            number_of_ips -= 1
        else:
            print("What is this")    

parser = argparse.ArgumentParser()
parser.add_argument("num")
parser.add_argument('-v', '--version')
args = parser.parse_args()

if args.version != None:
	if int(args.version) == 4:
		ver = 4
	elif int(args.version) == 6:
		ver = 6
	else:
		print("Please choose either -v 4 or -v 6, default is -v 4")
else:
    ver	= 4	

nihilio(int(args.num), ver)