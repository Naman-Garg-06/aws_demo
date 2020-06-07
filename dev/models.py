from django.db import models

# Create your models here.
class metrics(models.Model):
	attribute_i = ['Attr_1','Attr_2','Attr_3','Attr_4','Attr_5']
	val = [0 for idx in range(5)]
	def __init__(self, values):
		for idx in range(5):
			self.val[idx] = values[idx]
	
	def attributes(self,list_of_attributes):
		attr = dict()
		for attribute in list_of_attributes:
			attr[self.attribute_i[attribute]] = self.val[attribute]
		return str(attr)

class metadata(models.Model):
	instance_id = ""
	instance_type = ""
	public_ipv4 = ""
	ami_id = ""
	hostname = ""
	def __init__(self,a,b,c,d,e):
		self.instance_id = a
		self.instance_type = b
		self.public_ipv4 = c
		self.ami_id = d
		self.hostname = e
	def response(self):
		return_type = dict()
		return_type['instance_id'] = self.instance_id
		return_type['instance_type'] = self.instance_type
		return_type['public_ipv4'] = self.public_ipv4
		return_type['ami_id'] = self.ami_id
		return_type['hostname'] = self.hostname
		return str(return_type)