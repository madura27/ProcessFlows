from process_flows import ProcessFlows


def main():
    print("Welcome!")
    print("Time to process the input flows and tag them!")
    lookup_table_file_name = "lookup_table.csv"
    input_flow_logs_file_name = "input_flow_logs.txt"

    tag_count_file_name = "tag_count.txt"
    port_protocol_count_file_name = "port_protocol_count.txt"

    
    process_flows = ProcessFlows()
    process_flows.match_flow_to_tag(lookup_table = lookup_table_file_name, input_flow_logs = input_flow_logs_file_name)

    print("Getting the tag count for the input flows")
    process_flows.get_tag_count_and_output_to_file(tag_count_file_name)
    print("Please check file ../output_files/" , tag_count_file_name,"to view the tag counts")

    print("#################################")

    print("Getting the port protocol count for the input flows")
    process_flows.get_port_protocol_count_and_output_to_file(port_protocol_count_file_name)
    print("Please check file ../output_files/",port_protocol_count_file_name, "to view the port protocol counts")

    print("Thank you!")

if __name__ == "__main__":
    main()



