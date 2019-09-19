#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : upload_file.py
@time : 2019/09/20 01:30:15
@func : 
"""

# python连接远程服务器，发送文件
import paramiko
def ssh_scp_put(ip, port, user, password, local_file, remote_file):
    """
    :param ip: 服务器ip地址
    :param port: 端口(22)
    :param user: 用户名
    :param password: 用户密码
    :param local_file: 本地文件地址
    :param remote_file: 要上传的文件地址（例：/test.txt）
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)

    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
if __name__ == '__main__':

    ip=''
    port='22'
    user=''
    password=''
    local_file=r'D:\PycharmProjects\flask_test\github-branch-test\闭包00.py'
    remote_file=r'/root/homework/闭包00.py'

    ssh_scp_put(ip, port, user, password, local_file, remote_file)