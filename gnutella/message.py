from random import randint

class Message:
    payload_byte_to_string = {
        b"\x00": "ping", 
        b"\x01": "pong", 
        b"\x02": "bye", 
        b"\x40": "push", 
        b"\x80": "query", 
        b"\x81": "query hit"
    }

    payload_int_to_string = {
        0: "ping", 
        1: "pong", 
        2: "bye", 
        64: "push", 
        128: "query", 
        129: "query hit"
    }

    payload_string_to_byte = {
        "ping": b"\x00", 
        "pong": b"\x01", 
        "bye": b"\x02", 
        "push": b"\x40",
        "query": b"\x80",
        "query hit": b"\x81"
    }

    @staticmethod
    def __number_to_bytes(num, bytes):
        ints = []
        for byte_index in range(bytes):
            divisor = 2**(8*byte_index)
            modulus = 2**(8*(byte_index+1))
            i = (num // divisor)%modulus
            ints.append(i)
        return bytes(ints)

    @staticmethod
    def __bytes_to_number(bytes):
        return sum([2**(8*idx) * bytes[idx] for idx in range(len(bytes))])
    
    @staticmethod
    def __generate_msgid(seed = None):
        if seed is None: # for testing
            random_numbers = [randint(0, 255) for i in range(14)]
        else: random_numbers = seed
        msgid = bytes(random_numbers[:8] + [255] + random_numbers[8:] + [0])
        return msgid

    @staticmethod
    def __construct_header(msgid, payload_type, ttl, hops, payload_length):
        payload_type_bytes = Message.payload_string_to_byte[payload_type]
        if msgid is None: 
            msgid = Message.__generate_msgid()
        
        header = msgid + payload_type_bytes
        header += bytes([ttl, hops])
        header += Message.__number_to_bytes(payload_length, 4)
        return header

    @staticmethod
    def constructPong(address, keywords, ttl, hops):
        pong_payload = Message.__number_to_bytes(address[1], 2)
        # then the IP
        IP = [int(i) for i in address[0].split(".")]
        pong_payload += bytes(IP)
        # and the shared files and data
        pong_payload += Message.__number_to_bytes(keywords, 4)
        # we use no GGEP extension, so we’re finished with building the pong payload.

        # now we have the payload length, so we can get it and use it to create the header. 
        pong_payload_length = len(pong_payload)
        pong = Message.__construct_header(None, "pong", ttl, hops, pong_payload_length)
        pong += pong_payload   
        
        return pong