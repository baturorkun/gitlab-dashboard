#!/bin/bash

GL_DOMAIN="https://gitlab.example.com"
GL_TOKEN="xxxxxxxxxxxxx"

echo "" > gitlab_projects.txt

for ((i=1; ; i+=1)); do
    contents=$(curl "$GL_DOMAIN/api/v4/projects?private_token=$GL_TOKEN&per_page=100&page=$i")
    if jq -e '. | length == 0' >/dev/null; then
       break
    fi <<< "$contents"
    echo "$contents" | jq -r '.[] | [.name,.path_with_namespace,.ssh_url_to_repo] | join("|")' >> gitlab_projects.txt
done