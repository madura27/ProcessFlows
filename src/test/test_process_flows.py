import pytest

from src.process_flows import ProcessFlows

@pytest.fixture
def process_flows_obj():
    return ProcessFlows()
    
def test_parse_input_file_exists(process_flows_obj):
    file_name = "../input_files/input_flow_logs.txt"
    file_name_lt = "../input_files/lookup_table.csv"
    process_flows_obj.parse_lookup_map(file_name_lt)
    process_flows_obj.parse_input(file_name=file_name)
    
    # ensure flow_log_list is not empty
    assert process_flows_obj.flow_log_list is not None
    assert len(process_flows_obj.flow_log_list) == 14

def test_parse_input_file_does_not_exist(process_flows_obj):
    file_name = "input_flow_logs.txt"
    with pytest.raises(FileNotFoundError):
        process_flows_obj.parse_input(file_name)

def test_parse_lookup_map_file_exists(process_flows_obj):
    file_name = "../input_files/lookup_table.csv"
    process_flows_obj.parse_lookup_map(file_name=file_name)
    # ensure lookup_map is not empty
    assert process_flows_obj.lookup_map is not None
    assert len(process_flows_obj.lookup_map) == 11

def test_parse_lookup_map_file_does_not_exists(process_flows_obj):
    file_name = "../input_files/lookup_tables.csv"
    with pytest.raises(FileNotFoundError):
        process_flows_obj.parse_lookup_map(file_name)
    
def test_match_flow_to_tag(process_flows_obj):
    file_name_fl = "input_flow_logs.txt"
    file_name_lt = "lookup_table.csv"
    process_flows_obj.match_flow_to_tag(lookup_table=file_name_lt, input_flow_logs=file_name_fl)
    
    # ensure lookup_map is not empty
    assert process_flows_obj.lookup_map is not None
    assert len(process_flows_obj.lookup_map) == 11

    # ensure flow_log_list is not empty
    assert process_flows_obj.flow_log_list is not None
    assert len(process_flows_obj.flow_log_list) == 14

def test_create_lookup_map_valid_input(process_flows_obj):
    input_list = ['', '25,tcp,tag1', '80,udp,sv_P2']
    map = process_flows_obj.create_lookup_map(input_list)
    assert len(map) == len(input_list)-1 # the first row is skipped as it is column names   

def test_create_lookup_map_invalid_input(process_flows_obj):
    input_list = ['', '25,tcp', '80,udp,sv_P2']
    # second item in the list has 2 comma separated values instead of 3
    map = process_flows_obj.create_lookup_map(input_list)
    assert len(map) == len(input_list)-2

def test_create_lookup_map_empty_list(process_flows_obj):
    input_list = []
    map = process_flows_obj.create_lookup_map(input_list)
    assert len(map) == len(input_list)

def test_create_flow_log_list_valid_input(process_flows_obj):
    input_list = ['2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK', '2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK', '2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK']
    flow_log_list = process_flows_obj.create_flow_log_list(input_list)
    assert len(flow_log_list) == len(input_list)

def test_create_flow_log_list_empty_list(process_flows_obj):
    input_list = []
    flow_log_list = process_flows_obj.create_flow_log_list(input_list)
    assert len(flow_log_list) == len(input_list)





    


    
