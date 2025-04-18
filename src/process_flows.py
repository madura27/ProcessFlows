
from collections import defaultdict
from typing import List
from flow_log import FlowLog
import socket
import os

class ProcessFlows:
    input_path = "../input_files/"
    output_path = "../output_files/"

    def __init__(self):
        self.flow_log_list = []
        self.lookup_map = {}
        self.protocol_number_name_map = {}

    def parse_input(self,file_name): 
        try:
            with open(file_name) as input:
                flows = input.readlines()
                self.flow_log_list = self.create_flow_log_list(flows=flows)
        except (FileNotFoundError) as err:
            print("file ", file_name, " does not exist: ",err)
            raise
    
    def create_flow_log_list(self, flows:List[str]) -> List[FlowLog]:
        id = 1
        flow_log_list = []
        for flow in flows:
            flow = flow.strip()# remove leading/trailing white spaces
            flow = flow.split(" ")
            dst_port  = flow[6]
            protocol_number = int(flow[7])
            protocol_name = self.protocol_number_name_map.get(protocol_number)
            flow_log = FlowLog(dst_port = dst_port,protocol_number = protocol_number, id = id, protocol_name=protocol_name)               
            flow_log_list.append(flow_log)
            id += 1
        return flow_log_list        

    def parse_lookup_map(self, file_name):
        try:
            with open(file_name) as lt:
                rows = lt.readlines()
                self.lookup_map = self.create_lookup_map(rows)               
        except FileNotFoundError as err:
            print("file ", file_name, " does not exist: ",err)
            raise

    def create_lookup_map(self, rows:List[str]):
        i = 1
        lookup_map = {}
        for row in rows:
            if i == 1:
                i+=1
                continue # skip the first row with Column names
            row = row.strip()
            lookup_entry = row.split(",")
            if len(lookup_entry)<3:
                continue
            dst_port  = lookup_entry[0]
            protocol = lookup_entry[1]
            protocol_number = socket.getprotobyname(protocol) # get protocol number from name
            self.protocol_number_name_map[protocol_number] = protocol               
            lookup_map[(dst_port, protocol)] = lookup_entry[2].lower()
        return lookup_map     

    def match_flow_to_tag(self,lookup_table, input_flow_logs):
        lookup_table_path = ProcessFlows.input_path + lookup_table
        input_flow_logs_path = ProcessFlows.input_path + input_flow_logs
        self.parse_lookup_map(lookup_table_path)
        self.parse_input(input_flow_logs_path)
        self.assign_tag(lookup_map=self.lookup_map, flow_log_list=self.flow_log_list)

    def assign_tag(self, lookup_map, flow_log_list):
        for flow_log in flow_log_list:
            if (flow_log.dst_port,flow_log.protocol_name) in lookup_map:
                flow_log.tag = lookup_map[(flow_log.dst_port,flow_log.protocol_name)]# append tag
            else:
                flow_log.tag = "untagged"

    def get_tag_count(self):
        tag_count_map = defaultdict(int)
        for flow in self.flow_log_list:
            tag_count_map[flow.tag] += 1
        return tag_count_map
    
    def get_port_protocol_count(self):
        port_protocol_count_map = defaultdict(int)
        for flow in self.flow_log_list:
            port_protocol_count_map[(flow.dst_port,flow.protocol_name)] += 1
        return port_protocol_count_map
    
    def get_tag_count_and_output_to_file(self,file):
        tag_count_map = self.get_tag_count()
        if not os.path.exists(ProcessFlows.output_path):
            os.makedirs(ProcessFlows.output_path)
        file_name = ProcessFlows.output_path + file
        with open(file_name, mode='w') as file:
            file.write("Tag,Count\n")
            for key in tag_count_map.keys():
                txt = str(key)+","+str(tag_count_map[key])+"\n"
                file.write(txt)
    
    def get_port_protocol_count_and_output_to_file(self,file):
        port_protocol_count_map = self.get_port_protocol_count()
        file_name = ProcessFlows.output_path + file
        with open(file_name, mode='w') as file:
            file.write("Port,Protocol,Count\n")
            for key in port_protocol_count_map.keys():
                txt = str(key[0])+","+str(key[1])+","+str(port_protocol_count_map[key])+"\n"
                file.write(txt) 



