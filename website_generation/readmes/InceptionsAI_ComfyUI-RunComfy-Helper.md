# ComfyUI-RunComfy-Helper
## Usage
- curl http://localhost:8188/runcomfy/workflows
- curl -X POST http://localhost:8188/runcomfy/workflows \
     -H "Content-Type: application/json" \
     -d '{
           "workflows": [
             {
               "file_name": "file1.json",
               "workflow": {
                 "exampleKey": "exampleValue"
               },
               "default":true
             }
           ]
         }'
## Config
```
{
	"workflows": {
		"directory": "runcomfy/workflows",
		"default": "default.json"
	},
	"logging":true
}
```
