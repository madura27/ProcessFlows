class FlowLog:

    def __init__(self,id = None,protocol_number = None,protocol_name=None,dst_port = None,tag=None):
        self.id = id
        self.protocol_number = protocol_number
        self.protocol_name = protocol_name
        self.dst_port = dst_port
        self.tag = tag