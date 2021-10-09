# sutd-stl1

This study was conducted as it should be of great interest to cybersecurity professionals and also the layman to have uncrackable passwords. Using multiple approaches to password generation and password quality checking, this paper aims to find out which password generation method created the set of passwords with the strongest resistance to guessability and the applicability of our password quality checker tool compared to those already available online.

Evaluating character frequencies and time to generate, we conclude that among all 6 password generation sources, the Python Secrets module is the most cryptographically secure, although generating large amounts of passwords with this module is time consuming, and this is to be expected as this module was created intended to be used for cryptography-purposes. To generate a handful of passwords, the Python Secrets module is the fastest generator. We also conclude that our password quality tool checker utilizing the Levenshtein algorithm, time to bruteforce and rainbow tables is more stringent than some other online sources in classifying a password as strong, making it more security-focused than user-focused.

_Save all files to the same folder to test the scripts. Separate modules might need to be imported by another user testing out this scripts._

**stl1_password_generator.py**
has been set to generate 5 passwords only per character combination and length for all 6 sources and will output saved csv file stl1_all.csv:

![image](https://user-images.githubusercontent.com/39832806/136648762-2f999faa-1a6d-4809-91fd-5d24f644d805.png)


**stl1_hasher.py**
outputs all the MD5 hashes and populates this folder with the respective text files for all the 90 columns in the first generated csv. An example of one of the columns in the csv, output as hash in txt file:

![image](https://user-images.githubusercontent.com/39832806/136648617-87eb2d7d-7fde-4fa3-8e1a-0577d675e90a.png)


**stl1_frequency.py**
outputs all the character occurrences count in descending order for all the 90 columns in the first generated csv and populates this folder with the respective text files. An example of the top 10 most used characters in RJ source, combination 12-LDS:

![image](https://user-images.githubusercontent.com/39832806/136648715-67a6a364-605c-4f3d-9f91-7950c96f148a.png)


**stl1_tool.py**
tool to test the password quality checker tool, scored 0 - 5 of 5 points. This tool utilizes the Levenshtein's algorithm, time taken to bruteforce and a pre-generated rainbow table. An example of an extremely weak password:

![image](https://user-images.githubusercontent.com/39832806/136648581-7319f88c-c0c2-4afa-b6b1-9de17a3ada4e.png)

