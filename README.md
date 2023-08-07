# gstchecker
The details of a company is fetched using the `requests` library and parsed with `BeautifulSoup4`. GSTIN number — a 15 digit tax identification number is used to generate the name, address, type, etc. of the company.

Run this command in the terminal to install `gstchecker` package

    pip install gstchecker

## Documentation

To import the file use the below code

    import gstchecker


The program uses default test url and input parameters for testing and educational purposes. To GET details from GSTIN use

    gstchecker.check("_15 character GSTIN goes here_")

You check whether the check() was a success or not using

    gstchecker.status()

|  variable name | entity value  |
| ------------ | ------------ |
|  `gstchecker.name` | Entity name  |
| `gstchecker.pan`  | Entity PAN  |
|  `gstchecker.person` |  Entity registree |
|  `gstchecker.type` | Entity type  |
| `gstchecker.add`  | Entity address  |
| `gstchecker.date`  | Entity registration date  |

To print a particular variable listed above use the function

    gstchecker.disp(_variable to print_)

To quickly print all the variables together

    gstchecker.printall()
To print all the variable seperated by \t ot \n then use the following function. The \t or \n must be included within single or double quotes.

    gstchecker.printwith("\n")

To use this program you need to have legal access from a website to GET details. The website should have two inputs in the form, one input for gstin number and another a hidded input for csrf token. The default must be changed before using. The author is not responsible for how the program is being used.

To change all the value of the request parameter, use the function
    
	gstcheckerset("http://example.com/search.php","inputName","csrfmidwaretoken")
To change the just the `url` of the program
    
    gstchecker.seturl("htttp://example.com/search.php")
To change just the `inputName` (It is the name="value" of the input tag)
    
	gstchecker.setinput("value")
To change only the `csrf` (It is the name="value" of the hidden input tag)
    
	gstchecker.setcsrf("value")

Note that these parameters must be change before calling `check()` for it apply.

| parameter  | variable name  |
| ------------ | ------------ |
|  URL value |  `gstchecker.url` |
| input tag name value  |  `gstchecker.inputName` |
| csrf hidden input tag name value  |  `gstchecker.csrfName` |

## Errors

Errors are listed in specific order so that that one error can lead to subsequent errors in the list.

| displayed error  | explanation  |
| ------------ | ------------ |
| `[Offline]`  |  `check()` was not called and no parameters were sent and no data received |
|  `[GET URL Failure]` |  means the url is incorrect/incompatible ot No Internet |
| `[Content retreival failure]`  | means url, input and csrf parameter are not compatible and no data was received  |
|  `[Parsing Failure]` | means that some data was received, but it was unable to translate to needed data. The site may have altered its HTML  |
|  `[No Error]` |  is shown when requesting status through `gstchecker.status()` if all function worked perfectly |

## Screenshots

![image](https://github.com/hariprasath112/gstchecker/assets/96934076/164cfd3b-24ce-49c4-9f02-35c25b3b2b4d)

![Screenshot 2023-08-07 214511](https://github.com/hariprasath112/gstchecker/assets/96934076/9bf7de71-70f3-4499-a7e6-fbb0631abfdb)

![image](https://github.com/hariprasath112/gstchecker/assets/96934076/e1060454-a90b-42f2-91a0-7819ebea7fb7)

![image](https://github.com/hariprasath112/gstchecker/assets/96934076/4ca7c28a-f80c-449d-8cb5-a2ba93bd8e51)

### Functionality issues
The program faces issues with correctly parsing ~~nature~~ (removed for improved functionality) and date. 

