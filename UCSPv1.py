#!/usr/bin/python&amp;amp;amp;amp;amp;lt;/code&amp;amp;amp;amp;amp;gt;
 
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
 
def myNetwork():
 
	net = Mininet( topo=None,
		listenPort=6653,
		build=False,
		ipBase='10.0.0.0/8',
	link=TCLink)
 
	info( '*** Anadiendo controlador\n' )

	c0=net.addController(name='c0',
			controller=RemoteController,
			protocol='tcp', protocols='OpenFlow13', ip='127.0.0.1')
 
	info( '*** Creando Switches\n')
	
	s2 = net.addSwitch('s2', cls=OVSKernelSwitch, mac='00:00:00:00:00:09', protocols='OpenFlow13')
	s1 = net.addSwitch('s1', cls=OVSKernelSwitch, mac='00:00:00:00:00:08', protocols='OpenFlow13')
 
	info( '*** Creando hosts\n')
	h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None, mac='00:00:00:00:00:07')	
	h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None, mac='00:00:00:00:00:06')	
	h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None, mac='00:00:00:00:00:05')
	h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None, mac='00:00:00:00:00:04')	
	h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None, mac='00:00:00:00:00:03')
	h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None, mac='00:00:00:00:00:02')
	h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None, mac='00:00:00:00:00:01')
 
	info( '*** Creando Enlaces\n')
	net.addLink(s2, s1, bw=10, delay='0.2ms')
	
	net.addLink(s2, h7, cls=TCLink, bw=10)	
	net.addLink(s2, h6, cls=TCLink, bw=10)
	net.addLink(s2, h5, cls=TCLink, bw=10)
	net.addLink(s2, h4, cls=TCLink, bw=10)
	net.addLink(s2, h3, cls=TCLink, bw=10)
	net.addLink(s2, h2, cls=TCLink, bw=10)
	net.addLink(s1, h1, cls=TCLink, bw=10)
 

	info( '*** Iniciando la red\n')
	net.build()
	info( '*** Iniciando controladores\n')
	for controller in net.controllers:
		controller.start()
 
	info( '*** Iniciando switches\n')
	
	net.get('s2').start([c0])
	net.get('s1').start([c0])
 
	info( '*** Configuraciones posteriores\n')
 
	CLI(net)
	net.stop()

 
if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
