class message:
    def __init__(self,sender,reciver,content): 
        self.sender =sender
        self.reciver =reciver
        self.content =content

message_one=message("nasr","addo","hello")
message_two=message("ahmed","nasr","hi")
print(f"sender:{message_one.sender} reciver:{message_one.reciver} {message_one.content}")
print(f"sender:{message_two.sender} reciver:{message_two.reciver} {message_two.content}")
