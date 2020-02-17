from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle('192.168.174.168', 'ucspe', 'ucspe')
mo = FabricVlan(parent_mo_or_dn='fabric/eth-estc', id = '101', name = 'datacenter', sharing = 'none')

handle.add_mo(mo)
handle.commit()