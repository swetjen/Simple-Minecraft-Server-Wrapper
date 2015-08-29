import time, subprocess


class ServerManager(object):

    def __init__(self, path, server_file, xms=1, xmx=1, gui=False):
        self.process = None
        self.path = path
        self.server_file = server_file
        self.online = False
        self.xms = xms
        self.xmx = xmx
        self.gui = gui

    def start(self):
        command = 'java -jar -Xms' + str(self.xms) + 'G -Xmx' + str(self.xmx) + 'G ' + self.path + '' + self.server_file
        if not self.gui: command += ' nogui'
        print '--- Started server with command: ' + command
        if self.path == '':
            self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
        else:
            self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, cwd=self.path)
        self.online = True
        print self.process

    def shutdown(self):
        self.message('New version detected, server will be shutting down for maintenance in 1 minute.')
        time.sleep(30)
        self.message('Shutting down for maintenance in 30 seconds.')
        time.sleep(20)
        self.message('Shutting down for maintenance in 10 seconds.')
        self.message('Have some diamonds for the trouble.')
        self.message('give @a minecraft:diamond 5', True)
        time.sleep(10)
        self.message('stop', True)
        self.online = False
        self.process.terminate()
        time.sleep(5)

    # Server chat can be passed as ServerManager.message('hello')
    def message(self, message, command=False):
        print self.process
        if not command:
            self.process.stdin.write('say ### SMSW Message: \n')
            self.process.stdin.flush()
            self.process.stdin.write('say ' + message + '\n')
            self.process.stdin.flush()
        else:
            self.process.stdin.write(message + '\n')
            self.process.stdin.flush()
