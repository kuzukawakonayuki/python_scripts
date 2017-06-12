import pyshark


for p in pyshark.FileCapture(pcap_file, display_filter='http'):
        try:
            if p.http.request_method == 'GET':
                print(p.eth.src)
                print(p.eth.dst)
                print(p.ip.src)
                print(p.ip.dst)
                print(p.tcp.srcport)
                print(p.tcp.dstport)
                print(p.http.host)
                print(p.http.request_full_uri)
                print(p.sniff_time)
        except AttributeError as e:
            continue