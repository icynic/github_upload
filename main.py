import requests
import base64
import json

# --- Required information --- #
token ="YOUR-TOKEN"
user="USER-NAME"
repository="REPOSITORY-NAME"
online_path="UPLOAD-DIRECTORY"
message="a new commit message"
local_file_path="FILE-TO-UPLOAD"


# Open the local file (as bytes), get its name and content
with open(local_file_path, "rb+") as file:
    file_name=file.name
    file_content=file.read()

    # Form the URL, header
    url = f"https://api.github.com/repos/{user}/{repository}/contents/{online_path}/" + file_name
    headers = {"Authorization": "token " + token}
    # Encode the file content in base64, then convert it to a string
    content=base64.b64encode(file_content).decode('utf-8')
    # Form the data to upload
    data = {
        "message": message,
        "content": content
    }
    data = json.dumps(data)
    # Send the request
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    # Load response text
    re_data = json.loads(req.text)
    print(req.status_code)
    print(re_data['content']['html_url'])

# icynic

