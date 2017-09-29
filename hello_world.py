class Message():
	def __init__(self, question):
		"""存储一个问题，并为存储的问题准备答案"""
		self.question = question
		self.responses = []
		
	def show_question(self):
		"""显示调查问卷"""
		print(self.question)
		
	def store_response(self, response = ''):
		"""存储一个问题，并为存储的问题准备答案"""
		if response:
			self.responses.append(response)
		else:
			response = input("Language: ")
			if response == 'q':
				return False
			else:
				self.responses.append(response)
				return True
		
	def show_response(self):
		print("Survey results: ")
		for response in self.responses:
			print("- " + response.title())
"""			
question = "What language did you first learn to speak?"
message = Message(question)
message.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	flag = message.store_response()
	if flag:
		pass
	else:
		break
	
print("\nThank you everyone who participated in the survey!")
message.show_response()

	"""	
	