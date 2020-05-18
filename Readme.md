# Flask Celery Docker container example.

## 1. How to use celery with flask web API backend to handle long running programs     

### 1. Setup Celery in flask app  
        celery_app = Celery('module', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
    
  - 'module' - is the name of the worker ,
  - Broker is Redis endpoint 
  - backend is Redis endpoint 
  
### 2. Setup Celery worker in normal way (without a module )

   - check simple_worker folder. 
   
### 3. Setup Celery worker as python module 

   - check module worker 
   - inside module worker , there would be a python module called "module"
   - setup celery and link tasks for this worker (celery.py) 
   
### 4 . Usecase 

   - use in case when workers code does not need to be shared, separate Queues to be maintained  
   - control auto scaling independent of the worker.
   - scale docker containers ??