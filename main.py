import tweepy


def setup_api(direct):

	#load up credentials
	f = open(direct, "r")
	CONSUMER_KEY = f.readline().strip()
	CONSUMER_SECRET = f.readline().strip()
	ACCESS_KEY =  f.readline().strip()   
	ACCESS_SECRET =  f.readline().strip()
	f.close()

	# handle authentication
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

	return tweepy.API(auth)

def main():

	api = setup_api("../zine_creds")
	#api.update_status('Test tweet')

	# the ID of the status
	id = 1272771459249844224
	  
	# fetching the status
	user = api.get_status(id)
	  
	# fetching the created_at attribute
	created_at = user.created_at 
	  
	print("The status was created at : " + str(created_at))

if __name__ == '__main__':
	main()