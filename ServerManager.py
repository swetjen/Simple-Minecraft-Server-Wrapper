import time, subprocess

class ServerManager:

    def __init__(self, path, server_file, xms=1, xmx=1, gui=False):
        self.path = path
        self.server_file = server_file
        self.online = False
        self.xms = xms
        self.xmx = xmx
        self.gui = gui


    def start(self):
        global process
        command = 'java -jar -Xms' + str(self.xms) + 'G -Xmx' + str(self.xmx) + 'G ' + self.path + self.server_file
        if self.gui == False: command += ' nogui'
        print command
        if self.path !='':self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, cwd=self.path)
        if self.path =='':self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
        self.online = True
        return

    def shutdown(self):
        self.message('New version detected, server will be shutting down for maintenance in 1 minute.')
        time.sleep(30)
        self.message('Shutting down for maintenance in 30 seconds.')
        time.sleep(20)
        self.message('Shutting down for maintenance in 10 seconds.')
        self.message('Have some diamonds for the trouble.')
        self.message('give @a minecraft:diamond 5', true)
        self.online = False
        self.process.terminate()
        del process
        return

    #Server chat can be passed as ServerManager.message('hello')
    def message(self, message, command=False):
        
        if command == False:
            self.process.stdin.write('### SMSW Message: ')
            self.process.stdin.flush()
            self.process.stdin.write(message)
            self.process.stdin.flush()
        else:
            self.process.stdin.write(message)
            self.process.stdin.flush()
        return
            
        
        
        
        
