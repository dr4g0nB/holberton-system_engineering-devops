# HTTPS SSL

### Learning Objectives
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

### :file_folder: Tasks
Directory | Language
----- | -----
0 | Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
1 | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.
2 |  Configure HAproxy to automatically redirect HTTP traffic to HTTPS
