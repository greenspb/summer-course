curl http://20.127.202.175:8000 | Format-Table -Wrap -AutoSize # PS
curl http://20.127.202.175:8000 | less #unix
curl 20.127.202.175:8000
curl -H "X-Username: chief.engineer" -H "X-Password: ares-vallis-7" http://20.127.202.175:8000 

import requests
headers = {'X-Username': "chief.engineer", 'X-Password': "ares-vallis-7"}
response = requests.get("http://20.127.202.175:8000", headers=headers)
print(response.reason, response.status_code)
print(response.text)

ssh chief.tech@20.127.202.175
#1000-souls-aboard

#   [1] Telemetry systems      -> Python Problem 1
#   [2] Food resource recalc   -> Python Problem 2
#   [3] Emergency comms rocket -> Python Problem 3
#   [4] Submit solutions       -> pull request
#   [5] Broadcast beacon       -> host a site from your VM

#mkdir filename{1..100} #This command makes 100 directories.

ls
#cd mission
#cat the_answers.txt
#cd Folder1 
grep -r "telemetry" # Find the location of file mentioning telemetry.
grep -R "telemetry"


#either
#cat mission/Folder1/Folder22/Folder26/telemetry_python_problem1.txt
# or
grep -rl "telemetry" | xargs cat

#problem 2
grep -r "resource" 
grep -R "resource"
#grep -rl "resource" | xargs cat
cat mission/Folder1/Folder37/Folder86/resource_pythonProblem2.txt

#Problem 3
cd / #Root folder
cd Problem3
cat problem3_statement.txt 
