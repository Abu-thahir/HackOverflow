# Ransomware-Detection
Visual C++ console application to detect ransomware activity on Windows OS. It consists of a registry monitor, filesystem watcher and a process detector.

# Requirements
* Visual Studio 2022
* Visual C++ 2022 redistributable
* Selenium chrome Driver based on chrome version  

# Description

Ransomware is a malware/malicious software program designed to block or disable access to the data your computer until a sum of money is paid.
The project aims at detecting and notifying the user of potential ransomware behavior on the windows system and helping them to recover their system from ransomware.

![Flowchart (1)](https://user-images.githubusercontent.com/69951869/161373549-7da62010-fa63-4135-bb8c-fb85917534f9.jpeg)

```
WEB BROWSER EXTENSION
```
We have created an extension called SayNO2Ransome , which allows the users to drag and drop the files or urls which they need to check for ransomware dectection and recovery.

```
DETECTION
```

* Detecting a Process commonly executed by Ransomware.(Here we have detecting VSSadmin process which is commonly run by Ransomware for deleting backup files-Shadow copies)
* Monitoring a commonly affected Windows Registry key for changes for change of roles and to maintain persistence.
* Creating a honeypot folder, and monitoring it for any file changes.(renames and deletes)
* Checking for malicious things flagged by other vendors using Virus Total API.

We have decided to check these parameters on which the behavior can be judged after studying the behavior of various ransomware.The project is multithreaded so that all the  features can be run asynchronously.

```
RECOVERY
```

* To find type and name of the ransomware , we have used a website called ID-RANSOMEWARE , a free service to the public using selenium.
* To find the decryptors for the ransomwares , we have automated the process of crawling the repository and NoMoreRansome.org using selenium.

Such that users can download the decryptors and remove the ransomwares from their systems.

## Screenshots:


