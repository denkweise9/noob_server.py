#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# work in progress
# inspired by David Beazley, with intent to improve and replace socket module with asyncoro
# client and server coroutines communicating with message passing
# (asynchronous concurrent programming);
# see http://asyncoro.sourceforge.net/tutorial.html for details.
# introduced here is the simple concept of "co-routine stacking', example at bottom


'''
    noob_server.py is for async co-routine networking.
    Copyright (C) 2017      Authors: Denkweise9, Lvl4Sword, David Beazely
    The event loop class was taken from a pycon talk and credit is given
    to David Beazely
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see https://www.gnu.org/licenses/.
'''

try:
    import asyncio, asyncoro, socket  
    # The following below is for event loops
    from types import coroutine
    from collections import deque
    from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
except(ImportError):
    facts=r"""
        You are missing dependencies for networking!
        Please make sure you have the following:
                    asyncoro
           """
    print(facts)
    sys.exit()



loop = asyncio.get_event_loop()
socket_object = asyncoro.socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

def execute(func):
    return loop.run_until_complete(func) 

def Execute(func): #this uses the alternative loop handler
    return Loop.run_forever(func)

#Need to add 
def networking_client(object):
    async def send_data(address, data):
        self.sock = socket_object
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.send(bytes(str(data),'utf-8'))
        self.sock.setblocking(False)
        while self.sock:
            address, data = await self.loop.socket_accept(sock)  #this is using asyncio, we have Loop if needed
            print("Connection started with {0}".format(address))
            self.loop.create_task(resp_handler(client))

    async def echo_server(address):  # this requires sockets atm.
        self.sock = socket.socket(AF_INET, SOCK_STREAM)
        self.sock.setsockop(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(5)
        self.sock.setblocking(False)
        while True:
            client, addr = await self.loop.sock_accept(sock)
            print("Connection Established from {}".format(addr))
            self.loop.create_task(echo_handler(client))

    async def resp_handler(client):
        with client:
            while client:
                data = await self.loop.sock_recv(client, 10000)
                if not data:
                    break
                    self.socket.close()
                else:
                    await self.loop.sock_sendall(client, b"Received: " + data)
        print("Connection closed")




    def receive(self):
        data = []
        bytes_recv = 0
        while bytes_recv < message_len:
            chunk = self.socket.recv(min(message_len - bytes_recv, 2048))
            if chunk == b'':
                raise RuntimeError("Socket is dead")
            chunks.append(chunk)
            bytes_recv = bytes_recv + len(chunk)
        return b''.join(chunks)


    def send(self, host, port, data):
        total_packets = 0
        while (data is not None) and (total_packets < data):
            try:
                address = (host, port)
                socket = self.asyncoro.socket.create_connection(address)    
                sent = self.socket.send(bytes('{}'.format(data[total_packets:]), 'utf-8'))
                if sent == 0:
                    raise RuntimeError("Socket connection is empty or broken")
                total_packets = total_packets + sent
            except(ConnectionRefusedError):
                self.socket.close()
                sys.exit()

    def send_json_new(self, address):
         pass #pass for now, will update        




# The following is a slightly edited event loop created by David Beazley
# It can replace asyncio.get_event_loop() for certain tasks
# noob_serv intends to use this base for improved event handling, and improve the event loop.

@coroutine
def read_wait(sock):
    yield 'read_wait', sock

@coroutine
def write_wait(sock):
    yield 'write_wait', sock


class Loop(object):
    def __init__(self):
        self.ready = deque()
        self.selector = DefaultSelector

    async def sock_recv(self, sock, maxbytes):
        await read_wait(sock)
        return self.sock.recv(maxbytes)

    async def sock_accept(self,sock):
        await read_wait(sock)
        return self.sock.accept()

    async def sock_sendall(self, sock, data):
        while data:
            await write_wait(sock)
            self.nsent = sock.send(data)
            self.data = data[nsent:]

    def create_task(self, coro):
        self.ready.append(coro)

    def read_wait(self, sock):
        self.selector.register(sock, EVENT_READ, current_task)

    def write_wait(self, sock):
        self.selector.register(sock, EVENT_WRITE, current_task)
        


    def run_forever(self):
        while True:
            while not self.ready:
                self.events = selector.select()
                for key, _ in events:
                    self.ready.append(key.data)
                    self.selector.unregister(key.fileobj)
        while self.ready:
            self.current = ready.popleft()
            try:
                self.op, self.args = ready.popleft()
                getattr(op)(args)
                self.val = current_task.send(None)
            except(StopIteration):
                pass

            
'''
  
import asyncio
loop = asyncio.get_event_loop()

#we make a simple function using co-routine loop calls on whatever passed
def execute(coroutine_object):
    return loop.run_until_complete(coroutine_object)



In [450]: async def there(func):      
     ...:     greet = await func   # we await for the function call
     ...:     if greet:
     ...:         return greet, 'there' 

In [446]: async def foo(func):
     ...:     word = await func
     ...:     if word:
     ...:         return word, 'foo'


execute(foo(there(hello())))  #  <--- this proves we can stack event loops into a single call. Why aren't more doing this?

execute works on 1 co-routine, or 100 co-routines.
if conditions are contained within co-routines, execute will follow those conditons for you.
#output
(('hello ', 'there'), 'foo')


# Although async looks stupid when being used to say 'hi', it solves a huge amount of problems
# where you need concurrency and asynchronous actions in things like networking


usually I see the following used

if __name__ == '__main__':
   loop.run_until_complete(coroutine_object_0)
   loop.run_until_complete(coroutine_object_1)
   loop.run_until_complete(coroutine_object_2)
   loop.run_until_complete(coroutine_object_3)

  '''
