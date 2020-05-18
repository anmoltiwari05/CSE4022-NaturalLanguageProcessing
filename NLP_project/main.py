
print("Bot> Please wait, while I am loading my dependencies")
from Model import Model as DRM
from ProcessQuestion import ProcessQuestion as PQ
import re
import sys

if len(sys.argv) == 1:
	print("\t\t please run the code with this syntax '$ python3 P2.py <datasetName>'")
	print("Bot> You can find dataset name in \"dataset\" folder")
	exit()

datasetName = sys.argv[1]
# Loading Dataset
try:
	datasetFile = open(datasetName,"r", encoding='utf8')
except FileNotFoundError:
	print("Bot> Oops! I am unable to locate \"" + datasetName + "\"")
	exit()


paragraphs = []
for para in datasetFile.readlines():
	if(len(para.strip()) > 0):
		paragraphs.append(para.strip())


drm = DRM(paragraphs,True,True)

print("Bot> Hey! I am ready. Ask me a question ?")
print("Bot> You can say bye to me anytime you want")


greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.IGNORECASE)

isActive = True
while isActive:
	userQuery = input("You> ")
	if(not len(userQuery)>0):
		print("Bot> You need to ask something")

	elif greetPattern.findall(userQuery):
		response = "Hello!"
	elif userQuery.strip().lower() == "bye":
		response = "Bye Bye!"
		isActive = False
	else:
		pq = PQ(userQuery,True,False,True)

		response =drm.query(pq)
	print("Bot>",response)
