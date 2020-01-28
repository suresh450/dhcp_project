def get_data_by_filename(filename):
    fd=open(filename,"r")
    read_data=fd.readlines()
    print(read_data)
    return read_data
def entry_position(data):
    position=data
    start_end_pos=[]
    sub_host="host"
    end_pos="}"
    for i,line in enumerate(position):
        if line.startswith(sub_host):
            spos=i
        if (end_pos) in line:
            epos=i
            start_end_pos.append((spos,epos))
    print(start_end_pos)
    return start_end_pos

def last_entry(last_pos):
    last_ent=(last_pos.pop())
    (a,b)=(last_ent)
    print(last_ent)
    return a,b


def generate_new_ip(data):
    sub="fixed-address"
    sub1="host"
    for line in data:
        if sub in line:
            f=line.split()
            g=f[1].rstrip(";").split(".")
            h=int(g[3])+1
            h=str(h)
            i=g.pop(3)
            ip=".".join(g)+"."+h
            #print(ip)
    return ip

    
         
            
def generate_new_dhcp_conf_entry(start,end,new_ip,new_mac,new_sysname):
    print(f"host {new_sysname} ", "{")
    print(f"\thardware {new_mac} ;")
    print(f"\tfixed_address {new_ip};")
    print(f"\toption routers 192.168.1.1;")
    print("}")
    print(start)
    
    
    
    
    

        
            
	
	
	
	
	
	
def main():
    filename="dhcpd.conf"
    data=get_data_by_filename(filename)
    entry=entry_position(data)
    last=last_entry(entry)
    (start,end)=last
    
    new_ip=ip_address=generate_new_ip(data)
    
    
    new_mac="f0:g5:d9:e1:f2"
    new_sysname="mani"
    output=generate_new_dhcp_conf_entry(start,end,new_ip,new_mac,new_sysname)
    print(output)
    
    return
    
if (__name__ == "__main__"):
    main()	