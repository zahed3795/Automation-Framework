import os

cmd = os.system

install_g_express = 'npm install -g express'
npm_install = 'npm install'
nodeJS = 'node server.js'
list = [install_g_express, npm_install, nodeJS]

for j in list:
    cmd("cmd /k " + j)
