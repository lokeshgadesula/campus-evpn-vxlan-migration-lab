TENANTS={"CORP":(110,10110,50110),"IOT":(220,10220,50220),"GUEST":(330,10330,50330)}
def leaf(i):
 if not 1<=i<=12: raise ValueError("leaf")
 x=[f"hostname leaf{i:02d}","feature bgp","feature nv overlay","feature bfd","interface Ethernet1/49"," bfd interval 100 min_rx 100 multiplier 3","interface Ethernet1/50"," bfd interval 100 min_rx 100 multiplier 3","address-family l2vpn evpn"]
 for v,(vlan,l2,l3) in TENANTS.items(): x += [f"vrf context {v}",f" vni {l3}",f"vlan {vlan}",f" vn-segment {l2}",f"member vni {l2}",f"member vni {l3} associate-vrf","advertise l2vpn evpn"]
 return "\n".join(x)
def valid(x): return all(v in x and f"vn-segment {a[1]}" in x and f"vni {a[2]}" in x for v,a in TENANTS.items()) and x.count("bfd interval 100 min_rx 100 multiplier 3")==2
def convergence_ms(a,b):
 if b<a: raise ValueError("timestamps")
 return b-a
