import requests


def shorten_url(long_url, custom_url=None):
	"""
	Shortens a long URL using the TinyURL API and returns the shortened URL.
	If a custom URL is provided, attempts to customize the shortened URL accordingly.
	"""
	# Define the TinyURL API endpoint
	endpoint = "https://tinyurl.com/api-create.php"

	# Build the request parameters
	params = {"url": long_url}

	if custom_url:
		params["alias"] = custom_url

	try:
		# Send the request to the TinyURL API
		response = requests.get(endpoint, params=params)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
		return None

	# Check the status code and return the shortened URL
	if response.ok:
		return response.text
	else:
		print(f"An error occurred: {response.status_code}")
		return None


# Prompt the user to enter a long URL and a custom URL (optional)
long_url = input("Enter a long URL: ")
custom_url = input("Enter a custom URL (optional): ")

# Shorten the URL using TinyURL and customize if requested
if custom_url:
	short_url = shorten_url(long_url, custom_url)
else:
	short_url = shorten_url(long_url)

# Display the shortened URL if it exists
if short_url:
	print(f"Shortened URL: {short_url}")
else:
	print("Unable to shorten URL.")
