docker build -t Docker-agent:latest .

docker run -d --name Docker-agent Docker-agent:latest

     docker run -d --name docker-agent   --privileged  --network jenkins-net  -e JENKINS_URL=http://jenkins-master1:8080 -e JENKINS_SECRET=450cd749dbd6f7acfc2058e91dea35865bb63ddd77a581c5c6a2e5799be2f750 -e JENKINS_AGENT_NAME="docker-agent" -v docker-agent-data:/home/jenkins   -v /var/run/docker.sock:/var/run/docker.sock   docker-agent:latest
