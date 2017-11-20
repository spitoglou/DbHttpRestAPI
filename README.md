# Generic Database Http API


## Installation
I strongly recommend using Anaconda for python module and dependency management. 
#### Linux
```commandline
conda env create -f linux_environment.yml  
source activate dbapi
```
#### Windows
```commandline
conda env create -f environment.yml  
activate dbapi
```

##Usage
#### Run the server
Once the dependencies are installed, you can run `python run.md` from the root directory.  
By default it will run in debug mode, but you can change that in the `config.py` file:
```python
DEBUG = False
```
#### Queries
Once the server is up and running, you can query any database it has network access to 
by issuing a `POST` http request against the `/query` endpoint.

You must supply a `Content-Type` header with value `application/json` and the body of the request must be a properly formatted JSON object:
```json
{
	"host": "[database ip:port]",
	"user": "[username]",
	"password": "[password]",
	"db": "[schema name]",
	"charset": "[charset e.g. utf8 ]",
	"query": "[query e.g. select * from users]"
}
```

##Author
Stavros Pitoglou
