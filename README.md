# DataDescriptorAPI

You can start to build the streams-api docker container locally.
```
docker build -t dd-api:latest .
```

Or to just test the API without dependencies:
```
docker run -p 5000:5000 dd-api:latest
```

You can then go to localhost:5000/hello etc...

## Development
Developing you have to rebuild and redeploy the container when you make changes. To make this easier you can use this chained command that stops the container instance, removes it, rebuilds the container and starts a new instance.

Windows:

docker stop ddapi && docker build -t dd-api:latest . && docker rm ddapi && docker run -p 5000:5000 --name=ddapi dd-api:latest

Linux/Max:

docker stop ddapi ; docker build -t dd-api:latest . ; docker rm ddapi ; docker run -p 5000:5000 --name=ddapi dd-api:latest


## Running tests
1.) Before you start running the tests you will need to add the following to the config-local.json file for the tests with working username & password for the tenant you are testing against for the other Tapis services(sk,meta etc)
 ```
     "test_tenant_id" : "dev",
     "test_username" :"testusername",
     "test_password" :"testpassword"
 ```
2.) Build the tapis/streams-api docker container:  
```
docker build -t dd-api:latest .
```
3.) Build the test docker image:
```
docker build -t dd-tests -f Dockerfile-tests .
```
4.) Run these tests using the built docker image:
```
docker run -it --rm --name=dd-test -p 5000:5000 dd-tests
```


# DataDescriptorAPI Schema
An API for creating, updating, deleting, and retrieving Data Descriptors

Data Descriptor schema:
```
    {
      "title" : "DataDescriptor",
      "description" : "Information needed to describe a piece of data",
      "type" : "object",
      "ikewai" : true,
      "properties" : {
        "title" : {
          "title" : "Title ",
          "type" : "string"
        },
        "organizations" : {
          "type" : "array",
          "title" : "Organization(s)",
          "items" : {
            "type" : "object",
            "properties" : {
              "name" : {
                "type" : "string"
              },
              "uuid" : {
                "type" : "string"
              }
            }
          }
        },
        "creators" : {
          "type" : "array",
          "items" : {
            "type" : "object",
            "properties" : {
              "first_name" : {
                "type" : "string"
              },
              "last_name" : {
                "type" : "string"
              },
              "email" : {
                "type" : "string"
              },
              "organization" : {
                "type" : "string"
              },
              "phone" : {
                "type" : "string"
              },
              "uuid" : {
                "type" : "string"
              }
            }
          }
        },
        "formats" : {
          "type" : "array",
          "items" : {
            "title" : "Format",
            "type" : "string"
          }
        },
        "subjects" : {
          "type" : "array",
          "title" : "Subject(s)",
          "items" : {
            "type" : "string"
          }
        },
        "data_states" : {
          "type" : "array",
          "title" : "Data State(s)",
          "items" : {
            "type" : "string"
          }
        },
        "data_types" : {
          "type" : "array",
          "title" : "Data Type(s)",
          "items" : {
            "type" : "string"
          }
        },
        "contributors" : {
          "type" : "array",
          "items" : {
            "type" : "object",
            "properties" : {
              "first_name" : {
                "type" : "string"
              },
              "last_name" : {
                "type" : "string"
              },
              "email" : {
                "type" : "string"
              },
              "organization" : {
                "type" : "string"
              },
              "phone" : {
                "type" : "string"
              },
              "uuid" : {
                "type" : "string"
              }
            }
          }
        },
        "contributors_agency" : {
          "type" : "array",
          "items" : {
            "type" : "object",
            "properties" : {
              "name" : {
                "type" : "string"
              },
              "uuid" : {
                "type" : "string"
              }
            }
          }
        },
        "license_rights" : {
          "title" : "License Rights",
          "type" : "string"
        },
        "license_permission" : {
          "title" : "License Permissions",
          "type" : "string"
        },
        "subject" : {
          "title" : "Subject",
          "type" : "string"
        },
        "start_datetime" : {
          "title" : "Start Date",
          "type" : "string"
        },
        "end_datetime" : {
          "title" : "End Date",
          "type" : "string"
        },
        "description" : {
          "title" : "Description",
          "type" : "string"
        },
        "relations" : {
          "title" : "Relations",
          "type" : "string"
        },
        "language" : {
          "title" : "Language",
          "type" : "string"
        },
        "publisher" : {
          "type" : "string",
          "title" : "Publisher"
        },
        "date_published" : {
          "title" : "Date Published",
          "format" : "date-time",
          "type" : "string"
        },
        "project_type" : {
          "title" : "Project Type",
          "type" : "string"
        },
        "funding" : {
          "title" : "Funding Agency and Award Number",
          "type" : "array",
          "items" : {
            "type" : "object",
            "properties" : {
              "name" : {
                "type" : "string"
              },
              "award" : {
                "type" : "string"
              }
            }
          }
        },
        "pushedToIkewai" : {
          "title" : "Pushed To Ikewai",
          "type" : "boolean"
        },
        "pushedToHydroshare" : {
          "title" : "Pushed To Hydroshare",
          "type" : "boolean"
        },
        "stagedToIkewai" : {
          "title" : "Staged To Ikewai",
          "type" : "boolean"
        },
        "stagedToHydroshare" : {
          "title" : "Staged To Hydroshare",
          "type" : "boolean"
        },
        "rejectedFromHydroshare" : {
          "title" : "Rejected From Hydroshare",
          "type" : "boolean"
        },
        "rejectedReasonHydroshare" : {
          "title" : "Rejected From Hydroshare Reason",
          "type" : "string"
        },
        "rejectedFromIkewai" : {
          "title" : "Rejected From Ikewai",
          "type" : "boolean"
        },
        "published" : {
          "title" : "Published",
          "type" : "string"
        },
        "hydroshareResourceId" : {
          "title" : "Hydroshare Resource ID",
          "type" : "string"
        },
        "stagedToHydroshareDate" : {
          "title" : "Date resource was staged to Hydroshare",
          "type" : "string"
        },
        "institution" : {
          "title" : "Participant Institution",
          "type" : "string"
        }
      },
      "required" : [ "title", "license_rights", "license_permission" ]
    }
```
