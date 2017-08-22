# PhoneNumGenerator

| Title :|PhoneNumGenerator|
|:------|:------:|
|**Author:**|**Carl Baccus**|
|**License**|GNU GENERAL PUBLIC LICENSE (https://github.com/cjbaccus/PhoneNumGenerator/blob/master/LICENSE)|
|**Description:**|
|This script is intended to be ran on cli.  The purpose is to generate a file named `<City>-Num.txt` that has every phone number available in that particular City based on a web query lookup, and sequencing through all 10,000 numbers within an area-code and prefix for that particular city. This generated file could be used for brute force checking to ensure phone numbers were not used for passwords or WPA2 secrets etc.|
|**Usage:**|

```  > python PhoneNumGenerator.py
	 > What state? <answer>
	 > What City?  <answer>
	 result will write out file with `<City>-Num.txt` name.
```


 

# Things to do:
* fix 9999 problem
* 