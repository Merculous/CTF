#!/usr/bin/env python3

import paramiko


class Connect:
    host = 'bandit.labs.overthewire.org'

    def __init__(self, user: str, password: str, port: int = 2220) -> None:
        self.user = user
        self.password = password
        self.port = port

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            look_for_keys=False,
            allow_agent=False
        )

    def runCommand(self, command):
        return self.client.exec_command(command)

    def closeConnection(self):
        self.client.close()


def format(data) -> str:
    return data.decode('utf-8').strip()


def level1() -> str:
    c = Connect('bandit0', 'bandit0')
    (cmd_in, cmd_out, cmd_err) = c.runCommand('cat readme')
    password = format(cmd_out.read())
    c.closeConnection()
    return password

level1_pass = level1()
print(level1_pass)
