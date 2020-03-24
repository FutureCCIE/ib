import copy
import requests
import json
import xml
requests.packages.urllib3.disable_warnings()
import base64

class ib_test(object):
	def __init__(self):
		# store creds & and globally shared attributes inside  __init__
		self.username = _REDACTED_
		self.password = _REDACTED_
		self.site = 'https://site_url/wapi'
		self.version = '/v2.9.1/'
		self.url = self.site + self.version
		self.session = requests.Session()
		self.params = {
		'_max_results':'100',
		'_paging':'1',
		'_return_as_object':'1',
		#'Content-Type':'Application/json',
		}
		# dns variables used for get, post, and blah
		# note that 'name' is used when the user doesn't know what record type to use
		self._dns_types_ = {
		'arecord':'a?',
		'cname':'cname?',
		'zone':'zone?',
		'name':'name',
		'allrecords':'allrecords?',
		}
		# compound _searching_ in dns
		self._allrecords_in_zone_ = self._dns_types_['allrecords'] + self._dns_types_['zone']
		# basic dhcp url variables
		self._ipam_types_ = {
		'host':'host?name',
		'network':'network?',
		'ip':'ipv4address?',
		}
		# basic dhcp url variables
		self._dhcp_types_ = {
		'dhcp_network':'metwork?',
		'dhcp_range':'',
		'dhcp_range_attributes':'',
		'dhcp_range_servers':'',
		}
		# dhcp admin url variables
		self._admin_types_ = {
		'blah':'blah',
		}
		self._repcrting_types_ = {
		'blah':'blah',
		}
		# equality for all variables
		self._search_ = {
		'generic-search':'~=',
		'specific-search':'=',
		}
		self._record_ = 'record:'
		self.path_values = []
		self.final_path_values = ()
		self.main_dict = {}
		return
	# authentication function
	def authentication(self):
		self.session = requests.Session()
		un_pw = f'{self.username}:{self.password}'.encode()
		un_pw_b64 = base64.b64encode(un_pw).decode()
		auth_headers = {'Authorization': f'Basic {un_pw_b64}'}
		self.session.headers.update(auth_headers)
		return
	# base query used to query with the compiled final_path_values into a query
	# used to query type check
	def _options_(self, input):
		if input == 'dns':
			self.path_values.append(self._record_)
			#print(f'[x]you are querying for {input}')
			self.get_dns_req(input)
		if input == 'ipam':
			self.path_values.append(self._record_)
			#print(f'[x] you are querying for {input}')
			self.get_ipam_req(input)
		if input == 'dhcp':
			#print(f'[x] you are querying for {input}')
			self.get_dhcp_req()
		if input == 'admin':
			#print(f' [x] you are querying for {input}')
			self.get_admin_req()				
		return
	# basic dns option compiling
	def get_dns_req(self, input):
		for x in self._dns_types_:
			if input == x:
				print(f'[x] appending {self._dns_types_[x]} to query string')
				self._searching_(self._dns_types_[x])
				self._searching_(self._search_)
		return
	# basic ipam option compiling
	def get_ipam_req(self, input):
		for x in self._ipam_types_:
			if input == x:
				#print(f'[x] appending {self._ipam_types_[x]} to query string')
				self._searching_(self._ipam_types_[x])
				#self._searching_(self._search_)
		return	
	def search_type(self, input):
		for x in self._search_:
			if input == x:
				#print(f'[x] appending {self._search_[x]} to query string')
				self._searching_(self._search_[x])
		return
	# basic dhcp option compiling
	def get_dhcp_req(self):
			
		self.searchin()
		return
	# basic dhcp option compiling
	def get_admin_req(self):
		
		self.searchin()
		return
	# basic dhcp option compiling
	def get_reporting_req(self):
		
		self.searchin()
		return
	# basic final compiling for basic get request
	def _searching_(self, input):
		if input != self._dns_types_ or self._ipam_types_:
			self.path_values.append(input)
			#print(f'[x] appending {input} to query string')
			self._final_parsing_()
		return
	# well gotta make it look pretty before the GM sees it :)
	def _final_parsing_(self):
		temp = ''
		self.final_path_values = temp.join(self.path_values)
		self.base_get_req()
		#print(f'your query string prior to cleaning {self.path_values}')
		return
	def base_get_req(self):
		response = self.session.get(
		f'{self.url}{self.final_path_values}',
		params=self.params,
		verify=False
		)
		if response.status_code == 200:
			response_json = json.loads(response.text)
			self.main_dict = response_json['result']
			print(f'your output is stored in main_dict {self.main_dict}')
			print(f'your querying url is\n{self.url}{self.final_path_values}\n')
		#elif response.status_code == 400:
			#print(f'your life sucks, and this why you stupid retard:{response.text}\r')
		return
	def post_get_parsing(self):
		for x in self.main_dict[0:]:
			_ref_ = x['_ref']
			_split_ref_ = _ref_.split('/')
			print(_split_ref_)
		return
		
if __name__ == '__main__':
	ib_test = ib_test()
