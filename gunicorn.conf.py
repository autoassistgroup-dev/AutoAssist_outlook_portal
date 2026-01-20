# Gunicorn Configuration for AutoAssistGroup Support System
# Railway / Container Deployment

import multiprocessing
import os

# Server socket
# Bind to 0.0.0.0 (required for containers) on default port 8000
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
# For containers, static number or CPU-based is fine. 4 is a good safe default.
workers = 4
# Use 'gthread' worker - stable and doesn't require gevent dependency
worker_class = "gthread"
threads = 4
worker_connections = 1000
timeout = 120
keepalive = 2

# Logging
# Log to stdout/stderr for Docker/Railway
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "autoassist_support"

# Server mechanics
daemon = False
# REMOVED: pidfile, user, group (Incompatible with serverless/containers)

# Environment variables
raw_env = [
    'FLASK_ENV=production',
]

# Preload app for better performance
preload_app = True

# Forwarded allow ips (allows all for container network)
forwarded_allow_ips = "*"
